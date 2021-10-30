from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#
# service = Service('/usr/local/bin/chromedriver')
# browser = webdriver.Chrome(service=service)
# browser.get('http://localhost:8000')
#
# assert 'successfully' in browser.title
import unittest


class NewVisitorTest(unittest.TestCase):
    # start test
    def setUp(self):
        service = Service('/usr/local/bin/chromedriver')
        self.browser = webdriver.Chrome(service=service)
        self.browser.implicitly_wait(3)  # 암묵적 대기

    # end test
    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')

        self.assertIn('To-Do', self.browser.title)
        self.fail("finish test")


if __name__ == '__main__':
    unittest.main(warnings='ignore')
