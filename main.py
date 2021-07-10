from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options 
import telefono
import buscador_precio_paris.buscador as bparis

'''estas son opciones de como se abrira chroma'''
options = webdriver.ChromeOptions()
options.add_argument("--headless")  #esta es la opcion que hace que no haya UI
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.add_argument("--no-sandbox")
options.add_argument("--disable-setuid-sandbox")

driver = webdriver.Chrome(
    executable_path=("/usr/local/bin/chromedriver"), 
    options=options
    )
    # argumentos para que funcione en wsl2

bparis.smartphones(driver)

driver.close()