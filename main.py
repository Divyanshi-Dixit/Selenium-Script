import unittest
from selenium import webdriver
import page 

class PythnOrgSeacrh(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
		self.driver.get("http://www.python.org")

	def test_title_match(self):
		mainpage = page.MainPage()
		assert mainpage.is_title_matches()


	def tearDown(self):
		self.driver.close()


if __name__ == "__main__" : 
	unittest.main()