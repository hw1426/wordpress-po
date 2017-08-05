import sys
sys.path.append('.\page')
import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from login_page import LoginPage
from dashboard_page import DashboardPage
import time

class LoginCase(unittest.TestCase):
	def setUp(self):	
		print ('before test')
		self.domain = 'http://localhost/wordpress/'
		self.driver = webdriver.Chrome()

	def test_login_success(self):
		#arrange
		username = password = 'admin'
		#action
		login_page = LoginPage(self.driver, self.domain +'wp-login.php')
		dashboard_page = login_page.login(username, password)
        #assert
		self.assertTrue('wp-admin' in self.driver.current_url)
		self.assertTrue(username in dashboard_page.greeting_link.text)

	def tearDown(self):
		print('after every test!')
		self.driver.quit()

if __name__ == '__main__':
	unittest.main()