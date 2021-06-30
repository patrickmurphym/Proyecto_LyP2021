from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options 
import telefono

'''estas son opciones de como se abrira chroma'''
options = webdriver.ChromeOptions()
options.add_argument("--headless")  #esta es la opcion que hace que no haya UI
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.add_argument("--no-sandbox")
options.add_argument("--disable-setuid-sandbox")

driver = webdriver.Chrome(executable_path=("/usr/bin/chromedriver"), chrome_options=options)# argumentos para que funcione en wsl2
#method para ir a una pagina web
driver.get("https://www.paris.cl/tecnologia/celulares/smartphone/")
elem_nombre = driver.find_elements_by_class_name('ellipsis_text')
elem_precios = driver.find_elements_by_class_name('price')
telefonos = []
for i in range(len(elem_nombre)):
    nombre = elem_nombre[i].text
    Objeto_telefono = telefono.Telefono(nombre,"Na", "Na", "Na")
    telefonos.append(Objeto_telefono)
    ##### de aqui para abajo no esta funcionando bien
    try:
        precio_tienda = elem_precios[i].find_element_by_class_name("item-price price-normal")
        telefonos[i].precio_tienda = precio_tienda.text
    except:
        pass

    try:
        precio_internet = elem_precios[i].find_element_by_class_name("price-label-short")
        telefonos[i].precio_internet = precio_internet.text
    except:
        pass
    try:
        precio_tarjeta = elem_precios[i].find_element_by_class_name("col-md-9 col-xs-9 item-price offer-price price-tc cencosud-price")
        telefonos[i].precio_tarjeta = precio_tarjeta.text
    except:
        pass
    print(telefonos[i].nombre)
    print(telefonos[i].precio_tienda)
    print(telefonos[i].precio_internet)
    print(telefonos[i].precio_tarjeta)
    print("----------------------------------")

    
#elem es un objeto que contiene las propiedades de la clase llamada 'product-price'
# elem = driver.find_element_by_xpath("//div[@id='testId-pod-prices-7183779'") #este es distinto para cada retail
# precio = elem.text
# print(precio)
# print("esto no prendio cabros")

## preguntar por ayuda para encontrar el precio en falabella
driver.close()
