import time #para medir el tiempo
import logging #para configurar el logging registrando la mensaje


#confidurar el logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

#CONFIGURAMOS EL REGISTRO DE LOGS parq ue muestre mensajes de nivel INFO o MAYOR
#definimos el formato de los mensajes de registro incluyendo marcas de tiempo, el nivel de mensaje y el mensaje

def timeit(func):
    #decorador para medir el tiempo en una funcion
    def wrapper(*args, **kwargs):
        start_time = time.time() #registrar el tiempo de inicio
        result = func(*args, **kwargs) #ejecutar la funcion decorada
        end_time = time.time() #registrar el tiempo de finalización
        elapsed_time = end_time - start_time #calcular el tiempo de ejecución
        logging.info(f"Tiempo de ejecución de: {func.__name__}: {elapsed_time:.4f} segundos") #registrar el tiempo de ejecución
        
        return result #retornamos el resiltado
    return wrapper #devolver el decorador


def logit(func):
    #decorador para registrar el tiempo de ejecución de una funcion
    def wrapper(*args, **kwargs):
        logging.info(f"Se inicio: {func.__name__}") #registrar el tiempo de inicio
        result = func(*args, **kwargs) #ejecutar la funcion decorada
        logging.info(f"Se ejecuto: {func.__name__}") #registrar el tiempo de ejecución
        return result #retornamos el resiltado
    return wrapper #devolver el decorador