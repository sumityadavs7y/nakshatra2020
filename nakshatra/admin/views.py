from flask import redirect, url_for, request
from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.fileadmin import FileAdmin
from flask_login import current_user
from nakshatra.models import User

class AdminView(ModelView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.static_folder = 'static'
    
    def is_accessible(self):
        return True #session.get('user') == 'Administrator'
    
    def inaccessible_callback(self, name, **kwargs):
        if not self.is_accessible():
            return redirect(url_for('main.home', next=request.url))

class FileAdminExt(FileAdmin):
    def is_accessible(self):
        return True #session.get('user') == 'Administrator'