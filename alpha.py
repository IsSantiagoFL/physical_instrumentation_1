import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import csv
from uLogg import Meter

if __name__ == "__main__":

    Dtime = 1  # Cambiado a 1 segundo
    TimeWait = 0
    cont = 0
    total_time = 24 * 60 * 60  # 24 horas en segundos

    mt = Meter(Puerto='COM15')
    mt.ReadConfFile('config1.txt')

    data = [[], []]

    with open('temperatura_data.csv', 'w', newline='') as csvfile:
        fieldnames = ['timestamp', 'temperature']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        while cont < total_time:
            TimeNow = datetime.now()
            TimeUnix = TimeNow.timestamp()

            if TimeUnix >= TimeWait:
                TimeWait = TimeUnix + Dtime
                dt = mt.GetOneDat(False)
                temperature = (40.5844E-3) * dt[1] - 22.9740E1
                data[0].append(dt[0])
                data[1].append(temperature)
                writer.writerow({'timestamp': str(data[0][-1])[:-5], 'temperature': temperature})
                cont += 1
                print(f'{cont} {str(data[0][-1])[:-5]} {temperature:.1f}')

    mt.ClosePortLogg()

    # Graficar
    fig, ax1 = plt.subplots()

    color = 'tab:red'
    ax1.set_xlabel('Time')
    ax1.set_ylabel('Temperature', color=color)
    ax1.plot(data[0], data[1], color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()
    color = 'tab:blue'
    ax2.set_ylabel('Derivative', color=color)
    ax2.plot(data[0], np.gradient(data[1]), color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    plt.show()
