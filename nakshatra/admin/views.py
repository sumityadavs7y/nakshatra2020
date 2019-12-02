from flask import redirect, url_for, request, abort, flash
from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.fileadmin import FileAdmin
from flask_login import current_user
from nakshatra.models import User

class AdminView(ModelView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.static_folder = 'static'
    
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_type=='admin'
    
    def inaccessible_callback(self, name, **kwargs):
        if current_user.is_authenticated:
            abort(403)
        elif not self.is_accessible():
            flash('You need to be login as admin', 'info')
            return redirect(url_for('users.login', next=request.url))

class FileAdminExt(FileAdmin):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_type=='admin'