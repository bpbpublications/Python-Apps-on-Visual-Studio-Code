from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from myprofile import db
from myprofile.models import Users, Testimonials, Details
from myprofile.users.forms import RegistrationForm, LoginForm, UpdateUserForm
from myprofile.details.forms import ProfileForm
from myprofile.users.picture_handler import add_profile_pic
import datetime

users = Blueprint('users', __name__)

@users.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = Users(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)

        db.session.add(user)
        db.session.commit()
        flash('Thanks for registering! Now you can login!')
        return redirect(url_for('users.login'))
    return render_template('register.html', form=form)

@users.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():
        # Grab the user from our User Models table
        user = Users.query.filter_by(email=form.email.data).first()

        # Check that the user was supplied and the password is right
        # The verify_password method comes from the User object
        # https://stackoverflow.com/questions/2209755/python-operation-vs-is-not

        if user.check_password(form.password.data) and user is not None:
            #Log in the user

            login_user(user)
            flash('Logged in successfully.')

            # If a user was trying to visit a page that requires a login
            # flask saves that URL as 'next'.
            next = request.args.get('next')

            # So let's now check if that next exists, otherwise we'll go to
            # the welcome page.
            if next == None or not next[0]=='/':
                next = url_for('core.index')

            return redirect(next)
    return render_template('login.html', form=form)




@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('core.index'))


@users.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    #user = Users.query.filter_by(email=form.email.data).first()

    if current_user.acc_type==0:
        form = ProfileForm()
        # if form.validate_on_submit():
        #     print('#############################################')
        #     print(form)

        if request.method == 'POST':
            org = form.org.data
            startdate = form.startdate.data
            enddate = form.enddate.data
            #startdate = datetime.datetime.strptime(
                     #form.startdate.data,
                    # '%d-%m-%Y')
            title = form.title.data
            description = form.description.data
            
            info_type = form.info_type.data
            record = Details(org=org, startdate=startdate, enddate=enddate, title=title, description=description, info_type=info_type)
            db.session.add(record)
            db.session.commit()
            #flash('User Account Updated')

            #print(org)
            #print('=====>',startdate)
            #print(info_type)
            
            print('*****************************************')
            #print(form)

        return render_template('addinfo.html', form=form)

    else:  #non admin users

        form = UpdateUserForm()

        if form.validate_on_submit():
            print(form)
            if form.picture.data:
                username = current_user.username
                pic = add_profile_pic(form.picture.data,username)
                current_user.profile_image = pic

            current_user.username = form.username.data
            current_user.email = form.email.data
            db.session.commit()
            flash('User Account Updated')
            return redirect(url_for('users.account'))

        elif request.method == 'GET':
            form.username.data = current_user.username
            form.email.data = current_user.email

        profile_image = url_for('static', filename='profile_pics/' + current_user.profile_image)
        return render_template('account.html', profile_image=profile_image, form=form)


@users.route("/<username>")
def user_posts(username):
    page = request.args.get('page', 1, type=int)
    user = Users.query.filter_by(username=username).first_or_404()
    blog_posts = Testimonials.query.filter_by(author=user).order_by(Testimonials.date.desc()).paginate(page=page, per_page=5)
    return render_template('user_blog_posts.html', blog_posts=blog_posts, user=user)
