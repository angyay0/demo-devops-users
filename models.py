class BaseRequest:
    def __init__(self):
        self.data = {}

    def setAttribute(self, key, value):
        self.data[key] = value
    
    def JSON(self):
        return self.data


class UserLoginRequest(BaseRequest):
    def __init__(self, password="", username=""):
        BaseRequest.__init__(self)
        self.data["username"] = username
        self.data["password"] = password

    
class SignupRequest(BaseRequest):
    def  __init__(self, username, password):
        BaseRequest.__init__(self)
        self.data["username"] = username
        self.data["password"] = password

class LoginResponse(BaseRequest):
    def __init__(self,token,name,username):
        BaseRequest.__init__(self)
        self.attachToken(token,name,username)
    
    def attachToken(self, token, name, username):
        self.data["token"] = token
        self.data["name"] = name
        self.data["username"] = token