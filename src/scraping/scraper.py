import requests #para hacer las solicitudes http
from bs4 import BeautifulSoup #para extraer datos de la web
import pandas as pd #para trabajar con datos tabulares




def fetch_page (url):
    #obtenemos el contenido de la web
    response = requests.get(url) #realizamos una solicitud get a la web
    #print(response)
    if response.status_code == 200: #200 significa que la petición fue exitosa
        return response.content #devolvemos el contenido de la pagina
    else:
        raise Exception(f'Failed to fetch page: {url}, status {response.status_code}: reason  {response.reason}') #lanzamos una excepcion por si la solicitud falla


#print(fetch_page(url))

def parse_product (product):
    #analizamos los detalles de un producto
    title= product.find('h5', class_="product-name").text.strip() #encontramos y obtenemos el nombre del producto
    #description= product.find('p', class_="description").text.strip() #encontramos y obtenemos la descripción del producto
    price= product.find('div', class_="price").text.strip() #encontramos y obtenemos el precio del producto
    client_price= product.find('span', class_="product-price").text.strip() #encontramos y obtenemos el precio del producto
    return { #retornamos un diccionario con el titulo, descripcon y precio del producto
        'title': title, 
        #'description': description,
        'price': price,
        'client_price': client_price
    }




def scrape (url):
    #funcion principal del scraping
    page_content = fetch_page(url) #obtenemos el código base de la página
    soup = BeautifulSoup(page_content, 'html.parser') #analizamos el contenido de la página con beautifusoup
    print(soup)
    products = soup.find_all('article', class_="product-miniature") #encontramos todos los elementos div con la clase thumbnail que representan productos
    #print(products)
    products_data = [] #inicializamos una lista vacia para almacenar los datos de los productos

    for product in products:
        product_info = parse_product(product) #analizamos cada producto encontrado
        products_data.append(product_info) #agregamos los datos del producto a la lista

    #print(products_data)   
    return pd.DataFrame(products_data)

#print(scrape(url))

#dirección de la pagina para analizar
base_url="https://www.sukasa.com/172-colchones-bases-y-protectores"


#llamamos a la funcion scrape para obtener los datos del producto
df = scrape(base_url)

#imprimimos el df resultante
print(df)

#guardamos los datos en un archivo csv sin incluir el índice
df.to_csv('data/raw/productos.csv', index=False, encoding="utf-8")
 
