import tkinter as tk
from tkcalendar import DateEntry


class App(tk.Tk):
    data = []
    currentPeiceDate = {
        "fullName": '',
        "dateOfBirth": '',
        "gender": '',
        "grade": 0,
    }

    def __init__(self):
        super().__init__()
        self.title('Result table')
        self.gradeS = 0
        self.fullName = tk.StringVar()
        self.dateOfBirth = ''
        self.gender = '0'
        self.grade = tk.DoubleVar()

        # field
        tk.Label(self, text="Ho Ten", padx=8, pady=10).grid(row=0, column=1, sticky=tk.W)
        tk.Label(self, text="Ngay Sinh", padx=8, pady=10).grid(row=1, column=1, sticky=tk.W)
        tk.Label(self, text="Gioi Tinh", padx=8, pady=10).grid(row=2, column=1, sticky=tk.W)
        tk.Label(self, text="Diem", padx=8, pady=10).grid(row=3, column=1, sticky=tk.W)


        #input for fields
        #fullname
        tk.Entry(self, textvariable=self.fullName, width=40).grid(row=0, column=2, padx=8, columnspan=2,sticky=tk.W)
        #date of birth
        self.dateOfBirth = DateEntry(self, width= 16, background= "magenta3", foreground= "white", bd=2)
        self.dateOfBirth.grid(row=1, column=2, padx=8, sticky=tk.W)
        #set gender
        self.varStringGender = tk.StringVar()
        checkGender = tk.Checkbutton(self, textvariable='0', variable=self.varStringGender, command=self.setGender)
        checkGender.grid(row=2, column=2, padx=2.5, sticky=tk.W)
        #get grade
        tk.Entry(self, textvariable=self.grade, width=10).grid(row=3, column=2, padx=8, sticky=tk.W)


        #add user button
        tk.Button(self, text='add', padx=10, pady=0,command=self.add).grid(row=0, column=4, padx=8, pady=10, sticky=tk.W)


        #display board
        tk.Label(self, text='Danh sach').grid(row=4, column=1, padx=8, pady=10,sticky=tk.W)
        bgFrame = tk.LabelFrame(self, width=500, height=200, border=0, background='white')
        bgFrame.grid(row=5, column=1, columnspan=4, padx=8, pady=5, sticky=tk.W)
        self.displayFrame = tk.LabelFrame(self, border=0, background='white')
        self.displayFrame.grid(row=5, column=1, columnspan=4, padx=8, pady=5, sticky=tk.NW)

        #count
        tk.Button(self, text='So Luong', padx=10, pady=0, command=self.count).grid(row=6, column=1, padx=8, pady=10, sticky=tk.W)

        #average
        tk.Button(self, text='Trung Binh', padx=10, pady=0, command=self.average).grid(row=6, column=3, padx=8, pady=10, sticky=tk.W)

    def setGender(self):
        self.gender = self.varStringGender.get()


    def add(self):
        if self.fullName.get() == '':
            return

        #create new user
        self.currentPeiceDate["fullName"] = self.fullName.get()
        self.currentPeiceDate["dateOfBirth"] = self.dateOfBirth.get_date()
        self.currentPeiceDate["gender"] = self.gender
        self.currentPeiceDate["grade"] = self.grade.get()
        self.gradeS = self.gradeS + float(self.grade.get())
        #add to the display data
        self.data.append(self.currentPeiceDate)
        self.display()


    def count(self):
        i = len(self.data)
        
        self.countLabel = tk.Label(self, text=f'{i}', padx=8, pady=10).grid(row=6, column=2, sticky=tk.W)
        return


    def average(self):    
        i = len(self.data)
        self.countLabel = tk.Label(self, text=f'{self.gradeS / i}', padx=8, pady=10).grid(row=6, column=4, sticky=tk.W)


    def display(self):
        gender ="nam"
        if self.data[len(self.data) - 1]['gender'] == '1':
            gender = 'nu'
        row = 9 + len(self.data) -1
        tk.Label(self.displayFrame, text=self.data[len(self.data) - 1]['fullName'], background='white', padx=4, pady=4, font=('Calibri', 12)).grid(row=row, column=1, sticky=tk.W)
        tk.Label(self.displayFrame, text=self.data[len(self.data) - 1]['dateOfBirth'], background='white', padx=4, pady=4, font=('Calibri', 12)).grid(row=row, column=2, sticky=tk.W)
        tk.Label(self.displayFrame, text=gender, background='white', padx=4, pady=4, font=('Calibri', 12)).grid(row=row, column=3, sticky=tk.W)
        tk.Label(self.displayFrame, text=self.data[len(self.data) - 1]['grade'], background='white', padx=4, pady=4, font=('Calibri', 12)).grid(row=row, column=4, sticky=tk.W)


if __name__ == '__main__':
    app = App()
    app.mainloop()