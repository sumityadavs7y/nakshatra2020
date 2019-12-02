from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask_login import login_required, current_user
from datetime import datetime, timedelta

from nakshatra.models import User
from nakshatra import db
from nakshatra.models import Question, Score, Competition

comp = Blueprint('comp', __name__)

@comp.route("/mcq", methods=['GET','POST'])
@login_required
def mcq():
    questions = Question.query.order_by(Question.id).all()
    competition = Competition.query.filter_by(comp_name='mcq').first()
    remaining_minute = competition.duration
    remaining_second = 0
    score = Score.query.filter_by(comp_id=competition.id,user_id=current_user.id).first()
    if request.method=='POST':
        no_of_questions = len(questions)
        marks=0
        for i in range(no_of_questions):
            if str(questions[i].answer) == str(request.form.get('radio'+str(i))):
                marks=marks+1
            elif not request.form.get('radio'+str(i)):
                pass
            else:
                marks = marks - 0.5
        score.score=marks
        score.is_submitted=True
        db.session.commit()
        flash('Submitted', 'primary')
        return redirect(url_for('main.home'))
    if not score:
        score = Score(comp_id=competition.id,user_id=current_user.id)
        db.session.add(score)
        db.session.commit()
    elif score.is_submitted:
        flash('Already Submitted can\'t re-attempt', 'danger')
        return redirect(url_for('main.home'))
    else:
        end_time=score.start_time+timedelta(minutes=competition.duration)
        print(datetime.utcnow())
        print(end_time)
        if end_time > datetime.utcnow():
            residual = end_time - datetime.utcnow()
            print(residual.total_seconds())
            remaining_minute = int(residual.total_seconds()/60)
            remaining_second = int(residual.total_seconds()%60)
        else:
            score.is_submitted=True
            db.session.commit()
            flash('Your time is Over for MCQ','danger')
            return redirect(url_for('main.home'))
    return render_template('comp/mcq.html',title='MCQ', questions=questions, remaining_minute=remaining_minute, remaining_second=remaining_second)

@comp.route('/treasure',defaults={'question_id': 1})
@comp.route('/treasure/<int:question_id>')
@login_required
def treasure(question_id):
    return render_template('comp/treasure.html', title='Treasure')