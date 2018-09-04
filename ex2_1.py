"""
Created on Wed Sep 5 23:11:29 2018

@author: litingyi
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from matplotlib.widgets import Slider

class ButtonHandler:
    def __init__(self):
        self.flag = True
        self.range_s, self.range_e, self.range_step = 0, 1, 0.01
        plt.close()
        fig = plt.figure()
        self.ax = fig.add_subplot(1, 1, 1)
        plt.subplots_adjust(left=0.25, bottom=0.25)
        plt.grid(True)
        plt.ion()
        print('Simulation')

        axprev = plt.axes([0.61, 0.01, 0.1, 0.075])
        self.bprev = Button(axprev, 'Stop')
        self.bprev.on_clicked(self.Stop)
        axnext = plt.axes([0.7, 0.01, 0.1, 0.075])
        self.bnext = Button(axnext, 'Start')
        self.bnext.on_clicked(self.Start)
        axreset = plt.axes([0.79, 0.01, 0.1, 0.075])
        self.reset = Button(axreset, 'Reset')
        self.reset.on_clicked(self.Reset)

        axcolor = 'lightgoldenrodyellow'
        axfreq = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
        axamp = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)

        self.sfreq = Slider(axfreq, 'Freq', 0.1, 30.0, valinit=3)
        self.samp = Slider(axamp, 'Amp', 0.1, 10.0, valinit=5)


    def threadStart(self):
        while True:
            while self.flag:
                self.range_s += self.range_step
                self.range_e += self.range_step
                X = np.arange(self.range_s, self.range_e, self.range_step)
                Y = 3 * np.pi * np.exp(-5 * np.sin(2*np.pi*1*X))
                self.ax.plot(X, Y, 'r-')
                plt.pause(0.001)

            while not self.flag:
                plt.pause(0.1)


    def Start(self, event):
        self.flag= True

    def Stop(self, event):
        self.flag= False

    def Reset(self, event):
        plt.pause(0.1)
        self.__init__()

callback = ButtonHandler()
callback.threadStart()
plt.show()
