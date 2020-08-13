from userapi import app
from userapi.dbhandler import DBHandler
from flask import request
from flask import jsonify

#Object for managing Database Operations
handler = DBHandler()
handler.connect()

'''
This method handle a simple login request
with username and password
TODO: Validations at V1.2
'''
@app.route('/login', methods=["POST"])
def authenticate():
    if request.method == "POST":
        data = request.get_json()
        if data:
            result = handler.hasAccess(data)
            return jsonify(result.JSON())
        else:
            abort(403)
    abort(404)

'''
This method handle a simple signup request
with name, email, username and password
TODO: Validations at V1.2
'''
@app.route('/signup', methods=["POST"])
def signup():
    if request.method == "POST":
        data = request.data
        if data:
            result = handler.storeUser(data)
            return jsonify(result.JSON())
        else:
            abort(403)
    abort(404)