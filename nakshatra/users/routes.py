from flask import render_template, redirect, url_for, flash, Blueprint, request
from flask_login import login_user, current_user, logout_user, login_required

from nakshatra import db, bcrypt
from nakshatra.models import User

users = Blueprint('users', __name__)

@users.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('users/register.html')

@users.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    # if login successful
    # return redirect(request.args.get('next') or url_for('home'))
    return render_template('login.html')

@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.home'))