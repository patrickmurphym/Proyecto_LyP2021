from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import platform
import os
import csv


class Methods():

    def getOptions(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("--test-type")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-setuid-sandbox")
        options.add_argument('--ignore-ssl-errors')
        return options

    def getPath(self):
        os_name = platform.system()
        if os_name == "Windows":
            path = os.getcwd() + os.path.sep + "chromedriver_win.exe"
            return path
        if os_name == "Linux":
            path = os.getcwd() + os.path.sep + "chromedriver_linux"
            return path
        if os_name == "Darwin":
            path = os.getcwd() + os.path.sep + "chromedriver_mac"
            return path

    def csvOut(self, phones):
        with open("data.csv", 'w', newline='', encoding='utf8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(
                ['name', 'storePrice', 'internetPrice', 'cardPrice', 'page'])
            for phone in phones:
                writer.writerow(
                    [phone.name, phone.storePrice, phone.internetPrice, phone.cardPrice, phone.page])
