
import tkinter as tk
from tkinter.constants import BOTTOM, END, LEFT, RIDGE, RIGHT, TOP, VERTICAL, W, Y
from tkinter import  Scrollbar, filedialog


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('handling ggfile')
        self.allStudent = []

        tk.Button(self, text="open file", command=self.openFile).grid(row=0, column=1, padx=8, pady=5, sticky=W)
        self.listA = tk.Listbox(self, relief=RIDGE, width=50, height=30)
        self.listA.grid(row=1, column=1, padx=8, pady=5, sticky=W)

        tk.Button(self, text="handling", command=self.handling).grid(row=0, column=2, padx=8, pady=5, sticky=W)
        self.listB = tk.Listbox(self, relief=RIDGE, width=50, height=30)
        self.listB.grid(row=1, column=2, padx=8, pady=5, sticky=W)


    def openFile(self):
        # open file
        file = filedialog.askopenfile(mode='rb')
        wholeData = str(file.read())

        # handle data
        dataHandle = wholeData.split(": ")
        dataHandle.pop()
        for perStudent in dataHandle:
            self.listA.insert(END, perStudent.split('\\n')[len(perStudent.split('\\n')) - 2])
            self.listA.insert(END, perStudent.split('\\n')[len(perStudent.split('\\n')) - 1])
            self.listA.insert(END, perStudent.split('\\n')[len(perStudent.split('\\n')) - 4])
            self.listA.insert(END, '')
            self.allStudent.append(perStudent.split('\\n')[len(perStudent.split('\\n')) - 1])

        

    def handling(self):
        uniqueList = []

        for perStudent in self.allStudent:
            if perStudent not in uniqueList:
                uniqueList.append(perStudent)  
        
        for perUniqueStudent in uniqueList:
            self.listB.insert(END, perUniqueStudent)
        
        self.listB.insert(END, f'the total is: {len(uniqueList)}')
        

        
        





if __name__ == "__main__":
    app = App()
    app.mainloop()