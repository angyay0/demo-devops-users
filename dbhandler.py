from userapi.models import LoginResponse
import psycopg2
import json

#Load and return json as dict
def ReadFromJson():
    with open("db.json") as file:
        return (json.load(file))

#Database operations to retrieve and save users
class DBHandler:
    def __init__(self):
        self.credentials = ReadFromJson()
        self.connection = None
    
    def connect(self):
        try:
            #Connect
            return True
        except:
            return False
    
    def hasAccess(self, data):
        try:
            print (data)
            return LoginResponse("Valid-Token","Angel","angyay0")
        except:
            return LoginResponse("","","")
    
    def storeUser(self, data):
        try:
            print (data)
            #return ("Fallo interno", False)
            return LoginResponse("Valid-Token","Angel","angyay0")
        except:
            return LoginResponse("","","")