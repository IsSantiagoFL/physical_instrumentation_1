# Importamos la librería numpy para operaciones matemáticas
import numpy as np
# Importamos la librería matplotlib para graficar
import matplotlib.pyplot as plt
# Importamos funciones de datetime para manejar fechas y tiempos
from datetime import datetime, timedelta
# Importamos la librería csv para escribir y leer archivos CSV
import csv
# Importamos la clase Meter de la librería uLogg para manejar el dispositivo de medición
from uLogg import Meter

# Verificamos si este script se está ejecutando como el principal
if __name__ == "__main__":

    # Definimos el intervalo de tiempo entre mediciones, en este caso 1 segundo
    Dtime = 1
    # Inicializamos una variable para esperar el siguiente tiempo de medición
    TimeWait = 0
    # Contador para llevar registro de cuántas mediciones se han realizado
    cont = 0
    # Definimos el tiempo total de medición, en este caso 24 horas convertidas a segundos
    total_time = 24 * 60 * 60

    # Instanciamos el objeto Meter para comunicarnos con el dispositivo a través del puerto 'COM15'
    mt = Meter(Puerto='COM15')
    # Leemos el archivo de configuración para configurar el dispositivo
    mt.ReadConfFile('config1.txt')

    # Inicializamos una lista para almacenar los datos de tiempo y temperatura
    data = [[], []]

    # Abrimos (o creamos) un archivo CSV en modo escritura
    with open('temperatura_data.csv', 'w', newline='') as csvfile:
        # Definimos los nombres de las columnas del archivo CSV
        fieldnames = ['timestamp', 'temperature']
        # Creamos un escritor de diccionarios para el archivo CSV
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # Escribimos la cabecera del archivo CSV
        writer.writeheader()

        # Mientras no hayamos alcanzado el tiempo total de medición
        while cont < total_time:
            # Obtenemos la fecha y hora actual
            TimeNow = datetime.now()
            # Convertimos la fecha y hora actual a un timestamp (segundos desde 1970)
            TimeUnix = TimeNow.timestamp()

            # Si el timestamp actual es mayor o igual al tiempo de espera
            if TimeUnix >= TimeWait:
                # Actualizamos el tiempo de espera sumándole el intervalo de tiempo
                TimeWait = TimeUnix + Dtime
                # Obtenemos un dato del dispositivo
                dt = mt.GetOneDat(False)
                # Calculamos la temperatura usando la fórmula dada
                temperature = (40.5844E-3) * dt[1] - 22.9740E1
                # Añadimos el dato de tiempo y temperatura a nuestra lista de datos
                data[0].append(dt[0])
                data[1].append(temperature)
                # Escribimos el dato de tiempo y temperatura en el archivo CSV
                writer.writerow({'timestamp': str(data[0][-1])[:-5], 'temperature': temperature})
                # Incrementamos el contador de mediciones
                cont += 1
                # Imprimimos el número de medición, el dato de tiempo y la temperatura
                print(f'{cont} {str(data[0][-1])[:-5]} {temperature:.1f}')

    # Cerramos la comunicación con el dispositivo
    mt.ClosePortLogg()

    # Comenzamos a graficar
    # Creamos una figura y un eje para la gráfica
    fig, ax1 = plt.subplots()

    # Definimos el color para la gráfica de temperatura
    color = 'tab:red'
    # Establecemos las etiquetas de los ejes
    ax1.set_xlabel('Time')
    ax1.set_ylabel('Temperature', color=color)
    # Graficamos los datos de tiempo y temperatura
    ax1.plot(data[0], data[1], color=color)
    # Establecemos el color de las marcas del eje y
    ax1.tick_params(axis='y', labelcolor=color)

    # Creamos un segundo eje y para la derivada de la temperatura
    ax2 = ax1.twinx()
    # Definimos el color para la gráfica de la derivada
    color = 'tab:blue'
    # Establecemos la etiqueta del eje y para la derivada
    ax2.set_ylabel('Derivative', color=color)
    # Graficamos los datos de tiempo y la derivada de la temperatura
    ax2.plot(data[0], np.gradient(data[1]), color=color)
    # Establecemos el color de las marcas del eje y para la derivada
    ax2.tick_params(axis='y', labelcolor=color)

    # Mostramos la gráfica
    plt.show()
