from flask import render_template,url_for,flash, redirect,request,Blueprint,abort
from flask_login import current_user,login_required
from myprofile import db
from myprofile.models import Testimonials
from myprofile.testimonials.forms import TestimonialsForm
from myprofile.details.forms import UpdateDetailsForm

testimonials = Blueprint('testimonials',__name__)

@testimonials.route('/create',methods=['GET','POST'])
@login_required
def create_post():
    if current_user.acc_type == 0:
        #if admin user
        #form = UpdateDetailsForm()
        return redirect(url_for('details.editdetails'))
        #return render_template('editdetails.html')
    else:
        #if non-admin user
        form = TestimonialsForm()

        if form.validate_on_submit():

            blog_post = Testimonials(title=form.title.data,
                                 text=form.text.data,
                                 user_id=current_user.id
                                 )
            db.session.add(blog_post)
            db.session.commit()
            flash("Testimonial Added")
            return redirect(url_for('core.index'))

        return render_template('create_testimonial.html',form=form)


# int: makes sure that the blog_post_id gets passed as in integer
# instead of a string so we can look it up later.
@testimonials.route('/<int:blog_post_id>')
def blog_post(blog_post_id):
    # grab the requested blog post by id number or return 404
    blog_post = Testimonials.query.get_or_404(blog_post_id)
    return render_template('blog_post.html',title=blog_post.title,
                            date=blog_post.date,post=blog_post
    )

@testimonials.route("/<int:blog_post_id>/update", methods=['GET', 'POST'])
@login_required
def update(blog_post_id):
    blog_post = Testimonials.query.get_or_404(blog_post_id)
    if blog_post.author != current_user:
        # Forbidden, No Access
        abort(403)

    form = TestimonialsForm()
    if form.validate_on_submit():
        blog_post.title = form.title.data
        blog_post.text = form.text.data
        db.session.commit()
        flash('Post Updated')
        return redirect(url_for('blog_posts.blog_post', blog_post_id=blog_post.id))
    # Pass back the old blog post information so they can start again with
    # the old text and title.
    elif request.method == 'GET':
        form.title.data = blog_post.title
        form.text.data = blog_post.text
    return render_template('create_post.html', title='Update',
                           form=form)


@testimonials.route("/<int:blog_post_id>/delete", methods=['POST'])
@login_required
def delete_post(blog_post_id):
    blog_post = Testimonials.query.get_or_404(blog_post_id)
    if blog_post.author != current_user:
        abort(403)
    db.session.delete(blog_post)
    db.session.commit()
    flash('Testimonial has been deleted')
    return redirect(url_for('core.index'))
