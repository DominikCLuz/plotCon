import threading
import time
import matplotlib.pyplot as plt
import numpy as np
from drawnow import *
import math
import PlotPres as pp


def plot():
    pp.start()
    
def pltagem():
    t = 0
    x = []

    y = []

    def fig():
        plt.plot(x,y)
        plt.grid()
    while True:
        t = t + 1
        x.append(t)
        y = x
        drawnow(fig)

def write():
	while True:
    		var = input('coloque uma letra: ')
    		print(var)

if __name__ == "__main__":
    tread_plot = threading.Thread(target=plot)
    tread_write = threading.Thread(target=write)
    tread_plot.start()
    tread_write.start()
