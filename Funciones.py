def Tienda():
    print("En qué tienda quieres buscar:")
    print("\t- Paris")
    print("\t- Ripley")
    print("\t- Linio")
    return input("Introduce el nombre de la tienda: ")

def minPrice(df, tienda): 
    return printPrice(df.iloc[df[df['page'] == tienda]['internetPrice'].idxmin(),[0,2]], tienda, "barato")

def maxPrice(df, tienda):
    return printPrice(df.iloc[df[df['page'] == tienda]['internetPrice'].idxmin(),[0,2]], tienda, "caro")

def printPrice(df, tienda, tipo):
    return "En "+tienda+" el producto Apple más "+tipo+" es "+str(df['name'])+' a un precio de '+str(df['internetPrice'])

def minPriceAll(df): 
    printMinPriceAll(df.iloc[df['internetPrice'].idxmin(),:])

def printMinPriceAll(df):
    print("El producto más barato está en " + str(df['page']) + ", y es un " + str(df['name']) + " a " + str(df['internetPrice']))

def tableMean(df, parameter):
    df = df.copy().dropna()
    print("Mean of the table: ", df[parameter].mean())

def search(df, product):
    df['name'] = df['name'].str.lower()
    return df[df['name'].str.contains(product)]