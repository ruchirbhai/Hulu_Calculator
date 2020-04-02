# Video QE Coding Challenge: Calculator Service

 This is a coding exercise that entails writing a small microservice along with tests to exercise that microservice.

## Demo
Here is a working demo:  https://github.com/ruchirbhai/Hulu_Calculator

## Business Logic
The microservice should provide an API capable of basic math functions
limited to: addition, subtraction, multiplication and division.

### JSON Payload Structure

{
“number_1”: 1,
“number_2”: 2 }


### Successful Response
A successful response should return JSON with a “result” field containing the numeric value

### Error Response
An error response should return JSON with an “error” field which explains the error.

### Project Structure
- source code located @ /Hulu_Calculator/app.py
- pytest code located @ /Hulu_Calculator/tests/test_api.py
- project requirements@ /Hulu_Calculator/requirements.txt

## Project Setup and Execution

### Project Setup
- Download the code from  https://github.com/ruchirbhai/Hulu_Calculator
- Install all the requirements as per the requirements.txt

### Code Execution

- cd into the Hulu_Calculator directory
- To run the Flask app in production mode use the command "FLASK_APP=app.py flask run"
- The server will run on http://127.0.0.1:5000/ or http://localhost:5000/
- To run the Flask app in debug mode use the following command "FLASK_APP=app.py FLASK_DEBUG=true flask run"
- Sample Output<br />
 \* Serving Flask app "app.py"<br />
 \* Environment: production<br />
   WARNING: This is a development server. Do not use it in a production deployment.<br />
   Use a production WSGI server instead.<br />
 \* Debug mode: off<br />
 \* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)<br />

### Test Execution
 - To run the all the from the /Hulu_Calculator directory run "pytest" from terminal
 - To look at the test cases go to file @ /Hulu_Calculator/tests/test_api.py
 - Sample Output<br />
================================= test session starts =================================<br />
platform darwin -- Python 3.8.1, pytest-5.4.1, py-1.8.1, pluggy-0.13.1<br />
rootdir: /Users/ruchir/Documents/Hulu_Calculator<br />
plugins: flask-1.0.0<br />
collected 4 items<br />
tests/test_api.py ....                                                          [100%]<br />
================================== 4 passed in 0.05s ==================================<br />