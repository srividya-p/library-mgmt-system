from __future__ import annotations

from user import User
from login_system import LoginSystemInterface
from book import Book
from book_copy import BookCopy

librarian = None

class Librarian(User):
    def __init__(self, fullName, age, credentials = LoginSystemInterface) -> None:
        super().__init__(fullName, age, credentials)

    @staticmethod
    def createLibrarian(fullName, age, credentials) -> Librarian:
        global librarian
        if librarian != None:
            return librarian
        librarian = Librarian(fullName, age, credentials)
        print("Librarian created successfully.")
        return librarian

    @staticmethod
    def readLibrarian() -> None:
        global librarian
        if librarian == None:
            print('Librarian does not exist.')
            return 
        print(f"""
        Name: {librarian.fullName}
        Username: {librarian.credentials.getUserName()}
        Age: {librarian.age}
        """)

    @staticmethod
    def updateLibrarian(property, newValue) -> None:
        global librarian
        if librarian == None:
            print('Librarian does not exist.')
            return 
        oldValue = str(getattr(librarian, property))
        setattr(librarian, property, newValue)
        print("Librarian's "+property+" changed from "+str(oldValue)+" to "+str(newValue))

    @staticmethod
    def deleteLibrarian() -> None:
        global librarian
        if librarian == None:
            print('Librarian does not exist.')
            return 
        librarian = None
        print("Librarian deleted successfully.")

    def addBook(self, bookName, authorName, ISBN, publicationYear, price) -> None:
        if not self.credentials.isLoggedIn():
            print('You cannot perform this operation. you are not logged in.')
            return
        Book.addBook(bookName, authorName, ISBN, publicationYear, price)

    def readBookDetails(self,bookName) -> None:
        if not self.credentials.isLoggedIn():
            print('You cannot perform this operation. you are not logged in.')
            return
        Book.displayBookDetail(bookName)

    def updateBook(self, bookName, property, newValue) -> None:
        if not self.credentials.isLoggedIn():
            print('You cannot perform this operation. you are not logged in.')
            return
        Book.updateBookDetails(bookName, property, newValue)

    def deleteBook(self, bookName) -> None:
        if not self.credentials.isLoggedIn():
            print('You cannot perform this operation. you are not logged in.')
            return
        Book.deleteBook(bookName)

    def processIssueRequest(self, bookName) -> tuple[bool, str, BookCopy]:
        if not self.credentials.isLoggedIn():
            print('You cannot perform this operation. you are not logged in.')
            return
        return Book.issueBook(bookName)
       
    def acceptBookReturn(self, bookCopy) -> str:
        if not self.credentials.isLoggedIn():
            return False, 'You cannot perform this operation. you are not logged in.'
        if not bookCopy.getIssueStatus():
            return 'This book was not issued.'

        Book.returnBook(bookCopy)
        return 'Book returned successfully.'

    def fetchBooksByAuthor(self, authorName):
        Book.displayBooksByAuthor(authorName)
