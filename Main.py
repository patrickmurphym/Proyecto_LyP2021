from selenium import webdriver
import Methods as mt


class Product(object):
    def __init__(self, name, storePrice, internetPrice, cardPrice, page):
        self.name = name
        self.storePrice = storePrice
        self.internetPrice = internetPrice
        self.cardPrice = cardPrice
        self.page = page

    def __repr__(self):
        return "Product('{}','{}','{}','{}','{}')".format(
            self.name,
            self.storePrice,
            self.internetPrice,
            self.cardPrice,
            self.page)

    def __str__(self):
        return '{} - {} - {} - {} - {}'.format(
            self.name,
            self.storePrice,
            self.internetPrice,
            self.cardPrice,
            self.page)


class Ripley(Product):
    def __init__(self):
        pass

    def scrapper(self, driver, phones):
        driver.get(
            "https://simple.ripley.cl/tecno/celulares?facet=Marca%3AAPPLE&facet=Tipo%20de%20producto%3ASmartphone")
        names = driver.find_elements_by_class_name(
            'catalog-product-details__name')
        prices = driver.find_elements_by_class_name('catalog-prices__list')
        for i in range(len(names)):
            name = names[i].text

            try:
                storePrice = prices[i].find_element_by_class_name(
                    "catalog-prices__list-price")
                storePrice = int(storePrice.text.replace(
                    "$", "").replace(".", ""))
            except:
                storePrice = "Na"

            try:
                internetPrice = prices[i].find_element_by_class_name(
                    "catalog-prices__offer-price")
                internetPrice = int(
                    internetPrice.text.replace("$", "").replace(".", ""))
            except:
                internetPrice = "Na"

            try:
                cardPrice = prices[i].find_element_by_class_name(
                    "catalog-prices__card-price")
                cardPrice = int(cardPrice.text.replace(
                    "$", "").replace(".", ""))
            except:
                cardPrice = "Na"

            phone = Product(name, storePrice, internetPrice,
                            cardPrice, "Ripley")
            phones.append(phone)


class Paris(Product):
    def __init__(self):
        pass

    def scrapper(self, driver, phones):
        driver.get("https://www.paris.cl/tecnologia/celulares/smartphone/apple/")
        names = driver.find_elements_by_class_name('ellipsis_text')
        prices = driver.find_elements_by_class_name('price')
        for i in range(len(names)):
            name = names[i].text

            try:
                storePrice = prices[i].find_element_by_class_name(
                    "price__text-sm")
                storePrice = int(storePrice.text.replace(
                    "$", "").replace(".", ""))

            except:
                storePrice = "Na"

            try:
                temp = prices[i].find_element_by_class_name(
                    "price__text-wrap.price__text-wrap--primary")
                internetPrice = temp.find_element_by_class_name("price__text")
                internetPrice = int(
                    internetPrice.text.replace("$", "").replace(".", ""))
            except:
                internetPrice = "Na"

            try:
                cardPrice = prices[i].find_element_by_class_name("price__text")
                cardPrice = int(cardPrice.text.replace(
                    "$", "").replace(".", ""))

            except:
                cardPrice = "Na"

            phone = Product(name, storePrice, internetPrice,
                            cardPrice, "Paris")
            phones.append(phone)


class Linio(Product):
    def __init__(self):
        pass

    def scrapper(self, driver, phones):
        driver.get(
            "https://www.linio.cl/c/celulares-y-tablets/celulares-y-smartphones/b/apple")
        names = driver.find_elements_by_class_name('title-section')
        prices = driver.find_elements_by_class_name('price-section')
        for i in range(len(names)):
            name = name = names[i].text

            try:
                storePrice = prices[i].find_element_by_class_name(
                    "original-price")
                storePrice = int(storePrice.text.replace(
                    "$", "").replace(".", ""))

            except:
                storePrice = "Na"

            try:
                internetPrice = prices[i].find_element_by_class_name(
                    "price-main-md")
                internetPrice = int(
                    internetPrice.text.replace("$", "").replace(".", ""))
            except:
                internetPrice = "Na"

            try:
                cardPrice = prices[i].find_element_by_class_name(
                    "price-promotional")
                cardPrice = int(cardPrice.text.replace(
                    "$", "").replace(".", ""))

            except:
                cardPrice = "Na"

            phone = Product(name, storePrice, internetPrice,
                            cardPrice, "Linio")
            phones.append(phone)


def main():
    rpl = Ripley()
    prs = Paris()
    lno = Linio()
    options = mt.Methods().getOptions()
    path = mt.Methods().getPath()
    phones = []
    driver = webdriver.Chrome(executable_path=(path), chrome_options=options)
    rpl.scrapper(driver, phones)
    prs.scrapper(driver, phones)
    lno.scrapper(driver, phones)

    for x in phones:
        print(x)

    mt.Methods().csvOut(phones)


if __name__ == '__main__':
    main()
