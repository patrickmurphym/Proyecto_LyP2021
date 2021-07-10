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

driver = webdriver.Chrome(executable_path=("/usr/bin/chromedriver"), chrome_options=options)# argumentos para que funcione en wsl2,
#method para ir a una pagina web (todo lo de arriba lo pueden comentar si quieren ver la interfaz grafica)
driver.get("https://simple.ripley.cl/tecno/celulares?source=menu")
elem_nombre = driver.find_elements_by_class_name('catalog-product-details__name')
elem_precios = driver.find_elements_by_class_name('catalog-prices__list') # se selecciona la grilla que contiene los precios
telefonos = []

#ciclo for para crear el ojeto con nombre, luego se les asigna el precio correspondiente si este no lanza una exepcion
for i in range(len(elem_nombre)):
    nombre = elem_nombre[i].text
    Objeto_telefono = telefono.Telefono(nombre,"Na", "Na", "Na")
    telefonos.append(Objeto_telefono)
    try:
        precio_tienda = elem_precios[i].find_element_by_class_name("catalog-prices__list-price")
        telefonos[i].precio_tienda = precio_tienda.text
    except:
        pass

    try:
        precio_internet = elem_precios[i].find_element_by_class_name("catalog-prices__offer-price")
        telefonos[i].precio_internet = precio_internet.text
    except:
        pass
    try:
        precio_tarjeta = elem_precios[i].find_element_by_class_name("catalog-prices__card-price")
        telefonos[i].precio_tarjeta = precio_tarjeta.text
    except:
        pass
    
    print(telefonos[i].nombre)
    print(telefonos[i].precio_tienda)
    print(telefonos[i].precio_internet)
    print(telefonos[i].precio_tarjeta)
        
2

