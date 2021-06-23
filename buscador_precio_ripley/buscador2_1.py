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
#method para ir a una pagina web
driver.get("https://simple.ripley.cl/tecno/celulares?source=menu")

#elem es un objeto que contiene las propiedades de la clase llamada 'product-price'
elem = driver.find_element_by_class_name('catalog-container')
precio = elem.text
print(precio)
