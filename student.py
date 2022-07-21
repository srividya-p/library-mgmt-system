
from user import User

class Student(User):

    allStudents = []

    def init(self, Rollno):
        self.rollno = Rollno
        self.myBooks = []
        
    @staticmethod
    def requestBookName(BookId,Bookname):
        isBookExist, book = Book.findBook(authorName)
        if isBookExist:
            return False, "Book is not available"    
        Book.bookId += 1
        newBook = Book(booId, authorName)
        Book.allBooks.append(newBook)
        return True, "Book available!"

    @staticmethod
    def returnBook(BookName):
        return book 

        
    @staticmethod
    def findMyBookByName(AuthorName,myBooks):
        myBooks = []
        for Book in Book.MyBooks:
            if book.AuthoName == AuthorName:
                Books.append((book.bookName, AuthorName))
                return book




    @staticmethod
    def addStudent():
        pass

    @staticmethod
    def readStudent():
        pass

    @staticmethod
    def updateStudent():
        pass

    @staticmethod
    def deleteStudent():
        pass








        
