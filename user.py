from uuid import uuid4
from login_system import LoginSystemInterface 

class User:
    def __init__(self, fullName, age, authorizer = LoginSystemInterface):
        self.userId = str(uuid4())
        self.fullName = fullName
        self.age = age
        self.authorizer = authorizer
        self.isExists = True