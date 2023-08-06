# Importar los módulos necesarios
import numpy as np # Para realizar operaciones matemáticas, arrays, matrices, etc.
import matplotlib.pyplot as plt # Para la creación de gráficos y visulizarlos
from datetime import datetime # Para trabajar con fechas y tiempos
from datetime import timedelta # Para trabajar con fechas y tiempos
from uLogg import Meter # Para interactuar con el datalogger

# Definir las constantes:
D_TIME = 0.1 # Es el intervalo de tiempo que se espera entre cada lectura
NUM_READINGS = 200 # Número de lecturas que se tomaran del dispositivo
PORT = 'COM15' # Indica al puerto al que se conectara el dispositivo
CONFIG_FILE = 'config1.txt' # Indica el archivo que contiene la configuración del dispositivo


# 1. Configuración del dispositivo en una función:
def configure_device(port, config_file): # Los parametros necesarios sera, el puerto y el archivo de configuración
	'''Configura el dispositivo.'''
	# A continuación de inicializa el dispostivo creando una instancia de la clase "Meter"
	mt = Meter(Puerto = port) # Se indica que se usara el puerto "port" ya definido para comunicarse con el dispositivo
	mt.ReadConfFile(config_file) # Se usa un método para configurar el dispositivo usando el archivo de configuración especificado
	return mt # Devuelve el objeto "mt" que es el dispotivo ya configurado y conectado, listo para ser usado.

# 2. Adquisición de datos con el dispositivo ya configurado:
def collect_data(device, num_readings): # Parametros de entrada: Dispositivo previamente configurado y numero de lecturas a tomar
	'''Recolecta datos del dispositivo.'''
	data = [[],[]] # Se inicializa una lista llamada "data", es una lista bidimensional para almacenar los datos del dispositivo
	cont = 0 # Se inicializa el contador "cont" en cero, para rastrear el conjunto de datos recolectados
	time_wait = 0 # Se inicializa la varialbe a cero, Es el tiempo que espera antes de tomar la siguiente lectura

	while cont < num_readings: # Comienza un bucle que se ejecuta mientras el contador cont sea menor que num_readings.
		time_now = datetime.now()	# Obtiene el tiempo actual y lo almacena en la variable time_now.
		time_unix = time_now.timestamp() # Convierte time_now a una marca de tiempo UNIX y lo almacena en time_unix.

		if time_unix >= time_wait: # Verifica si la marca de tiempo UNIX actual es mayor o igual a time_wait. Si es cierto, es hora de recolectar un nuevo conjunto de datos.
			time_wait = time_unix + D_TIME # Actualiza la variable time_wait agregándole D_TIME, que es una constante definida previamente. Esto establece el próximo punto en el tiempo en el que se debería recolectar otro conjunto de datos.
			dt = device.GetOneDat(False) # Llama al método GetOneDat del objeto device (que representa el dispositivo) para obtener un conjunto de datos.
			# Los datos seran almacenados en la lista "data":
			data[0].append(dt[0]) # Agrega el primer elemento del conjunto de datos (dt[0]) a la primera lista en data.
			data[1].append((40.5844E-3)*dt[1]-22.9740E1) # Multiplica el segundo elemento del conjunto de datos (dt[1]) por 40.5844E-3, le resta 22.9740E1, y añade el resultado a la segunda lista en data.
			cont += 1 # Incrementa el contador cont en 1, indicando que se ha recolectado un conjunto adicional de datos.
			print(f'{cont} {str(data[0][-1])[:-5]} {data[1][-1]:.1f}') # imprimir información en la consola: numero actual de conjunto de datos recolectados, ultimo valor agregado a las listas de data.
	
	return data # devuelve la lista data que contiene los datos recolectados.
			
# 3. Se define la función para crear las graficas de los datos obtenidos:
def plot_data(data): # El unico parametro de entrada que acepta es "data" la lista para almacenar los datos obtenidos por el dispositivo.
    """Grafica los datos recolectados."""
    plt.plot(data[0], data[1]) # La función toma dos argumentos, que son las coordenadas x e y para el gráfico. En este caso, data[0] se usa para el eje x, y data[1] se usa para el eje y.
    plt.show() # para visualizar el gráfico en una ventana emergente. Esta función muestra el gráfico y permite al usuario interactuar con él


if __name__ == "__main__":
	# 1. Configuración del dispositivo:
	device = configure_device(PORT, CONFIG_FILE) # Se configura el dispositivo y se guarda en nla variable "device"

	# 2. Adquisición de datos
	data = collect_data(device, NUM_READINGS) # Se hace al adquisiscion de datos y se guarda en la varible "data"

	# 3. Finalización y graficación
	device.ClosePortLogg() # Se cierra la comunicación, la conexción con el dispositivo "device", liberando el recurso asociado
	plot_data(data) # Se grafica los datos guardados en la variable "data"