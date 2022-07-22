from uuid import uuid4
from login_system import LoginSystemInterface 

class User:
    def __init__(self, fullName, age, credentials = LoginSystemInterface) -> None:
        self.userId = str(uuid4())
        self.fullName = fullName
        self.age = age
        self.credentials = credentials