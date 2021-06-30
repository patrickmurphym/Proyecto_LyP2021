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
elem_precios = driver.find_elements_by_class_name('catalog-prices__list')
telefonos = []
for i in range(len(elem_nombre)):
    nombre = elem_nombre[i].text
    nombre_telefono = telefono.Telefono(nombre,"Na", "Na", "Na")
    telefonos.append(nombre_telefono)
    try:
        precio_tienda = elem_precios[i].find_element_by_class_name("catalog-prices__list-price")
        telefonos[i].precio_tienda = precio_tienda.text

    try:
        precio_internet = elem_precios[i].find_element_by_class_name("catalog-prices__offer-price")
        telefonos[i].precio_internet = precio_internet.text
        
    try:
        precio_tarjeta = elem_precios[i].find_element_by_class_name("catalog-prices__card-price")
        telefonos[i].precio_tarjeta = precio_tarjeta.text
    
    print(telefonos[i].nombre)
    print(telefonos[i].precio_tienda)
    print(telefonos[i].precio_internet)
    print(telefonos[i].precio_tarjeta)
        
    


# for i in range(len(elem)):   
#     try:
#         elem_precios[i].find_element_by_class_name("catalog-prices__card-price")
#         break
#     except:
#         elem[i] = "Na"
    



# elem = elem[14].find_element_by_class_name("catalog-prices__card-price")

# elem_nombre = driver.find_elements_by_class_name('catalog-product-details__name')
# elem_precio = driver.find_elements_by_class_name('catalog-prices__offer-price')  
# elem_precio_tarjeta = driver.find_elements_by_class_name('catalog-prices__card-price')
#elem es un objeto(WebElement) que contiene las propiedades de la clase llamada 'product-price'(como .text)
# for i in range(0,len(elem)):
#     nombre = elem_nombre[i].text
#     precio = elem_precio[i].text
#     precio_tarjeta = elem_precio_tarjeta[i].text
#     info_telefono = telefono.Telefono(nombre,precio, precio_tarjeta)
#     telefonos.append(info_telefono)
# for i in range(len(telefonos)):
#     print(telefonos[i].nombre)
#     print(telefonos[i].precio)
#     print(telefonos[i].precio_tarjeta)
# driver.close()

