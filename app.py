# Import flask libraries
from flask import Flask, render_template, jsonify, request

# Create the flask app
app = Flask(__name__)


# function to sanitize the input
def inp_sanitize(num1, num2):
    # Error 2: for an empty input get ValueError: could not convert string to float:
    print(num1, num2)
    # if num1 or num2 == '':
    #     error = jsonify({"error2": "Data empty"})
    #     print (error)
    #     return error
    return num1, num2


# Create homepage App route for the calculator
# Modify the homepage to show success or error
@app.route('/')
def hello():
    return 'hello world'


# route for using Json
@app.route('/add', methods=['POST'])
def add():
    # add this to try catch,
    try:
        if request.is_json:
            req = request.get_json()
            num1 = float(req.get("number_1"))
            num2 = float(req.get("number_2"))
            print("hello")
            num1, num2 = inp_sanitize(num1, num2)
            #improvement remove add and print statements+
            print(num1, num2)
            add = num1 + num2
            print(add)
            res = jsonify(add)

            return res, 200
        else:
            res = jsonify({"error1": "Data is not is JSON format"})
            return res, 400
    except:
        error = " This error"
        return error, 400

@app.route('/subtract', methods=['POST'])
def subtract():
    # add this to try catch,
    if request.is_json:
        req = request.get_json()
        num1 = float(req.get("number_1"))
        num2 = float(req.get("number_2"))

        add = num1 - num2
        res = jsonify(add)

        return res, 200
    else:
        res = jsonify({"error": "No data recieved"})
        return res, 400

@app.route('/multiply', methods=['POST'])
def multiply():
    # add this to try catch,
    # Error 1: for an empty input get ValueError: could not convert string to float:
    # Error 2: check if input in json format
    if request.is_json:
        req = request.get_json()
        num1 = float(req.get("number_1"))
        num2 = float(req.get("number_2"))

        add = num1 * num2
        res = jsonify(add)

        return res, 200
    else:
        res = jsonify({"error": "No data recieved"})
        return res, 400

@app.route('/divide', methods=['POST'])
def divide():
    # add this to try catch,
    # Error 1: divide by zero
    if request.is_json:
        req = request.get_json()
        num1 = float(req.get("number_1"))
        num2 = float(req.get("number_2"))

        if num2 == 0:
            raise ValueError("Cannot divide by Zero!")
        add = num1 / num2
        res = jsonify(add)

        return res, 200
    else:
        res = jsonify({"error": "No data recieved"})
        return res, 400


if __name__ == ' __main__':
    app.debug = True
    app.run()