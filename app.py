# Import flask libraries
from flask import Flask, jsonify, request

# Create the flask app
app = Flask(__name__)
# Logger.error, check for flask error, flask info


# function to validate the input
def inp_validation(data):
    app.logger.info("inside Input Validation")

    # Error 1: Check if the keys are correct expected number_1 and number_2
    if not ("number_1" in data and "number_2" in data):
        error = "Invalid input: Expected {\"number_1\": \"number\", \"number_2\": \"number\"}"
        raise TypeError(error)

    # Error 2: Ensure that the values are not empty
    if data.get("number_1") == '' or data.get("number_2") == '':
        error = "Invalid input: Expected {\"number_1\": \"number\", \"number_2\": \"number\"}"
        raise TypeError(error)

    # convert the input data to float, any non-numerical data caught in the general exception
    app.logger.info("String to float conversion")
    num1 = float(data.get("number_1"))
    num2 = float(data.get("number_2"))
    # app.logger.info(num1, num2)

    # return validated and converted data back
    return num1, num2


# route for using Json
@app.route('/add', methods=['POST'])
def add():
    try:
        app.logger.info("Calling add")
        # Request data in Json format, any JSON formatting issues caught by general Exception
        req = request.get_json()

        # Send values for validation
        num1, num2 = inp_validation(req)

        # perform operations on validated data
        add = num1 + num2
        app.logger.info(add)

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
    try:
        app.logger.info("Calling subtract")
        # Request data in Json format, any JSON formatting issues caught by general Exception
        req = request.get_json()

        # Send values for validation
        num1, num2 = inp_validation(req)

        # perform operations on validated data
        print(num1, num2)
        subtract = num1 - num2
        app.logger.info(subtract)

        return jsonify({"result": subtract}), 200

    except TypeError as e:
        app.logger.error(str(e))
        return jsonify({"error": str(e)}), 400

    except ValueError as e:
        app.logger.error(str(e))
        return jsonify({"error": str(e)}), 400

    except Exception as e:
        app.logger.error(e)
        return jsonify({"error": str(e)}), 400


@app.route('/multiply', methods=['POST'])
def multiply():
    try:
        app.logger.info("Calling multiply")
        # Request data in Json format, any JSON formatting issues caught by general Exception
        req = request.get_json()

        # Send values for validation
        num1, num2 = inp_validation(req)

        # perform operations on validated data
        multiply = num1 * num2
        app.logger.info(multiply)

        return jsonify({"result": multiply}), 200

    except TypeError as e:
        app.logger.error(str(e))
        return jsonify({"error": str(e)}), 400

    except ValueError as e:
        app.logger.error(str(e))
        return jsonify({"error": str(e)}), 400

    except Exception as e:
        app.logger.error(e)
        return jsonify({"error": str(e)}), 400


@app.route('/divide', methods=['POST'])
def divide():
    try:
        app.logger.info("Calling divide")
        # Request data in Json format, any JSON formatting issues caught by general Exception
        req = request.get_json()

        # Send values for validation
        num1, num2 = inp_validation(req)

        # perform operations on validated data
        divide = num1 / num2
        app.logger.info(divide)

        return jsonify({"result": divide}), 200

    except TypeError as e:
        app.logger.error(str(e))
        return jsonify({"error": str(e)}), 400

    except ValueError as e:
        app.logger.error(str(e))
        return jsonify({"error": str(e)}), 400

    except Exception as e:
        app.logger.error(e)
        return jsonify({"error": str(e)}), 400


if __name__ == ' __main__':
    app.debug = True
    app.run()