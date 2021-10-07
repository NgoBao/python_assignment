import tkinter as tk
from tkinter.constants import BOTH, DISABLED, LEFT, NORMAL, RIDGE, RIGHT, S, YES
from math import sin, cos, radians

class  App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title('The timer')
        self.switch = 0
        self.angle = 0
        self.pending = 0
        self.circleParameter = []
        self.xCoord = 0
        self.yCoord = 0
        self.radius = 0
        
        # the display area
        groupDisplay = tk.LabelFrame(self, relief=RIDGE, padx=10, pady=8)
        groupDisplay.pack(side=LEFT, pady=10, padx=8)

        self.areaDisplay = tk.Canvas(groupDisplay, width=300, height=300, bd=0, highlightthickness=0)
        self.areaDisplay.pack(expand=YES, fill=BOTH)
        self.createCircleParameters(150, 150, 130)
        self.areaDisplay.create_oval(
            self.circleParameter[0], 
            self.circleParameter[1], 
            self.circleParameter[2], 
            self.circleParameter[3], 
            outline="#4D7C8A"
        )
    
        self.point = self.areaDisplay.create_oval(
            self.xCoord + self.radius * cos(radians(0)) - 5,
            self.yCoord + self.radius * sin(radians(0)) - 5,
            self.xCoord + self.radius * cos(radians(0)) + 5,
            self.yCoord + self.radius * sin(radians(0)) + 5,
            fill="red",
            tags="default"
        )

        # the 2 control button
        groupButton = tk.LabelFrame(self, borderwidth=0, padx=10, pady=8)
        groupButton.pack(side=RIGHT, anchor=tk.N)

        self.startBtn = tk.Button(groupButton, text='start', width=8, padx=10, pady=0,command=self.move)
        self.startBtn.grid(row=0, column=1, padx=8, pady=10, sticky=tk.W)
        tk.Button(groupButton, text='pause', width=8, padx=10, pady=0,command=self.pause).grid(row=1, column=1, padx=8, pady=10, sticky=tk.W)


    def createCircleParameters(self, xCoord, yCoord, radius):
        self.xCoord = xCoord
        self.yCoord = yCoord
        self.radius = radius
        x0 = xCoord - radius
        y0 = yCoord - radius
        x1 = xCoord + radius
        y1 = yCoord + radius
        self.circleParameter = [x0, y0, x1, y1]


    def move(self):
        self.startBtn['state'] = DISABLED
        if self.angle >= 360:
            self.angle = 0
        self.angle = self.angle + 1
        self.areaDisplay.coords(
            self.point,
            self.xCoord + self.radius * cos(radians(self.angle)) - 5,
            self.yCoord + self.radius * sin(radians(self.angle)) - 5,
            self.xCoord + self.radius * cos(radians(self.angle)) + 5,
            self.yCoord + self.radius * sin(radians(self.angle)) + 5,
        )
        self.switch = self.after(12, self.move)


    def pause(self):
        self.after_cancel(self.switch)
        self.startBtn['state'] = NORMAL




if __name__ == "__main__":
    app = App()
    app.mainloop()