"""
Created on Wed Sep 5 00:00:29 2018

@author: litingyi
"""
import numpy as np
import matplotlib.pyplot as plt
from threading import Thread
from matplotlib.widgets import Button
"""
class Hfunct:
    @staticmethod
    def plot(self):
        for i in range(0, 100):
            print(self.hfunction(x))

    @staticmethod
    def hfunction(t):
        return 3 * math.pi * math.exp(-5 * math.sin(2*math.pi*1*t))

a = Hfunct()
print(a.plot(a))
"""
class ButtonHandler:
    def __init__(self):
        self.flag = True
        self.range_s, self.range_e, self.range_step = 0, 1, 0.01
        plt.close()
        fig = plt.figure()
        self.ax = fig.add_subplot(1, 1, 1)
        plt.grid(True)
        plt.ion()
        print('Simulation')

        axprev = plt.axes([0.81, 0.05, 0.1, 0.075])
        self.bprev = Button(axprev, 'Stop')
        self.bprev.on_clicked(self.Stop)

        axnext = plt.axes([0.7, 0.05, 0.1, 0.075])
        self.bnext = Button(axnext, 'Start')
        self.bnext.on_clicked(self.Start)

    def threadStart(self):
        while self.flag:
            self.range_s += self.range_step
            self.range_e += self.range_step
            X = np.arange(self.range_s, self.range_e, self.range_step)
            Y = 3 * np.pi * np.exp(-5 * np.sin(2*np.pi*1*X))
            self.ax.plot(X, Y, 'r+')
            plt.pause(0.001)
            self.bprev.on_clicked(self.Stop)
            self.bnext.on_clicked(self.Start)

    def threadStop(self):
        while not self.flag:
            plt.pause()
            self.bprev.on_clicked(self.Stop)
            self.bnext.on_clicked(self.Start)

    def Start(self, event):
        self.flag = True
        t = Thread(target=self.threadStart)
        t.start()

    def Stop(self, event):
        self.flag = False
        t = Thread(target=self.threadStop)

callback = ButtonHandler()
callback.threadStart()
plt.show()
