# Importar los módulos necesarios
import numpy as np 
import matplotlib.pyplot as plt 
import csv
from datetime import datetime

def load_from_csv(filename="temperatura_ambiente.csv"):
    '''Carga los datos desde un archivo CSV y devuelve una lista de listas: [tiempos, temperaturas].'''
    times = []
    temperatures = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Salta la fila de encabezados
        start_time = None
        for row in reader:
            # Convertimos las cadenas de tiempo a objetos datetime
            current_time = datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S")
            if start_time is None:
                start_time = current_time  # Establece el primer tiempo que encuentre como tiempo de inicio
            # Calcula la diferencia en segundos desde el tiempo de inicio
            elapsed_time = (current_time - start_time).total_seconds()
            times.append(elapsed_time)
            temperatures.append(float(row[1]))

    return [times, temperatures]


def compute_statistics(data):
    statistics = {}
    statistics["start_time"] = data[0][0]
    statistics["end_time"] = data[0][-1]
    statistics["total_time"] = statistics["end_time"] - statistics["start_time"]
    statistics["sampling_interval"] = data[0][1] - data[0][0]
    temperatures = np.array(data[1])
    statistics["min_temp"] = np.min(temperatures)
    statistics["max_temp"] = np.max(temperatures)
    statistics["mean_temp"] = np.mean(temperatures)
    statistics["std_temp"] = np.std(temperatures)
    statistics["num_readings"] = len(temperatures)
    return statistics


def plot_data(data): # El unico parametro de entrada que acepta es "data" la lista para almacenar los datos obtenidos por el dispositivo.
    """Grafica los datos recolectados y su derivada."""
    # Obteniendo las diferencias de tiempo y temperatura.
    # time_deltas = np.diff(data[0]) # Diferencias consecutivas en el tiempo
        
    temp_deltas = np.diff(data[1]) # Diferencias consecutivas en la temperatura

    # Convertir time_deltas a segundos (es una lista de objetos timedelta)
    # time_deltas_in_seconds = [delta.total_seconds() for delta in time_deltas]

    # Calculamos la derivada (pendiente) de la temperatura respecto al tiempo
    # derivatives = temp_deltas / np.array(time_deltas_in_seconds)
    
    derivatives = temp_deltas / np.diff(data[0])


	# Graficamos los datos originales (Temperatura)

    fig, ax1 = plt.subplots()

    ax1.set_xlabel('Tiempo')
    ax1.set_ylabel('Temperatura (ºC)', color='#0000FF')
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

    # Definimos las líneas de la gráfica
    temp_handle, = ax1.plot(data[0], data[1], label='Temperatura Ambiente', color='#0000FF', linestyle='--')

	# Definimos las leyendas usando líneas invisibles
    # Utiliza el diccionario 'statistics' para construir las etiquetas
    labels = [
        f"Min Temp: {statistics['min_temp']:.2f} ºC",
        f"Max Temp: {statistics['max_temp']:.2f} ºC",
        f"Mean Temp: {mean_temp:.2f} ºC",
        f"Std Dev: {std_temp:.2f}",
        f"Num of Readings: {num_readings}",
        f"Start Time: {start_time}",
        f"End Time: {end_time}",
        f"Total Time: {total_time}",
        f"Sampling Interval: {sampling_interval}"
        ]
    handles = [temp_handle] + [ax1.plot([], [], marker="", linestyle="", label=label)[0] for label in labels]

	# Mostramos la leyenda con todas las etiquetas en el eje izquierdo
    ax1.legend(handles=handles, loc="upper left")


	# para visualizar el gráfico en una ventana emergente.
    plt.show() # Esta función muestra el gráfico y permite al usuario interactuar con él



if __name__ == "__main__":

    start_time = data[0][0]
    end_time = data[0][-1]
    total_time = end_time - start_time

    data = load_from_csv("temperatura_ambiente.csv")  # Carga los datos del CSV
    
    # Calculando las estadísticas (podrías encapsular esto en una función para no repetir código)

    statistics = compute_statistics(data)  # Obtener las estadísticas
    plot_data(data, statistics)  # Pasa los datos y las estadísticas a plot_data   
    plot_data(data)  # Grafica los datos
