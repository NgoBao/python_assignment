import tkinter as tk


class App(tk.Tk):
    sum = 0
    context = ''

    def __init__(self):
        super().__init__()
        self.title("Read file")


        openBtn = tk.Button( 
            self, 
            text='open', 
            width=10, 
            command=self.openFile
        )    
        openBtn.pack(pady=10, padx=10, anchor=tk.W)


        self.displayFrame = tk.LabelFrame(
            self,
            padx=10,
            pady=10,
            width=300,
            height=200
        )
        self.displayFrame.pack(pady=5, padx=10)




        self.groupButton = tk.LabelFrame(self, padx=5, pady=5)
        self.groupButton.pack(pady=5, padx=5)
        submitBtn = tk.Button(
            self.groupButton,
            text='submit',
            command=self.calc,
            width=10
        )
        submitBtn.grid(column=1, row=0, padx=5)

        saveBtn = tk.Button(
            self.groupButton,
            text='save',
            command=self.save,
            width=10
        )
        saveBtn.grid(column=3, row=0, padx=5)

        self.resultLabel = tk.Label(
            self.groupButton,
            text=self.sum,
            width=10
        )
        self.resultLabel.grid(column=2, row=0, padx=5)


    def save(self):
        f = open(r"C:\Users\ADMIN\Desktop\python\practice\data.txt", "a")
        f.write(f'tong la: {self.sum}')
        f.close()


    def openFile(self):
        f = open(r"C:\Users\ADMIN\Desktop\python\practice\data.txt")
        self.context = f.read()
        f.close()

        tk.Label(
            self.displayFrame, 
            text=self.context,
            width=18,
            font=('Calibri', 20),
        ).grid(
            row=1,
            column=1,
        )


    def calc(self): 
        f = open(r"C:\Users\ADMIN\Desktop\python\practice\data.txt")
        f.readline()
        rawData = f.read().split('\n')
        f.close()
        data = []
    
        for subArr in rawData: 
            [data.append(value) for value in subArr.split(' ')]
        
        for value in data:
            if (value != ''):
                self.sum = self.sum + float(value)

        self.resultLabel = tk.Label(
            self.groupButton,
            text=self.sum,
            width=10
        )
        self.resultLabel.grid(column=2, row=0, padx=5)


if __name__ == '__main__':
    app = App()
    app.mainloop()













