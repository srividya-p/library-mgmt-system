from user import User
from login_system import LoginSystemInterface
from book import Book
from student import Student

class Librarian(User):

    allLibrarians = []

    def __init__(self):
        self.authorizer = LoginSystemInterface

    @staticmethod
    def isLibrarianExists(username):
        i = -1
        for l in Librarian.allLibrarians:
            i += 1
            if l.authorizer.getUsername() == username:
                return True, i
        return False, "Librarian does not exists"

    @staticmethod
    def addLibrarian(name, age, authorizer):
        isLibrarianExists, librarianIndex = Librarian.isLibrarianExists(authorizer.getUsername())
        if isLibrarianExists:
            return False, "Librarian already exists"
        newLibrarian = Librarian(name, age, authorizer)
        Librarian.allLibrarians.append(newLibrarian)
        return True, "Librarian added successfully"

    @staticmethod
    def readLibrarian(authorizer, property):
        isLibrarianExists, librarianIndex = Librarian.isLibrarianExists(authorizer.getUsername())
        if not isLibrarianExists:
            return False, "Librarian does not exists"
        returnvalue = getattr(Librarian.allLibrarians[librarianIndex], property)
        return True, returnvalue

    @staticmethod
    def updateLibrarian(authorizer, property, newValue):
        isLibrarianExists, librarianIndex = Librarian.isLibrarianExists(authorizer.getUsername())
        if not isLibrarianExists:
            return False, "Librarian does not exists"
        setattr(Librarian.allLibrarians[librarianIndex], property, newValue)
        return True, "Librarian updated successfully"

    @staticmethod
    def deleteLibrarian(authorizer):
        isLibrarianExists, librarianIndex = Librarian.isLibrarianExists(authorizer.getUsername())
        if not isLibrarianExists:
            return False, "Librarian does not exists"
        Librarian.allLibrarians[librarianIndex].isExist = False
        return True, "Librarian deleted successfully"

    def processIssueRequest(bookName):
        isBookIssued, bookObject = Book.issueBook(bookName)
        if not isBookIssued:
            return False, None
        return True, bookObject

    def acceptBookReturn(bookName):
        if Book.returnBook(bookName):
            return True

    def addBook(bookName, authorName, ISBN, publicationYear, price):
        Book.addBook(bookName, authorName, ISBN, publicationYear, price)
        return

    def readBookDetails(bookName):
        Book.displayBookDetail(bookName)
        return

    def updateBook(bookName, property, newValue):
        Book.updateBookDetails(bookName, property, newValue)
        return

    def deleteBook(bookName):
        Book.deleteBook(bookName)
        return

    def createStudentAccount(name, age, authorizer):
        isStudentCreated, statement = Student.addStudent(name, age, authorizer)
        if not isStudentCreated:
            return False, statement
        return True, statement

    def searchStudentDetails(authorizer, property):
        isStudentDetailsExists, studentDetails = Student.readStudent(authorizer, property)
        if not isStudentDetailsExists:
            return False, None
        return True, studentDetails

    def updateStudent(authorizer, property, newValue):
        isUpdated, statement = Student.updateStudent(authorizer, property, newValue)
        if not isUpdated:
            return False, statement
        return True, statement

    def deleteStudent(authorizer):
        isDeleted, statement = Student.deleteStudent(authorizer)
        if not isDeleted:
            return False, statement
        return True, statement
    
    def fetchBooksByAuthor(authorName):
        Book.displayBookByAuthorName(authorName)
        return
