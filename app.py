# Import flask libraries
from flask import Flask, jsonify, request

# Create the flask app
app = Flask(__name__)
# Logger.error, check for flask error, flask info


# function to validate the input
def inp_validation(data):
    app.logger.error("inside Input Validation")

    # Error 1: Check if the keys are correct expected number_1 and number_2
    if not ("number_1" in data and "number_2" in data):
        error = "Invalid input: Expected {\"number_1\": \"number\", \"number_2\": \"number\"}"
        raise TypeError(error)

    # Error 2: Ensure that the values are not empty
    if data.get("number_1") == '' or data.get("number_2") == '':
        error = "Invalid input: Expected {\"number_1\": \"number\", \"number_2\": \"number\"}"
        raise TypeError(error)

    # convert the input data to float, any non-numerical data caught in the general exception
    num1 = float(data.get("number_1"))
    num2 = float(data.get("number_2"))
    app.logger.error(num1, num2)

    # return validated and converted data back
    return num1, num2


# route for using Json
@app.route('/add', methods=['POST'])
def add():
    try:
        app.logger.error("Calling add")
        # Request data in Json format, any JSON formatting issues caught by general Exception
        req = request.get_json()

        # Send values for validation
        num1, num2 = inp_validation(req)

        # perform operations on validated data
        add = num1 + num2
        app.logger.error(add)

        return jsonify({"result": add}), 200

    except TypeError as e:
        app.logger.error(str(e))
        return jsonify({"error": str(e)}), 400

    except ValueError as e:
        app.logger.error(str(e))
        return jsonify({"error": str(e)}), 400

    except Exception as e:
        app.logger.error(e)
        return jsonify({"error": str(e)}), 400


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