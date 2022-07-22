from librarian import Librarian
from user import User
from login_system import LoginSystemInterface

class Student(User):

    allStudents = []

    def init(self, fullName, age, rollNo, authorizer = LoginSystemInterface):
        super().__init__(fullName, age, authorizer)
        self.rollno = rollNo
        self.myBooks = []
 
    #NEEDS FIXING
    def requestBook(self, bookName, librarianName):
        isBookIssued, bookObject = Librarian.processIssueRequest(bookName)
        if not isBookIssued:
            return False
        self.myBooks.append(bookObject)
        return True
    
    #NEEDS FIXING
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
                return True, book
        return False, None

    @staticmethod
    def findStudent(userName):
        i = -1
        for student in Student.allStudents:
            i += 1
            if student.authorizer.getUsername() == userName:
                return True, i
        return False, "Student does not exist."

    @staticmethod
    def addStudent(name, age, authorizer):
        isStudentExists, _ = Student.findStudent(authorizer.getUsername())
        if isStudentExists:
            return False, "Student already exists"
        newStudent = Student(name, age, authorizer)
        Student.all.append(newStudent)
        return True, "Student added successfully"

    @staticmethod
    def readStudent(authorizer, property):
        isStudentExists, studentIndex = Student.findStudent(authorizer.getUsername())
        if not isStudentExists:
            return False, "Student does not exists"
        returnvalue = getattr(Student.allStudent[studentIndex], property)
        return True, returnvalue

    @staticmethod
    def updateStudent(authorizer, property, newValue):
        isStudentExists, studentIndex = Student.findStudent(authorizer.getUsername())
        if not isStudentExists:
            return False, "Student does not exists"
        setattr(Student.allStudent[studentIndex], property, newValue)
        return True, "Student updated successfully"

    @staticmethod
    def deleteStudent(authorizer):
        isStudentExists, studentIndex = Student.findStudent(authorizer.getUsername())
        if not isStudentExists:
            return False, "Student does not exists"
        Student.allStudent[studentIndex].isExist = False
        return True, "Student deleted successfully"