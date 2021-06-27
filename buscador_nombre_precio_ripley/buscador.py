from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import telefono

'''estas son opciones de como se abrira chrome'''
options = webdriver.ChromeOptions()
options.add_argument("--headless")  #esta es la opcion que hace que no haya UI
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.add_argument("--no-sandbox")
options.add_argument("--disable-setuid-sandbox")

#driver = webdriver.Chrome(executable_path=("/usr/bin/chromedriver"), chrome_options=options)# argumentos para que funcione en wsl2,
#method para ir a una pagina web (todo lo de arriba lo pueden comentar si quieren ver la interfaz grafica)
driver.get("https://simple.ripley.cl/tecno/celulares?source=menu")
elem = driver.find_elements_by_class_name('catalog-product-details__name')

telefonos = []
#elem es un objeto(WebElement) que contiene las propiedades de la clase llamada 'product-price'(como .text)
for i in range(0,len(elem)):
    elem_nombre = driver.find_elements_by_class_name('catalog-product-details__name')
    elem_precio = driver.find_elements_by_class_name('catalog-prices__offer-price')
    nombre = elem_nombre[i].text
    precio = elem_precio[i].text
    info_telefono = telefono.Telefono(nombre,precio)
    telefonos.append(info_telefono)
    # print(telefono[i].nombre)  
    # telefono[i].precio = elem_precio[i].text
    # telefonos.append(telefono[i].precio)
    # print(telefono[i].precio)
for i in range(len(telefonos)):
    print(telefonos[i].nombre)
    print(telefonos[i].precio)
driver.close()

