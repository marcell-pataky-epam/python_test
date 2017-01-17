from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import unittest


class BasicTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('c:/programs/browserdrivers/chromedriver.exe')
        self.driver.get("http://automationpractice.com/")

    def test_Basic(self):
        search_field_id = 'search_query_top'
        search_button_css = '#searchbox > button'
        search_result_css = '#center_column > ul > li'
        search_text = 'T-shirt'

        search_input_element = self.driver.find_element_by_id(search_field_id)
        search_button = self.driver.find_element_by_css_selector(search_button_css)
        search_input_element.click()
        search_input_element.send_keys(search_text)
        search_button.click()

        self.assertTrue(WebDriverWait(self.driver, 30).until(
            lambda driver: driver.find_element_by_css_selector(search_result_css)), "Search result does not appear")

#    def tearDown(self):
#        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
