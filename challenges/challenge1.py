import unittest
from selenium import webdriver

class Challenge1(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")

    def tearDown(self):
        self.driver.close()

    def test_challenge1(self):
        self.driver.get("https://www.google.com")
        self.assertIn("Google", self.driver.title)

    def test_challenge2(self):
        self.driver.get("https://amazon.com")
        self.assertIn("Amazon.com", self.driver.title)

    def test_challenge3(self):
        self.driver.get("https://yahoo.com")
        self.assertIn("Yahoo", self.driver.title)

    def test_challenge4(self):
        self.driver.get("https://workfront.com/solutions")
        self.assertIn("Work Management Solutions For Your Team | Workfront", self.driver.title)

if __name__ == '__main__':
    unittest.main()