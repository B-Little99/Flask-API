from flask import Flask, jsonify

app = Flask(__name__)

usersList = ['Bob', 'Jim', 'John', 'Jimmy', 'James', ]

# Create, read, update, delete
'''
TDL:
gitignore
Base project - DONE
DB
    Set up model
    Auto add users script
Basic 
    Appropriate endpoints
        Specific employee
        Update acc bal
        All employees
        Register - checks for employee already
    Welcome/goodbye messages
    Password encryption
    Error messages
Testing
Docker
'''

# ------

@app.route('/helloworld', methods=['GET'])
def helloWorld():
    return 'Hello world!'

# ------
# add post method
@app.route('/users', methods=['GET'])
def users():
    return jsonify({'users': [user for user in usersList]})



