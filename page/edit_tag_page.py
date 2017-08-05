from base_page import BasePage
import time

class CreateTag(BasePage):
    @property
    def tag_text_field(self):
        return self.by_id('tag-name')

    @property
    def submit_btn(self):
        return self.by_id('submit')

    def create_tag(self,tag_name):
        self.tag_text_field.send_keys(tag_name)
        time.sleep(1)
        self.submit_btn.submit()

    def tag_link(self):
        return self.by_css('#the-list')
