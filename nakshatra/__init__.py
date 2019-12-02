from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from dotenv import load_dotenv
import os.path as op

load_dotenv(".env",verbose=True)
from nakshatra.config import Config

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    from nakshatra.admin.views import AdminView, FileAdminExt
    from nakshatra.models import User, Question, Score, Competition

    admin = Admin(app, name='Dashboard', index_view=AdminView(User, db.session, url='/admin', endpoint='admin'))
    path = op.join(op.dirname(__file__), 'static')
    admin.add_view(FileAdminExt(path, '/static/', name='Static Files',url='fileadmin'))
    admin.add_view(AdminView(Question, db.session))
    admin.add_view(AdminView(Competition, db.session))
    admin.add_view(AdminView(Score, db.session))
    
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    
    from nakshatra.main.routes import main
    from nakshatra.comp.routes import comp
    from nakshatra.users.routes import users
    from nakshatra.error.routes import page_not_found, unauthorized

    with app.app_context():
        db.create_all()

    app.register_blueprint(main)
    app.register_blueprint(comp, url_prefix='/comp')
    app.register_blueprint(users)
    app.register_error_handler(404,page_not_found)
    app.register_error_handler(403,unauthorized)

    return app
