from selenium import webdriver
from selenium.webdriver.common.keys import Keys




precios = {}

driver = webdriver.Chrome()

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--test-type')
options.add_argument('--no-sandbox')
options.add_argument('--disable-setuid-sandbox')

# driver.get("https://www.paris.cl")
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("iphone 12")
# elem.send_keys(Keys.RETURN)


driver.get("https://simple.ripley.cl/tecno/celulares?source=menu")
catalogo = driver.find_element_by_class_name('catalog-container')
celulares = catalogo.find_elements_by_class_name('catalog-product-item').find_elements_by_class_name('')

print(celulares)


# driver.get("https://www.paris.cl/iphone-12-pro-max-128gb-color-oro-486096999.html")
# elem = driver.find_element_by_css_selector('div.item-price')
# precios["Paris"] = elem.text

# elem.clear()


# driver.get("https://www.falabella.com/falabella-cl/product/prod24342599/Apple-iPhone-12-Pro-128GB/14686791")
# elem = driver.find_element_by_css_selector('span.copy12.primary.jsx-3736277290.normal')
# precios["Falabella"] = elem.text

# print(precios)
driver.close()