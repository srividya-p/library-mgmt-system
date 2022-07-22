from __future__ import annotations

from uuid import uuid4

class BookCopy:
    def __init__(self, bookCopyId, bookId, bookName, ISBN, publicationYear, price) -> None:
        self.bookCopyId = bookCopyId
        self.bookId = bookId
        self.bookName = bookName
        self.ISBN = ISBN
        self.publicationYear = publicationYear
        self.price = price
        self.issueDate = None
        self.returnDate = None
        self.isIssued = False
        self.isExists = True

    @staticmethod
    def createBookCopy(bookId, bookName, ISBN, publicationYear, price) -> BookCopy:
        bookCopyId = str(uuid4)
        newBookCopy = BookCopy(bookCopyId, bookId, bookName, ISBN, publicationYear, price)
        return newBookCopy

    def displayBookCopy(self) -> None:
        print(f"""
        \tCopy ID: {self.bookCopyId}\n
        \tISBN: {self.ISBN}\n
        \tPublication Year: {self.publicationYear}\n
        \tPrice: {self.price}\n
        \tReturn Date: {self.returnDate}\n\n
        """)

    def updateBookCopy(self, property, newValue) -> None:
        oldValue = str(getattr(self, property))
        setattr(self, property, newValue)
        print(self.bookName+"'s "+property+" changed from "+oldValue
                +" to "+str(getattr(self, property)))

    def deleteBookCopy(self) -> None:
        self.isExists = False

    def getIssueStatus(self) -> bool:
        return self.isIssued