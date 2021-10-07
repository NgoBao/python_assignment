import tkinter as tk
import os
from tkinter.constants import RIDGE, S

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("open directory")
        self.path = tk.StringVar()

        tk.Label(self, text="Folder path", padx=10, pady=10).grid(row=0, column=1, sticky=tk.W)
        tk.Entry(self, width=30, textvariable=self.path).grid(row=0, column=2, sticky=tk.W)
        tk.Button(self, width=10, pady=0, text='display', command=self.openDir).grid(row=0, column=3, pady=10, padx=10, sticky=tk.W)

        bgFrame = tk.LabelFrame(self, height=200, border=0, background="white", highlightthickness=0)
        bgFrame.grid(row=1, column=1, columnspan=4, padx=8, pady=5, sticky=tk.W)
    
    
    def openDir(self):
        dirNameListFile = os.listdir(self.path.get())
        self.displayFrame = tk.LabelFrame(self, borderwidth=0, highlightthickness=0)
        self.displayFrame.grid(row=1, column=1, columnspan=4, padx=8, pady=5, sticky=tk.NW)
        i = 0
        for file in dirNameListFile:
            size = str("{:.2f}".format(os.path.getsize(self.path.get() + '/' + file) / 1024)) + "KB"
            nameType = file.split('.')[1]
            nameFile = self.path.get() + f'\{file.split(".")[0]}' 
            tk.Label(self.displayFrame, text=nameFile, highlightthickness=0).grid(row=i, column=1, columnspan=2, padx=8, pady=8)
            tk.Label(self.displayFrame, text=size, highlightthickness=0, width=10).grid(row=i, column=3, padx=8, pady=8)
            tk.Label(self.displayFrame, text=nameType, highlightthickness=0, width=10).grid(row=i, column=4, padx=8, pady=8)
            i = i + 1



if __name__ == "__main__":
    app = App()
    app.mainloop()