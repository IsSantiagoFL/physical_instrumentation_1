# Importar los módulos necesarios
import numpy as np # Para realizar operaciones matemáticas, arrays, matrices, etc.
import matplotlib.pyplot as plt # Para la creación de gráficos y visulizarlos
from datetime import datetime # Para trabajar con fechas y tiempos
from datetime import timedelta # Para trabajar con fechas y tiempos
from uLogg import Meter # Para interactuar con el datalogger
import csv # Importar el modulo csv para guardar los datos en un .csv


# Definir las constantes:
PORT = 'COM15' # Indica al puerto al que se conectara el dispositivo
CONFIG_FILE = 'config1.txt' # Indica el archivo que contiene la configuración del dispositivo

# Crea una función que devuelve "D_TIME" a partir de lo que el usuario desee
def get_sampling_interval():
	'''Solicita al usuario el intervalo de muestreo (tiempo entre lecturas) en segundos'''
	try:
		D_TIME = float(input("Ingrese el intervalo de muestre en segundos (por ejemplo, 1.0 para un dato por segundo): "))
		return D_TIME
	except ValueError:
		print("Por favor, ingrese un valor numérico válido.")
		return get_sampling_interval()

# Funcion: piude al usuario el tiempo de toma de datos y lo convierte a segundos.
def get_duration_in_seconds():
	'''Solicita al usuario la duración y la unidad (segundos, mimutos u horas)
	y devuelve la duración total en segundos'''

	print("¿Durante cuanto tiempo desea recolectar datos?")
	print("Primero seleccione la unidad de tiempo:")
	print("1: Segundos")
	print("2: Minutos")
	print("3: Horas")

	choice = input("Ingrese su opción (1/2/3): ")

	if choice == "1":
		try:
			duration = float(input("Ingrese la duración en segundos: "))
			return duration
		except ValueError:
			print("Por favor, ingrese un valor numérico válido.")
			return get_duration_in_seconds()
		
	elif choice == "2":
		try:
			duration = float(input("Ingrese la duración en minutos: "))
			return duration * 60 # Convertimos minutos a segundos
		except ValueError:
			print("Por favor, ingrese un valor numérico válido.")
			return get_duration_in_seconds()
		
	elif choice == "3":
		try:
			duration = float(input("Ingrese la duración en horas: "))
			return duration * 3600 # Convertimos horas a segundos
		except ValueError:
			print("Por favor, ingrese un valor numérico válido.")
			return get_duration_in_seconds()
	else:
		print("Opción no valida, Por favor, selecione 1, 2 o 3.")
		return get_duration_in_seconds()

# Configuración del dispositivo en una función:
def configure_device(port, config_file): # Los parametros necesarios sera, el puerto y el archivo de configuración
	'''Configura el dispositivo.'''
	# A continuación de inicializa el dispostivo creando una instancia de la clase "Meter"
	mt = Meter(Puerto = port) # Se indica que se usara el puerto "port" ya definido para comunicarse con el dispositivo
	mt.ReadConfFile(config_file) # Se usa un método para configurar el dispositivo usando el archivo de configuración especificado
	return mt # Devuelve el objeto "mt" que es el dispotivo ya configurado y conectado, listo para ser usado.

# Adquisición de datos con el dispositivo ya configurado:
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

# Guarda los datos recolectados en un archivo .csv
def save_to_csv(data, filename="data.csv"): # Aquí se esta definicinedo la función
    '''Guarda los datos en un archivo CSV.'''
    with open(filename, 'w', newline='') as file: # Se esta creando el archivo con permisos de escritura
        writer = csv.writer(file) # creamos el objeto "writer" que nos permite escribir datos en ela archivo
        writer.writerow(["Tiempo", "Temperatura (ºC)"])  # Escribir encabezados
        for i in range(len(data[0])): # El bucle iterara cada elemento de "data" donde estan los datos guardados
            writer.writerow([data[0][i], data[1][i]]) # y luego los ira escibiendo en el archivo CSV

# Se define la función para crear las graficas de los datos obtenidos:
def plot_data(data): # El unico parametro de entrada que acepta es "data" la lista para almacenar los datos obtenidos por el dispositivo.
	"""Grafica los datos recolectados y su derivada."""
	# Obteniendo las diferencias de tiempo y temperatura.
	time_deltas = np.diff(data[0]) # Diferencias consecutivas en el tiempo
	temp_deltas = np.diff(data[1]) # Diferencias consecutivas en la temperatura

	# Convertir time_deltas a segundos (es una lista de objetos timedelta)
	time_deltas_in_seconds = [delta.total_seconds() for delta in time_deltas]

	# Calculamos la derivada (pendiente) de la temperatura respecto al tiempo
	derivatives = temp_deltas / np.array(time_deltas_in_seconds)

	# Graficamos los datos originales (Temperatura)
	fig, ax1 = plt.subplots()

	ax1.set_xlabel('Tiempo')
	ax1.set_ylabel('Temperatura (ºC)', color = 'tab:blue')
	ax1.plot(data[0], data[1], label='Temperatura Ambiente', color='#0000FF', linestyle='--')
	ax1.tick_params(axis='y', labelcolor='#0000FF')

	# Creando un segundo eje para la derivada
	ax2 = ax1.twinx()
	ax2.set_ylabel('Derivada (ºC/s)', color = 'tab:red')
	ax2.plot(data[0][1:], derivatives, label='Derivada', color='red', alpha=0.75)  # Color rojo con transparencia
	ax2.tick_params(axis='y', labelcolor='red')

	# Configurando el aspecto visual
	plt.title('Temperatura Ambiente y su derivada a lo largo del tiempo') # Título del gráfico
	fig.tight_layout()
	# plt.legend() # Mostrar leyenda
	plt.grid(True) # Mostrar una grilla para facilitar la lectura
	
	# para visualizar el gráfico en una ventana emergente.
	plt.show() # Esta función muestra el gráfico y permite al usuario interactuar con él


if __name__ == "__main__":
	# Solicitamos el intervalo de muestreo al usuario:
	D_TIME = get_sampling_interval()

	# Calcularemos el número total de lecturas que tomara el dispositivo.
	time_seconds = get_duration_in_seconds()
	NUM_READINGS = int(time_seconds / D_TIME) # divismos el tiempo de muestreo entre el intervalo de muestreo, ambos en unidades de segundos.
	
	# Configuración del dispositivo:
	device = configure_device(PORT, CONFIG_FILE) # Se configura el dispositivo y se guarda en nla variable "device"

	# Adquisición de datos
	data = collect_data(device, NUM_READINGS) # Se hace al adquisiscion de datos y se guarda en la varible "data"

	# Guardar los datos en un archivo CSV:
	save_to_csv(data, "temperatura_ambiente.csv")

	# Finalización y graficación
	device.ClosePortLogg() # Se cierra la comunicación, la conexción con el dispositivo "device", liberando el recurso asociado
	plot_data(data) # Se grafica los datos guardados en la variable "data"