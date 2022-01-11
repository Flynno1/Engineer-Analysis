from flask import Blueprint, render_template
from flask.templating import render_template_string

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/login')
def hologin():
    return render_template("login.html")

