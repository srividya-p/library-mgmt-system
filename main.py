from admin import Admin
from login_system import LoginSystem

admin = Admin.createAdmin(LoginSystem('admin', 'admin123'))

admin.addLibrarian('Mr. Librarian', 40, LoginSystem('lib', 'lib123'))
admin.authorizer.login('admin', 'admin123')

admin.addLibrarian('Mr. Librarian', 40, LoginSystem('lib', 'lib123'))
admin.readLibrarian()
admin.updateLibrarian('age', 41)
