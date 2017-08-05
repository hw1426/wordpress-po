import sys
sys.path.append('.\page')
import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from login_page import LoginPage
from create_edit_page import CreateEditPage
from post_list_page import PostListPage 

class CreatCase(unittest.TestCase):
	def setUp(self):
		print('before test!')
		self.dr = webdriver.Chrome()
		self.domain = 'http://localhost/wordpress/'

	def test_create_post(self):
		#arrange
		username = password = 'admin'
		title = '测试 %s'%(str(time.time()))
		content = 'test_body'

		#action
		login_page = LoginPage(self.dr, self.domain+'wp-login.php')
		login_page.login(username, password)

		create_post_page = CreateEditPage(self.dr, self.domain+'wp-admin/post-new.php')
		create_post_page.create_post(title, content)
		
		#assert
		post_list_page = PostListPage(self.dr, self.domain+'wp-admin/edit.php')
		self.assertEqual(title, post_list_page.first_post.text)


	def tearDown(self):
		print('after test!')
		self.dr.quit()

if __name__ == '__main__':
	unittest.main()
