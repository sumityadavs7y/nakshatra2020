from flask import Blueprint, request, render_template, flash, request, redirect
from flask_login import current_user, login_user, logout_user

from nakshatra import db, bcrypt
from nakshatra.models import User

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    return render_template('main/home.html',title='Home')

@main.route("/gallery")
def gallery():
    return render_template('main/gallery.html', title='About')

@main.route("/teams")
def teams():
    return render_template('main/teams.html', title='About')

@main.route("/about")
def about():
    return render_template('main/about.html', title='About')