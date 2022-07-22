from user import User
from login_system import LoginSystemInterface
from book import Book

librarian = None

class Librarian(User):
    def __init__(self, fullName, age, authorizer = LoginSystemInterface):
        super().__init__(fullName, age, authorizer)

    @staticmethod
    def createLibrarian(fullName, age, authorizer):
        global librarian
        if librarian != None:
            return librarian
        librarian = Librarian(fullName, age, authorizer)
        print("Librarian created successfully.")
        return librarian

    @staticmethod
    def readLibrarian():
        global librarian
        if librarian == None:
            print('Librarian does not exist.')
            return 
        print(f"""
        Name: {librarian.fullName}
        Username: {librarian.authorizer.getUserName()}
        Age: {librarian.age}
        """)

    @staticmethod
    def updateLibrarian(property, newValue):
        global librarian
        if librarian == None:
            print('Librarian does not exist.')
            return 
        oldValue = str(getattr(librarian, property))
        setattr(librarian, property, newValue)
        print("Librarian's "+property+" changed from "+str(oldValue)+" to "+str(newValue))

    @staticmethod
    def deleteLibrarian():
        global librarian
        if librarian == None:
            print('Librarian does not exist.')
            return 
        librarian = None
        print("Librarian deleted successfully.")

    def addBook(self, bookName, authorName, ISBN, publicationYear, price):
        if not self.authorizer.isLoggedIn():
            print('You cannot perform this operation. you are not logged in.')
            return
        Book.addBook(self, bookName, authorName, ISBN, publicationYear, price)

    def readBookDetails(self,bookName):
        if not self.authorizer.isLoggedIn():
            print('You cannot perform this operation. you are not logged in.')
            return
        Book.displayBookDetail(bookName)

    def updateBook(self, bookName, property, newValue):
        if not self.authorizer.isLoggedIn():
            print('You cannot perform this operation. you are not logged in.')
            return
        Book.updateBookDetails(bookName, property, newValue)

    def deleteBook(self, bookName):
        if not self.authorizer.isLoggedIn():
            print('You cannot perform this operation. you are not logged in.')
            return
        Book.deleteBook(bookName)

    def processIssueRequest(self, bookName):
        if not self.authorizer.isLoggedIn():
            print('You cannot perform this operation. you are not logged in.')
            return
        return Book.issueBook(bookName)
       
    def acceptBookReturn(self, bookCopy):
        if not self.authorizer.isLoggedIn():
            print('You cannot perform this operation. you are not logged in.')
            return
        if not bookCopy.isIssued():
            return False, 'This book was not issued.'

        Book.returnBook(bookCopy)
        return True, ''

    # @staticmethod
    # def isLibrarianExists(username):
    #     i = -1
    #     for l in Librarian.allLibrarians:
    #         i += 1
    #         if l.authorizer.getUsername() == username:
    #             return True, i
    #     return False, "Librarian does not exists"

    # @staticmethod
    # def addLibrarian(fullName, age, authorizer):
    #     isLibrarianExists, _ = Librarian.isLibrarianExists(authorizer.getUsername())
    #     if isLibrarianExists:
    #         print("Librarian already exists.")
    #         return
        
    #     newLibrarian = Librarian(fullName, age, authorizer)
    #     Librarian.allLibrarians.append(newLibrarian)
    #     print("Librarian added successfully.")

    # @staticmethod
    # def readLibrarian(userName):
    #     isLibrarianExists, librarianIndex = Librarian.isLibrarianExists(userName)
    #     if not isLibrarianExists:
    #         print("Librarian does not exist.")
    #         return
    #     librarian = Librarian.allLibrarians[librarianIndex]
    #     print(f"""
    #     Name: {librarian.fullName}\n
    #     Username: {librarian.authorizer.getUserName()}\n
    #     Age: {librarian.age}\n\n
    #     """)
        
    # @staticmethod
    # def updateLibrarian(userName, property, newValue):
    #     isLibrarianExists, librarianIndex = Librarian.isLibrarianExists(userName)
    #     if not isLibrarianExists:
    #         print("Librarian does not exist.")
    #         return
    #     setattr(Librarian.allLibrarians[librarianIndex], property, newValue)
    #     print("Librarian updated successfully.")

    # @staticmethod
    # def deleteLibrarian(userName):
    #     isLibrarianExists, librarianIndex = Librarian.isLibrarianExists(userName)
    #     if not isLibrarianExists:
    #         print("Librarian does not exist.")
    #         return
    #     Librarian.allLibrarians[librarianIndex].isExists = False
    #     print("Librarian deleted successfully.")