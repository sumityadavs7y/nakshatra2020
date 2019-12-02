from datetime import datetime
from flask_login import UserMixin, current_user
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app

from nakshatra import db, login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    college = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    user_type = db.Column(db.String(20), nullable=False, default='participant')

    scores = db.relationship('Score', backref='submitted_mcq_by', lazy=True)
    treasure_scores = db.relationship('Treasuresubmission', backref='submitted_treasure_by', lazy=True)
    ide_submissions = db.relationship('Idesubmission', backref='submitted_ide_by', lazy=True)

    def __repr__(self):
        return f'User({self.college}, {self.user_type})'

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text, nullable=False)
    optiona = db.Column(db.String(120), nullable=False)
    optionb = db.Column(db.String(120), nullable=False)
    optionc = db.Column(db.String(120), nullable=False)
    optiond = db.Column(db.String(120), nullable=False)
    answer = db.Column(db.String(10), nullable=False)

class Score(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    score = db.Column(db.Float,default=0)
    is_submitted = db.Column(db.Boolean, default=False, nullable=False)
    comp_id = db.Column(db.Integer, db.ForeignKey('competition.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class Competition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comp_name = db.Column(db.String(120), nullable=False, unique=True)
    duration = db.Column(db.Integer, nullable=False)

    scores = db.relationship('Score', backref='submissions', lazy=True)

class Treasurequestion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(30), nullable=False)
    answer = db.Column(db.String(60), nullable=False)

    submission = db.relationship('Treasuresubmission', backref='submission_by', lazy=True)
    hints = db.relationship('Treasurehint', backref='hints_question_by', lazy=True)

class Treasurehint(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hint = db.Column(db.String(120), nullable=False)

    question_id = db.Column(db.Integer, db.ForeignKey('treasurequestion.id'), nullable=False)

class Treasuresubmission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    submitted_answer = db.Column(db.String(120))
    question_id = db.Column(db.Integer, db.ForeignKey('treasurequestion.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class Idequestion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text, nullable=False)

    ide_submissions = db.relationship('Idesubmission', backref='ide_submissions', lazy=True)

class Idesubmission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    answer = db.Column(db.Text, nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('idequestion.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)