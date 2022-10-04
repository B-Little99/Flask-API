from flask import Flask, jsonify, request

app = Flask(__name__)

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
        HTTP Codes/error messages
    Welcome/goodbye messages
    Password encryption
    Error messages
Testing
Docker
'''

usersList = ['Bob', 'Jim', 'John', 'Jimmy', 'James', ]

# ------

@app.route('/helloworld', methods=['GET'])
def helloWorld():
    return 'Hello world!'

# ------
@app.route('/employees', methods=['GET'])
def get_employees():
    return jsonify({'employees': [user for user in usersList]})

@app.route('/employees/<int:employeeID>', methods=['GET'])
def get_specific_employee(employeeID):
    employee = {'employee': usersList[employeeID]}
    context = request.args.get('context')

    if context == 'welcome':
        employee['contextMessage'] = f'Welcome {usersList[employeeID]}'
        return jsonify(employee)

    elif context == 'goodbye':
        employee['contextMessage'] = f'Goodbye {usersList[employeeID]}, have a good day.'
        return jsonify(employee)

    else:
        return jsonify(employee)

# ------
@app.route('/employees', methods=['POST'])
def create_employee(name, id, email, mobileNumber, pin):
    pass
    # check if exists in db, if not create args + accBal

# ------
@app.route('/employees/<int:employeeID>', methods=['PUT'])
def update_balance():
    pass
    # check if exists in db, if then update
    # queryParam acc bal

# ------
@app.route('/employees/<int:employeeID>', methods=['DELETE'])
def delete_employee():
    pass
    # check if exists in db, if then delete

