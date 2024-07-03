import unittest
from app import app


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_api(self):
        response = self.app.post('/scrape')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
