from abc import ABC, abstractclassmethod

class LoginSystemInterface(ABC):
    @abstractclassmethod
    def login(userName, password):
        pass

    @abstractclassmethod
    def logout():
        pass

#credential
class LoginSystem(LoginSystemInterface):
    def __init__(self, userName, password):
        self.userName = userName
        self.password = password
        self.loggedIn = False

    def login(self, userName, password):
        """Login method for all actors"""
        if self.userName != userName or self.password != password:
            print("Invalid credentials!")
            return
        
        self.loggedIn = True
        print('Logged in successfully.')

    def logout(self):
        """Logout method for all actors"""
        if not self.loggedIn:
            print("You are not logged in!")
            return
        self.loggedIn = False
        print('Logged out of account.')

    def isLoggedIn(self):
        return self.loggedIn

    def getUserName(self):
        return self.userName

    