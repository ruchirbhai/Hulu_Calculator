# from flask import Flask, jsonify
# import pytest
# from app import app
#
# def test_hello():
#     response = app.test_client().get('/')
#     print(response)
#     assert response.data == b'hello world'
#
# def test_add():
#     response = app.test_client().get('/add')
#     print(response)
#     assert response.data == b'120.0'
# # import requests
# #
# # url = 'http://127.0.0.1:5000'
# #
# # @pytest.fixture
# # def test_add():
# #     r = requests.post(url+'/add')
# #     print(r)
# #     #assert(json == 120)
# #     data = r.json()
# #     assert data == 120
# #     # tester = app.test_client(self)
# #     # response = tester.post(jsonify({"number_1": "100","number_2": "20"}))
# #     # self.assertEqual(response, 120)
# #
# # # if __name__ == '__main__':
# # #     #unittest.main()