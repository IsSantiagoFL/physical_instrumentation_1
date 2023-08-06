# Importar los módulos necesarios
import numpy as np # Para realizar operaciones matemáticas, arrays, matrices, etc.
import matplotlib.pyplot as plt # Para la creación de gráficos y visulizarlos
from datetime import datetime # Para trabajar con fechas y tiempos
from datetime import timedelta # Para trabajar con fechas y tiempos
from uLogg import Meter # Para interactuar con el datalogger

if __name__ == "__main__":
	
# Definir las constantes:

D_TIME = 0.1 # Es el intervalo de tiempo que se espera entre cada lectura
NUM_READINGS = 200 # Número de lecturas que se tomaran del dispositivo
PORT = 'COM15' # Indica al puerto al que se conectara el dispositivo
CONFIG_FILE = 'config1.txt' # Indica el archivo que contiene lña configuración del dispositivo


# Configuración del dispositivo:
mt=Meter(Puerto = PORT) # Se crea una instancia del objeto "Meter" que representa el dispositivo y se conecta al puerto "COM15" 
mt.ReadConfFile( CONFIG_FILE ) # Se usa un método para leer el archivo de configuración config1.text para configurar el dispositivo.

# Adquisición de datos:

TimeWait=0 # Es el tiempo que espera antes de tomar la siguiente lectura
cont=0 # Es un contador utilizado para realizar 200 lecturas
data=[[],[]] # Es una lista bidimensional para almacenar los datos del dispositivo


while cont < NUM_READINGS: # Bucle que tomara 200 lecturas del dispositivo
	TimeNow=datetime.now()	# Sirve para saber el tiempo y la hora actual
	TimeUnix=TimeNow.timestamp()	

	if TimeUnix >= TimeWait: # Cada vez que el tiempo actual alcanza (o supera) el TimeWait, se realiza una lectura del dispositivo, se almacena y se actualiza el TimeWait para la próxima lectura.
		TimeWait=TimeUnix + D_TIME
		dt=mt.GetOneDat(False)
		# Los datos seran almacenados en la lista "data"
		data[0].append(dt[0])
		data[1].append((40.5844E-3)*dt[1]-22.9740E1)
		cont += 1
		print(f'{cont} {str(data[0][-1])[:-5]} {data[1][-1]:.1f}') # imprimir información en la consola.
		
# Finalización:
mt.ClosePortLogg() # Se cierra el puerto de comunicación con el dispositivo.

# Se grafican los datos recolectados.
plt.plot(data[0], data[1])
plt.show()
