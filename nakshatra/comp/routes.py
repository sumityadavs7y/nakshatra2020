from flask import Blueprint, request, render_template

from nakshatra.models import User
from nakshatra import db

comp = Blueprint('comp', __name__)

@comp.route("")
@comp.route("/mcq")
def mcq():
    # user=User(college='asdf',password='asdasf')
    # db.session.add(user)
    # db.session.commit()
    return render_template('comp/mcq.html',title='MCQ')

@comp.route("/treasure")
def treasure():
    return render_template('comp/treasure.html', title='Treasure')