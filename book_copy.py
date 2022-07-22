from uuid import uuid4

class BookCopy:
    def __init__(self, bookCopyId, bookId, bookName, ISBN, publicationYear, price) -> None:
        self.bookCopyId = bookCopyId
        self.bookId = bookId
        self.bookName = bookName
        self.ISBN = ISBN
        self.publicationYear = publicationYear
        self.price = price
        self.returnDate = None
        self.isExists = True

    def createBookCopy(self, bookId, bookName, ISBN, publicationYear, price):
        bookCopyId = str(uuid4)
        newBookCopy = (bookCopyId, bookId, bookName, ISBN, publicationYear, price)
        return newBookCopy

    def displayBookCopy(self):
        print(f"""
        \tCopy ID: {self.bookCopyId}\n
        \tISBN: {self.ISBN}\n
        \tPublication Year: {self.publicationYear}\n
        \tPrice: {self.price}\n
        \tReturn Date: {self.returnDate}\n\n
        """)

    def updateBookCopy(self, property, newValue):
        oldValue = str(getattr(self, property))
        setattr(self, property, newValue)
        print(self.bookName+"'s "+property+" changed from "+oldValue
                +" to "+str(getattr(self, property)))

    def deleteBookCopy(self):
        self.isExists = False

    def isIssued(self):
        return self.returnDate != None