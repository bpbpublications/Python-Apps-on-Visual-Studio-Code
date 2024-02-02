# Form Based Imports

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, HiddenField
from wtforms.validators import DataRequired
from wtforms import StringField, BooleanField
from wtforms.fields import DateField, EmailField, TelField

# User Based Imports
#from flask_login import current_user
from myprofile.models import Details


class ProfileForm(FlaskForm):
    # no empty titles or text possible
    id = HiddenField()
    org = StringField('Organization', render_kw={"placeholder": "Organisation"})
    startdate = DateField('Start Date')
    enddate = DateField('End Date')

    title = StringField('Title', validators=[DataRequired()], render_kw={"placeholder": "Title"})
    description = TextAreaField('Description', validators=[DataRequired()], render_kw={"placeholder": "Description"})
    dropdown_list = ['Project', 'Work Experience','Education', 'Expertise','Extra Curricular']  # You can get this from your model
    #info_type = SelectField('Work Type', choices=dropdown_list)
    info_type = SelectField('Choose the Data Type',
        choices=['Project', 'Work Experience','Education', 'Expertise'])
    #info_type = TextAreaField('Text', validators=[DataRequired()])

    submitform = SubmitField('Save Data')

#Update for admin user only
class UpdateDetailsForm(FlaskForm):
    # no empty titles or text possible
    startdate = DateField('Start Date')
    enddate = DateField('Start Date')
    org = StringField('Organization')
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    dropdown_list = ['Project', 'Work Experience','Education', 'Expertise','Extra Curricular']  # You can get this from your model
    info_type = SelectField('info_type', choices=dropdown_list, default=1)

    editform = SubmitField('Save Data')

