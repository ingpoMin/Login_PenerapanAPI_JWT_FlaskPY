from app import app
from app.controller import UserController
from flask import request

@app.route ('/')
def index():
    return "Hello World"

@app.route ("/users", methods = ["POST", "GET"])
def users():
    if request.method == "GET":
        return UserController.index()
    else:
        return UserController.store()

@app.route ("/users/<int:id>", methods = ["PUT", "DELETE", "GET"])
def usersDetail(id):
    if request.method == "GET":
        return UserController.show(id)
    elif request.method == "PUT":
        return UserController.update(id)
    elif request.method == "DELETE":
        return UserController.delete(id)
    
@app.route ("/login", methods = ["POST"])
def login():
    return UserController.login()