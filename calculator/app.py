# app.py

from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('calculator.html')

@app.route('/scientific_calculator', methods=['GET', 'POST'])
def scientific_calculator():
    result = None

    if request.method == 'POST':
        num1 = float(request.form['num1'])
        operation = request.form['operation']

        if operation == 'sqrt':
            result = math.sqrt(num1)
        elif operation == 'log':
            result = math.log10(num1)
        elif operation == 'sin':
            result = math.sin(math.radians(num1))
        elif operation == 'cos':
            result = math.cos(math.radians(num1))
        elif operation == 'tan':
            result = math.tan(math.radians(num1))

    return render_template('scientific_calculator.html', result=result)

@app.route('/cal', methods=['POST'])
def calculate():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    operation = request.form['operation']
    result = None

    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'Module':
        result = num1 % num2
    elif operation == 'power':
        result = num1 ** num2
    elif operation == 'divide':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error: Cannot divide by zero."

    return render_template("calculator.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
