#core/views.py
from flask import render_template, request,Blueprint
from myprofile.models import Testimonials, Details


'''
A blueprint defines a collection of views, templates, static files 
and other elements that can be applied to an application. For example, 
let's imagine that we have a blueprint for an admin panel. This blueprint 
would define the views for routes like /admin/login and /admin/dashboard.
'''
core=Blueprint('core',__name__)

@core.route('/')
def index():
    return render_template("index.html")

@core.route('/goals')
def goals():
    return render_template("goals.html")

@core.route('/activities')
def activities():
    return render_template("activities.html")
@core.route('/testimonials')
def alltestimonials():
    testimonials=Testimonials.query.all()
    return render_template("alltestimonials.html", testimonials=testimonials)

@core.route('/profile')
def profile():
    details=Details.query.all()
    return render_template("profile.html", details=details)



