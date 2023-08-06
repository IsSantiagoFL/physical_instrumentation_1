import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from datetime import timedelta
from uLogg import Meter

if __name__ == "__main__":

	Dtime=0.1
	TimeWait=0
	cont=0

mt=Meter(Puerto='COM15') # Instanciar, e indicarle el puerto al que se va conectar 
mt.ReadConfFile('config1.txt')  # Se usa el método para leer el archivo deconfiguración y configurar el dispostivo

data=[[],[]]


while cont<200:
	TimeNow=datetime.now()	# Sirve para saber el tiempo y la hora actual
	TimeUnix=TimeNow.timestamp()	# C

	if TimeUnix >= TimeWait:
		TimeWait=TimeUnix+Dtime
		dt=mt.GetOneDat(False)
		data[0].append(dt[0])
		data[1].append((40.5844E-3)*dt[1]-22.9740E1)
		cont += 1
		print(f'{cont} {str(data[0][-1])[:-5]} {data[1][-1]:.1f}')
mt.ClosePortLogg()
plt.plot(data[0], data[1])
plt.show()
