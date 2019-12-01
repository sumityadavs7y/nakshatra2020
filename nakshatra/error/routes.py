from flask import render_template, redirect, url_for, flash, Blueprint, request
from flask_login import login_user, current_user, logout_user, login_required

from nakshatra import db, bcrypt
from nakshatra.models import User

error = Blueprint('errors', __name__)

@error.errorhandler(404)
def page_not_found(e):
    return 'Page Not Found'

@error.errorhandler(403)
def unauthorized(e):
    return 'unauthorized'