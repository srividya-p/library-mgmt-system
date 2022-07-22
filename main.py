from admin import Admin
from login_system import LoginSystem

admin = Admin.createAdmin(LoginSystem('admin', 'admin123'))

admin.addLibrarian('Mr. Librarian', 40, LoginSystem('lib', 'lib123'))
admin.credentials.login('admin', 'admin123')

librarian = admin.addLibrarian('Mr. Librarian', 40, LoginSystem('lib', 'lib123'))
admin.readLibrarian()
admin.updateLibrarian('age', 41)

student1 = admin.createStudentAccount('Student 1', 20, 130, LoginSystem('stu1', 'stu123'))
student2 = admin.createStudentAccount('Student 2', 22, 131, LoginSystem('stu2', 'stu123'))

librarian.credentials.login('lib', 'lib123')
student1.credentials.login('stu1', 'stu123')
student2.credentials.login('lib', 'stu123')

librarian.addBook('Book 1', 'Author 1', '#001', 2000, 250)
librarian.addBook('Book 1', 'Author 1', '#001', 2000, 250)
librarian.addBook('Book 2', 'Author 1', '#002', 2001, 250)
librarian.addBook('Book 3', 'Author 2', '#004', 2002, 300)
librarian.addBook('Book 4', 'Author 3', '#007', 2002, 400)

student1.requestBook('Book 1', librarian)
student1.returnBook('Book 1', librarian)

student1.getBooksByAuthorName('Author 1', librarian)

librarian.credentials.logout()
student1.credentials.logout()
admin.credentials.logout()

