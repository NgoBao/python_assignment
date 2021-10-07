import tkinter as tk
from tkinter.constants import BOTH, INSIDE, PROJECTING, RIDGE, S, SUNKEN, Y, YES
from tkinter.ttk import tclobjs_to_py

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('the passing right form to draw a circle')
        
        #default radius
        self.radius = tk.DoubleVar()
        self.radius.set(0)

        # entry form and button draw
        tk.Label(self, text='Radius').grid(row=0, column=1, padx=8, pady=10, sticky=tk.W)
        tk.Entry(self, width=13, textvariable=self.radius).grid(row=0, column=2, padx=8, pady=10, sticky=tk.W)
        tk.Button(self, text='draw', width=10, command=self.openAnotherWindow).grid(row=1, column=2, padx=8, pady=10)


    def openAnotherWindow(self):
        #func exit the new window
        def quitNewOne():
            newOne.destroy()

        #create new window
        newOne = tk.Toplevel(self)
        painterWidthSquare = self.defineCirleParameters()

        #setting and the circle
        newOne.title('Circle')
        painter = tk.Canvas(newOne, width=painterWidthSquare, height=painterWidthSquare , relief=SUNKEN, borderwidth=2, highlightthickness=0)
        painter.pack(expand=YES, fill=BOTH, pady=8, padx=8)
        painter.create_oval(40, 40, painterWidthSquare - 40, painterWidthSquare - 40,fill="#A2A392", outline='')
        
        #button exit the new one
        tk.Button(newOne, text="close", width=10, command=quitNewOne).pack(pady=8, padx=8)


    def defineCirleParameters(self):
        painterWidthSquare = self.radius.get() * 2 + 80
        return painterWidthSquare


if __name__ == '__main__':
    app = App()
    app.mainloop()