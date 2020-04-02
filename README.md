# Video QE Coding Challenge: Calculator Service

 This is a coding exercise that entails writing a small microservice along with tests to exercise that microservice.

## Demo
Here is a working demo hosted on GCP app engine: https://hulucalc.wl.r.appspot.com/<operations>
operations available: /add, /substract, /multiply, /divide

Github Code: https://github.com/ruchirbhai/Hulu_Calculator

## Business Logic
The microservice should provide an API capable of basic math functions
limited to: addition, subtraction, multiplication and division.

### Expected JSON Payload Structure

```
{
    “number_1”: 1,
    “number_2”: 2
}
```



### Successful Response
A successful response should return JSON with a “result” field containing the numeric value
```json
{"result": 1.0}
```
### Error Response
An error response should return JSON with an “error” field which explains the error.

### Project Structure
- source code located @ /Hulu_Calculator/main.py
- pytest code located @ /Hulu_Calculator/tests/test_api.py
- project requirements@ /Hulu_Calculator/requirements.txt
- flask configuration @ /Hulu_Calculator/config.py
- App engine config   @ /Hulu_Calculator/app.yaml

## Project Setup and Execution

### Project Setup
- Clone the code from  https://github.com/ruchirbhai/Hulu_Calculator
- Install all the requirements as per the requirements.txt

    ```text
    $ git clone https://github.com/ruchirbhai/Hulu_Calculator
    $ python3 -m venv hulu_calc
    $ source hulu_calc/bin/activate
    $ pip install -r requirements.txt

    ```

### Code Execution

- cd into the Hulu_Calculator directory
- To run the Flask app in development mode use the command
``
$ FLASK_APP=main.py FLASK_DEBUG=true flask run"
``

- The server will run on `http://127.0.0.1:5000/` or `http://localhost:5000/`
- To run the Flask app in production mode use the following command, add the env variable `FLASK_CONFIGURATION`
    ```
    $ export FLASK_CONFIGURATION=production
    $ FLASK_APP=main.py flask run"
    ```

### Test Execution
 - To run the all the from the /Hulu_Calculator directory run "pytest" from terminal

    `$ pytest`
 - To look at the test cases go to file @ /Hulu_Calculator/tests/test_api.py
 - Sample Output<br />
     ```text


    ================================= test session starts =================================<br />
    platform darwin -- Python 3.8.1, pytest-5.4.1, py-1.8.1, pluggy-0.13.1<br />
    rootdir: /Users/ruchir/Documents/Hulu_Calculator<br />
    plugins: flask-1.0.0<br />
    collected 4 items<br />
    tests/test_api.py ....                                                          [100%]<br />
    ================================== 4 passed in 0.05s ==================================<br />
    ```

