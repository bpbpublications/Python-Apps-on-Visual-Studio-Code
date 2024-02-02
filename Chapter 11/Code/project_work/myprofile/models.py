#models.py
from myprofile import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)

class Users(db.Model,UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True)
    acc_type = db.Column(db.Integer,default=1) # 1 for regular user, 0 for admin handled within
    profile_image = db.Column(db.String(64),nullable=False,default='default_profile.png')
    email = db.Column(db.String(64),unique=True,index=True)
    username = db.Column(db.String(64),unique=True,index=True)
    password_hash = db.Column(db.String(128))

    testimonials = db.relationship('Testimonials',backref='author',lazy=True)
    #details = db.relationship('Details', backref='user_id', lazy=True)

    def __init__(self,email,username,password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f"Username {self.username}"

class Details(db.Model):
    __tablename__ = 'details'
    #users = db.relationship(Users)

    id = db.Column(db.Integer,primary_key=True)
    #user_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable=False)
    org = db.Column(db.Text, nullable=False)
    startdate = db.Column(db.Date) #,nullable=False,default=datetime.utcnow)
    enddate = db.Column(db.Date) #, nullable=False, default=datetime.utcnow)
    title = db.Column(db.String(140),nullable=False)
    description = db.Column(db.Text,nullable=False)
    info_type = db.Column(db.Text)  #NOT This 1 - for Education, 2 for Expertise 3 for Projects 4 Others

    def __init__(self, org, startdate,enddate,title,description,info_type):
        #self.id = id
        #self.user_id = user_id
        self.org = org
        self.startdate = startdate
        self.enddate = enddate
        self.title = title
        self.description = description
        #'Project', 'Work Experience','Education', 'Expertise','Extra Curricular'
        self.info_type = info_type


    '''
    def __repr__(self):
        return f"Post ID: {self.id} -- Date: {self.date} --- {self.title}"
    '''

class Testimonials(db.Model):

    users = db.relationship(Users)

    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable=False)

    date = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    title = db.Column(db.String(140),nullable=False)
    text = db.Column(db.Text,nullable=False)

    def __init__(self,title,text,user_id):
        self.title = title
        self.text = text
        self.user_id = user_id

    def __repr__(self):
        return f"Post ID: {self.id} -- Date: {self.date} --- {self.title}"
