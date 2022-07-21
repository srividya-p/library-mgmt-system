from login_system import LoginSystem
from admin import Admin

admin = Admin.createAdmin(LoginSystem(userName='admin', password='admin123'))