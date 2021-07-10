# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options 
import telefono

# '''estas son opciones de como se abrira chroma'''
# options = webdriver.ChromeOptions()
# options.add_argument("--headless")  #esta es la opcion que hace que no haya UI
# options.add_argument('--ignore-certificate-errors')
# options.add_argument("--test-type")
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-setuid-sandbox")

#driver = webdriver.Chrome(executable_path=("/usr/bin/chromedriver"), chrome_options=options)# argumentos para que funcione en wsl2
#method para ir a una pagina web

def smartphones(driver):
    driver.get("https://www.paris.cl/tecnologia/celulares/smartphone/")
    elem_nombre = driver.find_elements_by_class_name('ellipsis_text')
    elem_precios = driver.find_elements_by_class_name('price')
    telefonos = []
    for i in range(len(elem_nombre)):
        nombre = elem_nombre[i].text
        Objeto_telefono = telefono.Telefono(nombre,"Na", "Na", "Na")
        telefonos.append(Objeto_telefono)
        
        try:
            elem_precio_tienda = elem_precios[i].find_element_by_class_name("price__text")
            telefonos[i].precio_tienda = elem_precio_tienda.text
        except:
            pass

        try:
            precio_internet = elem_precios[i].find_element_by_class_name("price-internet")
            telefonos[i].precio_internet = precio_internet.text
        except:
            pass
        try:
            precio_internet = elem_precios[i].find_element_by_class_name("col-md-9.col-xs-9.item-price.offer-price.price-tc.default-price")
            telefonos[i].precio_internet = precio_internet.text
        except:
            pass

        try:
            precio_tarjeta = elem_precios[i].find_element_by_class_name("col-md-9.col-xs-9.item-price.offer-price.price-tc.cencosud-price")
            telefonos[i].precio_tarjeta = precio_tarjeta.text
        except:
            pass
    
    print(telefonos[0].nombre)
    print(telefonos[0].precio_tienda)
    print(telefonos[0].precio_internet)
    print(telefonos[0].precio_tarjeta)
    #print("----------------------------------")
    
    return


#driver.close()
