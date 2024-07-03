import unittest
from scraper.scraper import scrape_public_register


class TestScraper(unittest.TestCase):
    def test_scrape_data(self):
        payload = {'lastName': 'test', 'firstName': 'John'}
        data = scrape_public_register(payload)
        self.assertIsInstance(data, list)
        self.assertTrue(all(isinstance(item, dict) for item in data))


if __name__ == '__main__':
    unittest.main()
