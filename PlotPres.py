import serial
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from drawnow import drawnow
import time


Pres = []
arduinoData = serial.Serial('/dev/ttyACM0',9600)
plt.ion()
t = []
tempo = 0

fname = 'medição'+str(time.time())
#time = int(input(r'Duração: '))
def makeFig():
    arduinoString = float(arduinoData.readline())
    #print(arduinoString,tempo)
    #dataArray = arduinoString
    #P = float(dataArray[0])
    Pres.append(arduinoString)
    t.append(tempo)
    plt.plot(t,Pres)
    plt.xlabel('Tempo (s)')
    plt.ylabel('Pressão')
    plt.grid()
    plt.ion()

  #  f.writelines(Pres,t)
'''
for tempo in range(time):es
    while(arduinoData.inWTaiting()==0):
        pass
    #tempo = tempo + 1
    drawnow(makeFig)
'''


#run = False
run = True
tempo = 0
while run:
    tempo = tempo + 1
    drawnow(makeFig)
    df = pd.DataFrame({})
    df['Pres'] = Pres
    df['t'] = t

    df.to_csv(f'{fname}.csv', sep=',', index=False)
