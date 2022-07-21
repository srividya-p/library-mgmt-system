from login_system import LoginSystemInterface
from librarian import Librarian

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
        Librarian.addLibrarian(fullName, age, authorizer)

    def readLibrarian(self, userName):
        Librarian.readLibrarian(userName)

    def updateLibrarian(self, userName, property, newValue):
        Librarian.readLibrarian(userName, property, newValue)

    def deleteLibrarian(self, userName):
        Librarian.deleteLibrarian(userName)