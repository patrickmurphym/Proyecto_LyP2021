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

def tableMean(df, parameter):
    df = df.copy().dropna()
    print("Mean of the table: ", df[parameter].mean())

def search(df, product):
    df['name'] = df['name'].str.lower()
    return df[df['name'].str.contains(product)]