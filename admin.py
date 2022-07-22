from __future__ import annotations

from login_system import LoginSystemInterface
from librarian import Librarian
from student import Student

admin = None
class Admin:
    def __init__(self, credentials=LoginSystemInterface):
        self.credentials = credentials

    @staticmethod
    def createAdmin(credentials) -> Admin:
        global admin
        if admin != None:
            return admin
        admin = Admin(credentials)
        return admin

    def addLibrarian(self, fullName, age, credentials) -> Librarian:
        if not self.credentials.isLoggedIn():
            print('You cannot perform this operation. you are not logged in.')
            return
        return Librarian.createLibrarian(fullName, age, credentials)

    def readLibrarian(self) -> None:
        if not self.credentials.isLoggedIn():
            print('You cannot perform this operation. you are not logged in.')
            return
        Librarian.readLibrarian()

    def updateLibrarian(self, property, newValue) -> None:
        if not self.credentials.isLoggedIn():
            print('You cannot perform this operation. you are not logged in.')
            return
        Librarian.updateLibrarian(property, newValue)

    def deleteLibrarian(self) -> None:
        if not self.credentials.isLoggedIn():
            print('You cannot perform this operation. you are not logged in.')
            return
        Librarian.deleteLibrarian()

    def createStudentAccount(self, fullName, age, rollNo, credentials) -> Student:
        if not self.credentials.isLoggedIn():
            print('You cannot perform this operation. you are not logged in.')
            return
        return Student.addStudent(fullName, age, rollNo, credentials)

    def searchStudentDetails(self, userName) -> None:
        if not self.credentials.isLoggedIn():
            print('You cannot perform this operation. you are not logged in.')
            return
        Student.findStudent(userName)

    def updateStudent(self, userName, property, newValue) -> None:
        if not self.credentials.isLoggedIn():
            print('You cannot perform this operation. you are not logged in.')
            return
        Student.updateStudent(userName, property, newValue)

    def deleteStudent(self, userName) -> None:
        if not self.credentials.isLoggedIn():
            print('You cannot perform this operation. you are not logged in.')
            return
        Student.deleteStudent(userName)