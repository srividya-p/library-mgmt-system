from __future__ import annotations

from uuid import uuid4
from datetime import date, timedelta
from book_copy import BookCopy

class Book:
    allBooks = []
    def __init__(self, bookId, bookName, authorName) -> None:
        self.bookId = bookId
        self.bookName = bookName
        self.authorName = authorName
        self.bookCopies = []
        self.isExists = True

    @staticmethod
    def findBookByName(bookName) -> tuple[bool, Book]:
        for book in Book.allBooks:
            if book.bookName == bookName and book.isExists:
                return True, book
        return False, None

    @staticmethod
    def findBooksByAuthorName(authorName) -> list[Book]:
        books = []
        for book in Book.allBooks:
            if book.authorName == authorName and book.isExists:
                books.append((book.bookName, authorName))
        return books

    def findBookCopyById(self, bookCopyId) -> tuple[bool, BookCopy]:
        for bookCopy in self.bookCopies:
            if bookCopy.copyId == bookCopyId and bookCopy.isExists:
                return True, bookCopy
        return False, None

    @staticmethod
    def addBook(bookName, authorName, ISBN, publicationYear, price) -> Book:
        bookFound, book = Book.findBookByName(bookName)
        if not bookFound:
            bookId = str(uuid4())
            newBook = Book(bookId, bookName, authorName)
            newBookCopy = BookCopy.createBookCopy(bookId, bookName, ISBN, publicationYear, price)
            newBook.bookCopies.append(newBookCopy)
            Book.allBooks.append(newBook)
            return newBook
        else:
            newBookCopy = BookCopy.createBookCopy(book.bookId, bookName, ISBN, publicationYear, price)
            book.bookCopies.append(newBookCopy)
            return book

    @staticmethod
    def displayBookDetails(bookName) -> None:
        bookFound, book = Book.findBookByName(bookName)
        if not bookFound:
            print('This book does not exist.')
            return
        
        print(f"""
        Book ID: {book.bookId}
        Book Name: {book.bookName}\n\n
        """)

        for bookCopy in book.bookCopies:
            bookCopy.displayBookCopy()

    @staticmethod
    def updateBookDetails(bookName, property, newValue) -> None:
        bookFound, book = Book.findBookByName(bookName)
        if not bookFound:
            print('This book does not exist.')
            return

        oldValue = str(getattr(book, property))
        setattr(book, property, newValue)
        print(book.bookName+"'s "+property+" changed from "+oldValue
                +" to "+str(getattr(book, property)))

    @staticmethod
    def updateBookCopyDetails(bookName, bookCopyId, property, newValue) -> None:
        bookFound, book = Book.findBookByName(bookName)
        if not bookFound:
            print('This book does not exist.')
            return

        bookCopyFound, bookCopy = book.findBookCopyById(bookCopyId)
        if not bookCopyFound:
            print('This book copy does not exist.')
            return

        bookCopy.updateBookCopy(property, newValue)

    @staticmethod
    def deleteBook(bookName) -> None:
        bookFound, book = Book.findBookByName(bookName)
        if not bookFound:
            print('This book does not exist.')
            return

        book.isExists = False

    @staticmethod
    def deleteBookCopy(bookName, bookCopyId) -> None:
        bookFound, book = Book.findBookByName(bookName)
        if not bookFound:
            print('This book does not exist.')
            return

        bookCopyFound, bookCopy = book.findBookCopyById(bookCopyId)
        if not bookCopyFound:
            print('This book copy does not exist.')
            return

        bookCopy.deleteBookCopy()

    def checkBookAvailablity(self, book) -> tuple[bool, BookCopy]:
        for bookCopy in book.bookCopies:
            if not bookCopy.getIssueStatus():
                return True, bookCopy
        return False, None
    
    @staticmethod
    def issueBook(bookName) -> tuple[bool, str, BookCopy]:
        bookFound, book = Book.findBookByName(bookName)
        if not bookFound:
            return False, 'This book does not exist.', None

        isAvailable, bookCopy = book.checkBookAvailablity(book)

        if not isAvailable:
            return False, 'This book is not available.', None

        bookCopy.issueDate = date.today()
        bookCopy.returnDate = date.today() + timedelta(7)
        bookCopy.isIssued = True
        return True, 'Issued successfully.', bookCopy

    @staticmethod
    def returnBook(bookCopy) -> None:
        bookCopy.issueDate = None
        bookCopy.returnDate = None
        bookCopy.isIssued = True

    @staticmethod
    def displayBooksByAuthor(authorName) -> None:
        books = Book.findBooksByAuthorName(authorName)
        if len(books) == 0:
            print('Author nor found.')
            return 
            
        for book, author in books:
            print(f"""
            Book Name: {book}\t
            Author: {author}
            """)