import tkinter as tk
from tkinter.constants import CURRENT, LEFT, RIGHT, S

class App(tk.Tk):
    currentList = []
    def __init__(self):
        super().__init__()
        self.title("Danh sach trai cay")
        self.currentInput = tk.StringVar()
        self.currentPickedElement = []
        self.countDeleted = 0

        #line 1 INPUT
        groupInput = tk.LabelFrame(self, borderwidth=0)
        groupInput.pack()
        tk.Label(groupInput, text="Trai cay", padx=8, pady=10).grid(row=0, column=1, sticky=tk.W)
        tk.Entry(groupInput, textvariable=self.currentInput, width=60).grid(row=0, column=2, padx=8, columnspan=2)
        tk.Button(groupInput, text='add', padx=10, pady=0,command=self.addToCurrentListed).grid(row=0, column=4, padx=8, pady=10, sticky=tk.W)

        #line 2 DISPLAY
        groupDisplay = tk.LabelFrame(self, borderwidth=0, padx=10, pady=8)
        groupDisplay.pack(fill=tk.BOTH)

        self.displayCurrentList = tk.LabelFrame(groupDisplay, background='white', height=150)
        self.displayCurrentList.pack(side=LEFT, expand=1, fill=tk.BOTH)

        tk.Label(groupDisplay, width=8, height=10).pack(side=LEFT)

        self.displayList = tk.LabelFrame(groupDisplay, background='white', height=150)
        self.displayList.pack(side=RIGHT, expand=1, fill=tk.BOTH)
        
        #line 3 Count
        self.groupCount = tk.LabelFrame(self, borderwidth=0, padx=10, pady=8)
        self.groupCount.pack(side=LEFT)
        tk.Label(self.groupCount, text='So luong').pack(side=LEFT)
        self.count = tk.Label(self.groupCount, text=len(self.currentList), padx=10)
        self.count.pack(side=LEFT)


    def addToCurrentListed(self):
        index = len(self.currentList)
        btn = tk.Button(
            self.displayCurrentList, 
            background="white", 
            text=self.currentInput.get(), 
            borderwidth=0,
            command=lambda: self.mutiplePick(btn, index)
        )
        btn.pack(fill=tk.X)
        btn.bind('<Button-3>', lambda event : self.getPopUp(event, index))
        self.currentList.append([self.currentInput.get(), btn])
        self.getCount() 


    def getPopUp(self ,event, i):
        btnMenu = tk.Menu(self, tearoff=0)
        btnMenu.add_command(label='copy to right', command = lambda: self.copyToRight(i))        
        btnMenu.add_command(label='move to right', command = lambda: self.moveToRight(i))        
        btnMenu.add_command(label='delete', command = lambda: self.delete(i))

        try: 
            btnMenu.tk_popup(event.x_root, event.y_root)
        finally: 
            btnMenu.grab_release()


    def mutiplePick(self, btn, index):
        btn.config(background="#003D5B", fg="white")
        self.currentPickedElement.append(index)


    def copyToRight(self, i): 
        #picked element
        if len(self.currentPickedElement) > 0:
            for index in self.currentPickedElement:
                data = self.currentList[index][0]
                btn = tk.Button(
                    self.displayList, 
                    background="white", 
                    text=data, 
                    borderwidth=0,
                )
                btn.pack(fill=tk.X)
            self.clearPick()
            return
        #default
        data = self.currentList[i][0]
        btn = tk.Button(
            self.displayList, 
            background="white", 
            text=data, 
            borderwidth=0,
        )
        btn.pack(fill=tk.X)


    def moveToRight(self, i): 
        # picked element
        if len(self.currentPickedElement) > 0:
            for index in self.currentPickedElement:
                data = self.currentList[index][0]
                btn = tk.Button(
                    self.displayList, 
                    background="white", 
                    text=data, 
                    borderwidth=0,
                )
                btn.pack(fill=tk.X)
            
            for index in self.currentPickedElement:
                self.currentList[index][1].destroy()
                self.countDeleted = self.countDeleted + 1

            self.currentPickedElement = []
            return

        #Default
        self.copyToRight(i)
        self.delete(i)


    def delete(self, i): 
        #picked elements
        if len(self.currentPickedElement) > 0:
            for index in self.currentPickedElement:
                self.currentList[index][1].destroy()
                self.countDeleted = self.countDeleted + 1
            self.getCount()
            return
        #default
        self.currentList[i][1].destroy()
        self.countDeleted = self.countDeleted + 1   
        self.getCount()


    def getCount(self):
        self.count.config(text=len(self.currentList) - self.countDeleted)


    def clearPick(self):
        for index in self.currentPickedElement:
            btn = self.currentList[index][1]
            btn.config(background='white', fg='black')
        self.currentPickedElement = []


if __name__ == "__main__":
    app = App()
    app.mainloop()