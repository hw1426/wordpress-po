import sys
sys.path.append('.\page')
import unittest, time
from selenium import webdriver
from base_page import BasePage
from login_page import LoginPage
from edit_tag_page import CreateTag

class CreatTagCase(unittest.TestCase):
    def setUp(self):
        print('before test!')
        self.dr = webdriver.Chrome()
        self.domain = 'http://localhost/wordpress/'

    def test_creat_tag(self):
        #arrange
        username = password = 'admin'
        tag_name = 'tag%s' %(time.time())

        #action
        login_page = LoginPage(self.dr, self.domain + 'wp-login.php')
        login_page.login(username, password)

        edit_tag_page = CreateTag(self.dr, self.domain +'wp-admin/edit-tags.php')
        edit_tag_page.create_tag(tag_name)

        #assert
        table = edit_tag_page.tag_link().text
        self.assertIn(tag_name,table)

    def tearDown(self):
        print('after test!')
        self.dr.quit()

if __name__ == '__main__':
    unittest.main()



