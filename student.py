from __future__ import annotations

from book import Book

from user import User
from login_system import LoginSystemInterface

class Student(User):
    allStudents = []
    def __init__(self, fullName, age, rollNo, credentials = LoginSystemInterface) -> None:
        super().__init__(fullName, age, credentials)
        self.rollno = rollNo
        self.myBooks = []
        self.isExists = True

    @staticmethod
    def findStudent(userName) -> tuple(bool, int):
        i = -1
        for student in Student.allStudents:
            i += 1
            if student.credentials.getUserName() == userName and student.isExists:
                return True, i
        return False, -1

    @staticmethod
    def addStudent(fullName, age, rollNo, credentials) -> Student:
        isStudentExists, _ = Student.findStudent(credentials.getUserName())
        if isStudentExists:
            print("Student already exists")
            return None
        newStudent = Student(fullName, age, rollNo, credentials)
        Student.allStudents.append(newStudent)
        print("Student added successfully.")
        return newStudent

    @staticmethod
    def readStudent(userName) -> None:
        isStudentExists, studentIndex = Student.findStudent(userName)
        if not isStudentExists:
            print("Student does not exist.")
            return
        student = Student.allStudents[studentIndex]
        print(f"""
        Name: {student.fullName}\n
        Username: {student.credentials.getUserName()}\n
        Age: {student.age}\n
        Roll No.: {student.rollNo}\n\n
        """)

    @staticmethod
    def updateStudent(userName, property, newValue) -> None:
        isStudentExists, studentIndex = Student.findStudent(userName)
        if not isStudentExists:
            print("Student does not exist.")
            return
        student = Student.allStudents[studentIndex]

        oldValue = str(getattr(student, property))
        setattr(student, property, newValue)
        print(student.fullName+"'s "+property+" changed from "+oldValue
                +" to "+str(getattr(student, property)))

    @staticmethod
    def deleteStudent(userName) -> None:
        isStudentExists, studentIndex = Student.findStudent(userName)
        if not isStudentExists:
            print("Student does not exist.")
            return
        Student.allStudents[studentIndex].isExists = False
        print("Student deleted successfully.")

    def findMyBookByName(self, bookName) -> tuple(bool, Book):
        for book in self.myBooks:
            if book.bookName == bookName:
                return True, book
        return False, None

    def requestBook(self, bookName, librarian) -> None:
        requestComplete, message, bookCopy = librarian.processIssueRequest(bookName)
        print(message)
        if not requestComplete: return
        self.myBooks.append(bookCopy)
    
    def returnBook(self, bookName, librarian) -> None:
        bookCopyFound, bookCopy = self.findMyBookByName(bookName)
        if not bookCopyFound:
            print('You do not possess this book.')
            return
        message = librarian.acceptBookReturn(bookCopy)
        print(message)