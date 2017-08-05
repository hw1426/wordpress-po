from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
DEFAULT_SECONDS = 5
class BasePage(object):
	url = None
	driver = None
	domain = None

	def __init__(self,driver,page_url=None):
		self.driver = driver
		self.domain = 'http://localhost/wordpress/'
		self.url = page_url
		if self.url != None:
			self.navigate()

	def title(self):
		return self.driver.get_title()

	def url(self):
		return self.url

	def navigate(self):
		self.driver.get(self.url)

	def by_id(self, the_id):
		locator = (By.ID, the_id)
		WebDriverWait(self.driver, DEFAULT_SECONDS).until(EC.visibility_of_element_located(locator))
		return self.driver.find_element_by_id(the_id)

	def by_name(self, the_name):
		return self.driver.find_element_by_name(the_name)

	def by_css(self, css):
		return self.driver.find_element_by_css_selector(css)

	def js(self, js_text):
		return self.driver.execute_script(js_text)



