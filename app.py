# Import flask libraries
from flask import Flask, render_template, jsonify, request

# Create the flask app
app = Flask(__name__)


# Create homepage App route for the calculator
@app.route('/')
def index():
    return render_template('homepage.html')


# Send action on submit
@app.route('/send', methods=['POST'])
def send(sum=sum):
    if request.method == 'POST':
        num1 = request.form['num1']
        num2 = request.form['num2']
        operation = request.form['operation']

        if operation == 'add':
            sum = float(num1) + float(num2)
            return render_template('homepage.html', sum=sum)

        elif operation == 'subtract':
            sum = float(num1) - float(num2)
            return render_template('homepage.html', sum=sum)

        elif operation == 'multiply':
            sum = float(num1) * float(num2)
            return render_template('homepage.html', sum=sum)

        elif operation == 'divide':
            sum = float(num1) / float(num2)
            return render_template('homepage.html', sum=sum)
        else:
            return render_template('homepage.html')


if __name__ == ' __main__':
    app.debug = True
    app.run()