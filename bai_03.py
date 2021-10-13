import tkinter as tk
from tkinter.constants import BOTH, LEFT, RIGHT, S, YES

class App(tk.Tk):
    shapes = ('circle', 'triangle', 'rectangle')
    colorNames = ('red', 'green', 'blue')
    colorCode = {
        '111': 'white',
        '010': 'green',
        '110': 'yellow',
        '100': 'red',
        '000': 'black',
        '011': '#00FFFF',
        '001': 'blue',
        '101': '#FF00FF'
    }

    def __init__(self): 
        super().__init__()
        self.title('shape and color')
        self.currentColor = '000'


        # radio group button (shape)
        self.varStringShape = tk.StringVar()
        self.varStringShape.set(self.shapes[0])
        self.labelFrameShape = tk.LabelFrame(self, text='shapes')
        self.labelFrameShape.pack(side=RIGHT, padx=10, pady=10)
        for shape in self.shapes: 
            radioOne = tk.Radiobutton(self.labelFrameShape, 
                                        text=shape,
                                        value=shape,
                                        variable=self.varStringShape,
                                        command=self.reShape,
                                        padx=10,
                                        pady=10)
            radioOne.pack(anchor=tk.W)


        #checkbox group button (colors name)
        self.varStringColor = [tk.StringVar(), tk.StringVar(), tk.StringVar()]
        self.labelFrameColor = tk.LabelFrame(self, text='colors')
        self.labelFrameColor.pack(side=RIGHT, padx=10, pady=10)
        for index, value in enumerate(self.colorNames):
            radioOne = tk.Checkbutton(self.labelFrameColor,
                                        text=value,
                                        variable=self.varStringColor[index],
                                        command=self.reColor)
            radioOne.pack(anchor=tk.W)


        #shape display
        self.labelFrameDisplay = tk.LabelFrame(self, text='display')
        self.labelFrameDisplay.pack(side=LEFT, padx=10, pady=10)
        self.canvas = tk.Canvas(self.labelFrameDisplay, width=300, height=300, bd=0, highlightthickness=0)
        self.getShape()


    def reColor(self):
        codeColor = ''
        for code in self.varStringColor:
            if (code.get() == ''):
                codeColor = codeColor + '0'
            else: 
                codeColor = codeColor + code.get()

        self.currentColor = codeColor
        self.reShape()


    def getShape(self):
        self.canvas.pack(expand=YES, fill=BOTH)
        if (self.varStringShape.get() == 'circle'): 
            self.canvas.create_oval(10, 10, 290, 290, fill=self.colorCode[self.currentColor], outline=self.colorCode[self.currentColor],tags='shape')
        
        elif (self.varStringShape.get() == 'triangle'): 
            self.canvas.create_rectangle(10, 10, 290, 290, fill=self.colorCode[self.currentColor], outline=self.colorCode[self.currentColor], tags='shape')
        
        else:
            self.canvas.create_polygon((0, 290, 150, 0, 290, 290), fill=self.colorCode[self.currentColor], outline=self.colorCode[self.currentColor], tags='shape')


    def reShape(self):
        self.canvas.delete('shape')
        self.getShape()


if __name__ == "__main__":
    app = App()
    app.mainloop()
