from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options 

'''estas son opciones de como se abrira chrome'''
options = webdriver.ChromeOptions()
options.add_argument("--headless")  #esta es la opcion que hace que no haya UI
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.add_argument("--no-sandbox")
options.add_argument("--disable-setuid-sandbox")

driver = webdriver.Chrome(executable_path=("/usr/bin/chromedriver"), chrome_options=options)# argumentos para que funcione en wsl2
#method para ir a una pagina web
driver.get("https://simple.ripley.cl/tecno/celulares?source=menu")

#elem es un objeto(WebElement) que contiene las propiedades de la clase llamada 'product-price'(como .text)
for i in range(0,46):
    elem = driver.find_elements_by_class_name('catalog-product-details__name')
    nombre = elem[i].text
    print(nombre)
    elem = driver.find_elements_by_class_name('catalog-prices__offer-price')
    precio = elem[i].text
    print(precio)
driver.close()
