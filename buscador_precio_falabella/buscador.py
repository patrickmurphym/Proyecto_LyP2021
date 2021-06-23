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
driver.get("https://www.paris.cl/iphone-12-pro-max-128gb-color-oro-486096999.html")

#elem es un objeto que contiene las propiedades de la clase llamada 'product-price'
elem = driver.find_element_by_xpath("//div[@id='testId-pod-prices-7183779'") #este es distinto para cada retail
precio = elem.text
print(precio)
print("esto no prendio cabros")

## preguntar por ayuda para encontrar el precio en falabella
