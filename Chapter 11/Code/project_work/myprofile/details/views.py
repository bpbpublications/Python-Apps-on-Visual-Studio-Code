from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from myprofile import db
#from werkzeug.security import generate_password_hash,check_password_hash
from myprofile.models import Details, Users
from myprofile.details.forms import ProfileForm, UpdateDetailsForm



details = Blueprint('details', __name__)

@details.route('/submitform', methods=['GET', 'POST'])
def submitform():
    form = ProfileForm()
    #flash('Working...')
    if form.validate_on_submit():
        org = form.org.data,
        startdate=form.startdate.data,
        enddate=form.enddate.data,
        title=form.title.data,
        description=form.description.data,
        info_type=form.info_type.data
        record = Details(startdate, enddate, org, title, description, info_type)
        db.session.add(record)
        db.session.commit()
        flash('Details Saved!')
        #return redirect(url_for('users.login'))
        return render_template('addinfo.html', form=form)
    return render_template('addinfo.html', form=form)


@details.route('/editdetails', methods=['GET', 'POST'])
def editdetails():
    details = Details.query.all()
    if request.method == 'POST':
        data_id = request.form['type_radio']
        print('form submit=========>',data_id)
        Details.query.filter_by(id=data_id).delete()
        db.session.commit()
        print('delete done')
        return redirect("/editdetails", code=302)

    return render_template("editdetails.html",details=details)

@details.route('/editform', methods=['GET', 'POST'])
def editform():
    '''
    form = UpdateDetailsForm()
    '''
    flash('Working...')
    #option = request.form["type_radio"]
    #return render_template(option)
    #db.session.delete()
    #db.session.commit()

    #return render_template('editdetails.html')
    return redirect(url_for('details.editdetails'))