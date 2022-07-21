import stat
from user import User
# add the class name
from login_system import LoginSystemInterface

class Librarian(User):

    allLibrarians = []

    def __init__(self):
        self.authorizer = LoginSystemInterface

    @staticmethod
    def addLibrarian():
        pass

    @staticmethod
    def readLibrarian():
        pass

    @staticmethod
    def updateLibrarian():
        pass

    @staticmethod
    def deleteLibrarian():
        pass

    def processIssueRequest():
        pass

    def acceptBookReturn():
        pass

    def addBook():
        pass

    def readBookDetails():
        pass

    def updateBook():
        pass

    def deleteBook():
        pass

    def createStudentAccount():
        pass

    def searchStudentDetails():
        pass

    def updateStudent():
        pass

    def deleteStudent():
        pass
