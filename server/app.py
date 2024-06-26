#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route("/print/<parameter>")
def print_parameter(parameter):
    print(parameter)
    return parameter

@app.route("/count/<int:parameter>")
def count_parameter(parameter):
    count = f""
    for i in range(parameter):
        count += f"{i}\n"
    return count

@app.route("/math/<int:parameter1>/<string:operation>/<int:parameter2>")
def math(operation, parameter1, parameter2):
    if operation == "+":
        answer = parameter1 + parameter2
    elif operation == "-":
        answer = parameter1 - parameter2
    elif operation == "*":
        answer = parameter1 * parameter2
    elif operation == "div":
        answer = parameter1 / parameter2
    elif operation == "%":
        answer = parameter1 % parameter2
    else:
        return None
    return str(answer)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
