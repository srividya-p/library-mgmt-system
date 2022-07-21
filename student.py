
from librarian import Librarian
from user import User

class Student(User):

    allStudents = []

    def init(self, Rollno):
        self.rollno = Rollno
        self.myBooks = []

        
    def requestBook(self, bookName):
        isBookIssued, bookObject = Librarian.processIssueRequest(bookName)
        if not isBookIssued:
            return False
        self.myBooks.append(bookObject)
        return True

    def returnBook(self,bookName):
        isBookIssued, bookObject = Librarian.acceptBookReturn(bookName)
        if not isBookIssued:
            return False
        bookObject = self.findMyBook
        self.myBooks.remove(bookObject)
        return True
        

    def findMyBookByName(self, bookName):
        myBooks = []
        for book in self.MyBooks:
            if book.bookName == bookName:
                return book


    @staticmethod
    def addStudent(name, age, authorizer):
        isStudentExists, studentIndex = Librarian.isLibrarianExists(authorizer.getUsername())
        if isStudentExists:
            return False, "Student already exists"
        newStudent = Student(name, age, authorizer)
        Student.all.append(newStudent)
            return True, "Student added successfully"

    @staticmethod
    def readStudent(authorizer, property):
        isStudentExists, studentIndex = Student.isStudentExists(authorizer.getUsername())
        if not isStudentExists:
            return False, "Student does not exists"
        returnvalue = getattr(Student.allStudent[studentIndex], property)
            return True, returnvalue


    @staticmethod
    def updateStudent(authorizer, property, newValue):
        isStudentExists, studentIndex = Student.StudentExists(authorizer.getUsername())
        if not isStudentExists:
            return False, "Student does not exists"
        setattr(Student.allStudent[StudentIndex], property, newValue)
            return True, "Student updated successfully"



    @staticmethod
    def deleteStudent(authorizer):
        isStudentExists, studentIndex = Student.isStudentExists(authorizer.getUsername())
        if not isStudentExists:
            return False, "Student does not exists"
        Student.allStudent[StudentIndex].isExist = False
            return True, "Student deleted successfully"

    

    








        
