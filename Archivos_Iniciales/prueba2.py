import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get(
            "https://www.paris.cl/iphone-12-pro-max-128gb-color-oro-486096999.html")
        #self.assertIn("Python", driver.title)

        elem = driver.find_element_by_class_name('item-price')
        precio = elem.text
        print(precio.split('\n'))
        # elem = driver.find_element_by_name("q")
        # elem.send_keys("Almacenes Paris")
        # elem.send_keys(Keys.RETURN)
        # assert "No results found." not in driver.page_source

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
