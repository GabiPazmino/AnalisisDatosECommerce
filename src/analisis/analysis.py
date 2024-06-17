import pandas as pd #para manipular datos
import os #para interactuar con el sistema operativo
from ..decorations.decorators import timeit, logit #importamos los decoradores

@logit #añamos el logging para registrar el tiempo de ejecución de la funcion
@timeit # añamos que se registre el tiempo de ejecución de la funcion
def load_data (data_path):
    #cargar datos desde un csv o excel

    if data_path.endswith('.csv'):
        df= pd.read_csv(data_path) #cargamos los datos del archivo csv

    elif data_path.endswith('.xlsx'):
        df= pd.read_excel(data_path) #cargamos los datos del archivo excel

    else:
        raise ValueError('The file format is not supported') #lanzamos un error si el formato del archivo no es compatible
    print ("Data loaded successfully") #imprimimos un mensaje indicando que se cargaron correctamente los datos

    return df

#print(load_data("data/raw/productos.csv"))

@logit #añamos el logging para registrar el tiempo de ejecución de la funcion
@timeit # añamos que se registre el tiempo de ejecución de la funcion
def clean_data (df):
    #limpiar los datos
   # Eliminar todo lo que esté antes del primer número en la columna "price"
    df["price"] = df["price"].str.extract(r'(\d+\.?\d*)').astype(float)
       # Eliminar todo lo que esté antes del primer número en la columna "client_price"
    df["client_price"] = df["client_price"].str.extract(r'(\d+\.?\d*)').astype(float)


    print ("Data cleaned successfully") #imprimimos un mensaje indicando que se limpiaron correctamente los datos

    return df #devolvemos los datos


@logit #añamos el logging para registrar el tiempo de ejecución de la funcion
@timeit # añamos que se registre el tiempo de ejecución de la funcion
def analize_data(df):
    #analizar los datos
    print ("Basic data analysis: ") #imprimimos un encabezado para el analisis de datos
    print(df.describe()) #imprimimos un resumen estadísticos de los datos
    
    #calsulo de estadsisticas
    print ("\nPrice' statistics: ") #imprimimos un encabezado para el calculo de estadisticas
    print(f"Precio promedio: ${df['price'].mean():.2f}")
    print(f"Precio maximo: ${df['price'].max():.2f}")
    print(f"Precio minimo: ${df['price'].min():.2f}")
    print(f"Precio Sukasa promedio: ${df['client_price'].mean():.2f}")
    print(f"Precio Sukasa maximo: ${df['client_price'].max():.2f}")
    print(f"Precio Sukasa minimo: ${df['client_price'].min():.2f}")
    
    print ("\nProducts with the highest prices: ") #imprimimos un encabezado para los productos con el precio mas altos
    highest_prices = df.nlargest(10, 'price') #obtenemos los 10 productos con el precio mas alto
    print(highest_prices) #imprimimos los productos con el precio mas alto
    lowest_prices = df.nsmallest(10, 'price') #obtenemos los 10 productos con el precio mas bajo
    print ("\nProducts with the lowest prices: ") #imprimimos un encabezado para los productos con el precio mas bajos
    print(lowest_prices) #imprimimos los productos con el precio mas bajo

    # Combinar ambos conjuntos de datos en un solo DataFrame
    combined_df = pd.concat([highest_prices, lowest_prices])

    return combined_df #devolvemos los datos


@logit #añamos el logging para registrar el tiempo de ejecución de la funcion
@timeit # añamos que se registre el tiempo de ejecución de la funcion
def save_clean_data(df, df_analyzed, output_path, output_analyzed_path):
    #guardar los datos linpios
    if output_path.endswith('.csv'):
        df.to_csv(output_path, index=False, encoding="utf-8") #guardamos los datos en un archivo csv

    elif output_path.endswith('.xlsx'):
        df.to_excel(output_path, index=False, encoding="utf-8") #guardamos los datos en un archivo excel

    else:
        raise ValueError('The file format is not supported') #lanzamos un error si el formato del archivo no es compatible
    print ("Clean data saved successfully to {output_path}") #imprimimos un mensaje indicando que se guardaron correctamente los datos


    
    #guardar los datos 
    if output_analyzed_path.endswith('.csv'):
        df_analyzed.to_csv(output_analyzed_path, index=False, encoding="utf-8") #guardamos los datos en un archivo csv

    elif output_analyzed_path.endswith('.xlsx'):
        df_analyzed.to_excel(output_analyzed_path, index=False, encoding="utf-8") #guardamos los datos en un archivo excel

    else:
        raise ValueError('The file format is not supported') #lanzamos un error si el formato del archivo no es compatible
    print ("Analyzed data saved successfully to {output_analyzed_path}") #imprimimos un mensaje indicando que se guardaron correctamente los datos





if __name__ == "__main__": #permitimos que el script se ejecute solamente en este archivo

    data_path = 'data/raw/productos.csv' #definimos la ruta de datos crudos

    output_path = "data/process/cleaned_productos.csv" #definimos la ruta de datos 

    output_analyzed_path = "data/process/productos_max_min_prices.csv" #definimos la ruta de datos analizados

    df = load_data(data_path) #cargamos los datos crudos
    df = clean_data(df) #limpiamos los datos cargados
    df_analyzed = analize_data(df) #analizamos los datos
       # Asegurarnos de que exista el directorio para guardar los datos
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    os.makedirs(os.path.dirname(output_analyzed_path), exist_ok=True)

    # Guardar los datos limpios y analizados en archivos CSV separados
    save_clean_data(df, df_analyzed, output_path, output_analyzed_path)