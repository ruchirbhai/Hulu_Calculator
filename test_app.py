import unittest
import app

class TestApp(unittest.TestCase):

    def test_add(self):
        result = app.add(100, 20)
        self.assertEqual(result, 120)

if __name__ == '__main__':
    unittest.main()