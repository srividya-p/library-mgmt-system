import imp
from admin import Admin
from login_system import LoginSystem

admin = Admin.createAdmin(LoginSystem('admin', 'admin123'))
