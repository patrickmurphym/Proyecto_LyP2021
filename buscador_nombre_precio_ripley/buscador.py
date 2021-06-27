from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options 

'''estas son opciones de como se abrira chroma'''
options = webdriver.ChromeOptions()
options.add_argument("--headless")  #esta es la opcion que hace que no haya UI
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.add_argument("--no-sandbox")
options.add_argument("--disable-setuid-sandbox")

driver = webdriver.Chrome(executable_path=("/usr/bin/chromedriver"), chrome_options=options)# argumentos para que funcione en wsl2
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()

# import os  
# from selenium import webdriver  
# from selenium.webdriver.common.keys import Keys  
# from selenium.webdriver.chrome.options import Options  

 
# options = webdriver.ChromeOptions()
# options.add_argument("--headless")  
# options.add_argument('--ignore-certificate-errors')
# options.add_argument("--test-type")
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-setuid-sandbox")
# driver = webdriver.Chrome(executable_path=("/usr/bin/chromedriver"),   chrome_options=options)
# driver.get('https://google.com')
# print(driver.title)
# driver.quit()
