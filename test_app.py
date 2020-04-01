from flask import Flask, jsonify
import unittest
from app import app

@pytest.fixture
def test_add(self):
    json, rv = self. '/add')
    self.assertTrue(json == 120)
    # tester = app.test_client(self)
    # response = tester.post(jsonify({"number_1": "100","number_2": "20"}))
    # self.assertEqual(response, 120)

if __name__ == '__main__':
    unittest.main()