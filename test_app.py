# tests/test_app.py
import unittest
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'Hello, CI/CD with Docker!')

    def test_health_check(self):
        response = self.app.get('/health')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'OK')

    def test_fail_case(self):
        response = self.app.get('/wrong-endpoint')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
