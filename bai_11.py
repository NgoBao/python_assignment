import tkinter as tk
from tkinter.constants import BOTH, YES

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("mainform")
        self.radius = tk.DoubleVar()
        self.radius.set(0)

        self.painter = tk.Canvas(self, width=300, height=300, borderwidth=0, highlightthickness=0)
        self.painter.pack(padx=8, pady=10, expand=YES, fill=BOTH)

        tk.Button(self, text='add radius', width=10, command=self.openNewWindow).pack(pady=10, padx=8)


    def openNewWindow(self):

        self.newOne = tk.Toplevel(self)
        self.newOne.title("add radius")

        tk.Label(self.newOne, text='Radius').grid(row=0, column=1, padx=8, pady=10, sticky=tk.W)
        tk.Entry(self.newOne, width=13, textvariable=self.radius).grid(row=0, column=2, padx=8, pady=10, sticky=tk.W)
        tk.Button(self.newOne, text='draw', width=10, command=self.drawCircle).grid(row=1, column=2, padx=8, pady=10)


    def drawCircle(self):
        self.painter.delete('shape')
        self.newOne.destroy()
        painterWidthSquare = self.defineCirleParameters()
        self.painter.config(width=painterWidthSquare, height=painterWidthSquare)
        self.painter.create_oval(40, 40, painterWidthSquare - 40, painterWidthSquare - 40, fill="#A2A392", outline='', tags='shape')


    def defineCirleParameters(self):
        painterWidthSquare = self.radius.get() * 2 + 80
        print(painterWidthSquare)
        return painterWidthSquare


if __name__ == "__main__":
    app = App()
    app.mainloop()