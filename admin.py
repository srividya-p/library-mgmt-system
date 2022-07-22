from login_system import LoginSystemInterface
from librarian import Librarian
from student import Student

admin = None
class Admin:
    def __init__(self, authorizer=LoginSystemInterface):
        self.authorizer = authorizer

    @staticmethod
    def createAdmin(authorizer):
        global admin
        if admin != None:
            return admin
        admin = Admin(authorizer)
        return admin

    def addLibrarian(self, fullName, age, authorizer):
        if not self.authorizer.isLoggedIn():
            print('You cannot perform this operation. you are not logged in.')
            return
        Librarian.createLibrarian(fullName, age, authorizer)

    def readLibrarian(self):
        if not self.authorizer.isLoggedIn():
            print('You cannot perform this operation. you are not logged in.')
            return
        Librarian.readLibrarian()

    def updateLibrarian(self, property, newValue):
        if not self.authorizer.isLoggedIn():
            print('You cannot perform this operation. you are not logged in.')
            return
        Librarian.updateLibrarian(property, newValue)

    def deleteLibrarian(self):
        if not self.authorizer.isLoggedIn():
            print('You cannot perform this operation. you are not logged in.')
            return
        Librarian.deleteLibrarian()

    def createStudentAccount(self, fullName, age, rollNo, authorizer):
        if not self.authorizer.isLoggedIn():
            print('You cannot perform this operation. you are not logged in.')
            return
        Student.addStudent(fullName, age, rollNo, authorizer)

    def searchStudentDetails(self, userName):
        if not self.authorizer.isLoggedIn():
            print('You cannot perform this operation. you are not logged in.')
            return
        Student.findStudent(userName)

    def updateStudent(self, userName, property, newValue):
        if not self.authorizer.isLoggedIn():
            print('You cannot perform this operation. you are not logged in.')
            return
        Student.updateStudent(userName, property, newValue)

    def deleteStudent(self, userName):
        if not self.authorizer.isLoggedIn():
            print('You cannot perform this operation. you are not logged in.')
            return
        Student.deleteStudent(userName)