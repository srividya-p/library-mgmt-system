from librarian import librarian
from user import User
from login_system import LoginSystemInterface

class Student(User):
    allStudents = []
    def __init__(self, fullName, age, rollNo, authorizer = LoginSystemInterface):
        super().__init__(fullName, age, authorizer)
        self.rollno = rollNo
        self.myBooks = []
        self.isExists = True

    @staticmethod
    def findStudent(userName):
        i = -1
        for student in Student.allStudents:
            i += 1
            if student.authorizer.getUsername() == userName and student.isExists:
                return True, i
        return False, "Student does not exist."

    @staticmethod
    def addStudent(fullName, age, rollNo, authorizer):
        isStudentExists, _ = Student.findStudent(authorizer.getUsername())
        if isStudentExists:
            print("Student already exists")
            return
        newStudent = Student(fullName, age, rollNo, authorizer)
        Student.allStudents.append(newStudent)
        print("Student added successfully.")

    @staticmethod
    def readStudent(userName):
        isStudentExists, studentIndex = Student.findStudent(userName)
        if not isStudentExists:
            print("Student does not exist.")
            return
        student = Student.allStudents[studentIndex]
        print(f"""
        Name: {student.fullName}\n
        Username: {student.authorizer.getUserName()}\n
        Age: {student.age}\n
        Roll No.: {student.rollNo}\n\n
        """)

    @staticmethod
    def updateStudent(userName, property, newValue):
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
    def deleteStudent(userName):
        isStudentExists, studentIndex = Student.findStudent(userName)
        if not isStudentExists:
            print("Student does not exist.")
            return
        Student.allStudents[studentIndex].isExists = False
        print("Student deleted successfully.")

    def findMyBookByName(self, bookName):
        for book in self.myBooks:
            if book.bookName == bookName:
                return True, book
        return False, None

    def requestBook(self, bookName):
        requestComplete, returnValue = librarian.processIssueRequest(bookName)
        if not requestComplete:
            print(returnValue)
            return
        self.myBooks.append(returnValue)
        print('Book issued successfully.')
        return True
    
    def returnBook(self, bookName):
        returnComplete, message = librarian.acceptBookReturn(bookName)
        if not returnComplete:
            print(message)
            return

        print('Book returned successfully.')