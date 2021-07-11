# Implementamos un mínimo de 12 funciones para que mostrara lo que queríamos que mostrara.
# 6 integrantes * 2 funciones = 12 como mínimo.

def Tienda():
    print("En qué tienda quieres buscar:")
    print("\t- Paris")
    print("\t- Ripley")
    print("\t- Linio")
    return input("Introduce el nombre de la tienda: ").capitalize()

def checkTienda(tienda):
    if tienda in ['Paris', 'Ripley', 'Linio']:
        return True
    else: 
        print("\nTienda introducida incorrecta.\nIntente de nuevo.")
        return False

def minPrice(df, tienda): 
    if checkTienda(tienda):
        printPrice(df.iloc[df[df['page'] == tienda]['internetPrice'].idxmin(),[0,2]], tienda, "barato")
    else:
        return

def maxPrice(df, tienda):
    if checkTienda(tienda):
        printPrice(df.iloc[df[df['page'] == tienda]['internetPrice'].idxmax(),[0,2]], tienda, "caro")
    else:
        return

def printPrice(df, tienda, tipo):
    print("\nEn "+tienda+" el producto Apple más "+tipo+" es "+str(df['name'])+' a un precio de '+str(df['internetPrice']))

def minPriceAll(df): 
    printPriceAll(df.iloc[df['internetPrice'].idxmin(),:], 'barato')

def maxPriceAll(df): 
    printPriceAll(df.iloc[df['internetPrice'].idxmax(),:], 'caro')

def printPriceAll(df, tipo):
    print("\nEl producto más "+tipo+" está en " + str(df['page']) + ", y es un " + str(df['name']) + " a " + str(df['internetPrice']))

def meanOption():
    print("\n¿Qué promedio desea?")
    print("\t1. Precio tienda")
    print("\t2. Precio internet")
    print("\t3. Precio tarjeta")
    return int(input("Seleccione precio: "))

def storeOption():
    print("¿En qué tienda quiere buscar buscar?")
    print("\t1. Ripley")
    print("\t2. Paris")
    print("\t3. Linio")
    print("\t4. Todas")
    return int(input("Seleccione tienda: "))

def tableMean(df, parameter):
    df = df.copy().dropna()
    print("\nMean of the table: ", "{:.2f}".format(df[parameter].mean()))

def productName():
    print("Introduzca nombre del producto: ")
    return input()

def search(df, product):
    df['name'] = df['name'].str.lower()
    print(df[df['name'].str.contains(product)])

def buscar(df):
    a = storeOption()
    b = productName()
    if a == 1:
        search(df[df['page'] == 'Ripley'], b)
    if a == 2:
        search(df[df['page'] == 'Paris'], b)
    if a == 3:
        search(df[df['page'] == 'Linio'], b)
    if a == 4:
        search(df, b)

def promedio(df):
    b = storeOption()
    c = meanOption()
    if b == 1:
        if c == 1:
            tableMean(df[df['page'] == 'Ripley'], "storePrice")
        if c == 2:
            tableMean(df[df['page'] == 'Ripley'], "internetPrice")
        if c == 3:
            tableMean(df[df['page'] == 'Ripley'], "cardPrice")
    if b == 2:
        if c == 1:
            tableMean(df[df['page'] == 'Paris'], "storePrice")
        if c == 2:
            tableMean(df[df['page'] == 'Paris'], "internetPrice")
        if c == 3:
            tableMean(df[df['page'] == 'Paris'], "cardPrice")
    if b == 3:
        if c == 1:
            tableMean(df[df['page'] == 'Linio'], "storePrice")
        if c == 2:
            tableMean(df[df['page'] == 'Linio'], "internetPrice")
        if c == 3:
            tableMean(df[df['page'] == 'Linio'], "cardPrice")
    if b == 4:
        if c == 1:
            tableMean(df, "storePrice")
        if c == 2:
            tableMean(df, "internetPrice")
        if c == 3:
            tableMean(df, "cardPrice")


