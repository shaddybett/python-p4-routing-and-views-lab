#!/usr/bin/env python3

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index ():
    title = "Python Operations with Flask Routing and Views"
    return render_template('index.html', title=title)

@app.route('/print/<string>')
def count(num):
    numbers = '\n'.join(str(i) for i in range(num + 1))
    return f'<pre>{numbers}</pre>'

@app.route('/math/<float:num1><operation><float:num2>')
def math(num1,operation,num2):
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-': 
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    elif operation == '%':
        result = num1 % num2
    else:
        return "Error: Invalid operation."

    return f"<h1>Result: {result}</h1>"

if __name__ == '__main__':
    app.run(debug=True)           
