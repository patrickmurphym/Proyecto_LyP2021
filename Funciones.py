def minPrice(df, tienda): 
    printPrice(df.iloc[df[df['page'] == tienda]['internetPrice'].idxmin(),[0,2]], tienda, "barato")

def maxPrice(df, tienda):
    printPrice(df.iloc[df[df['page'] == tienda]['internetPrice'].idxmin(),[0,2]], tienda, "caro")

def printPrice(df, tienda, tipo):
    print("En "+tienda, "el producto Apple más "+tipo+" es", df['name'], 'a un precio de', df['internetPrice'])
    return
