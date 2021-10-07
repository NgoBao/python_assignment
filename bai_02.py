import tkinter as tk
import math
from tkinter import messagebox as msg
from tkinter.constants import LEFT, RIDGE, RIGHT

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Solve function')
        self.varA = tk.StringVar(value='')
        self.varB = tk.StringVar(value='')
        self.varC = tk.StringVar(value='')
        self.result = ''


        # form submit
        entryFunction_group = tk.LabelFrame(
                                    self, 
                                    padx=15, 
                                    pady=10, 
                                    text='function: ')
        entryFunction_group.pack(pady=5, padx=10)

        tk.Label(entryFunction_group, text='variable a ').grid(row=0, column=1)        
        tk.Label(entryFunction_group, text='variable b ').grid(row=1, column=1)
        tk.Label(entryFunction_group, text='variable c ').grid(row=2, column=1)        
        tk.Entry(entryFunction_group, textvariable=self.varA).grid(row=0, column=2, sticky=tk.W)        
        tk.Entry(entryFunction_group, textvariable=self.varB).grid(row=1, column=2, sticky=tk.W)
        tk.Entry(entryFunction_group, textvariable=self.varC).grid(row=2, column=2, sticky=tk.W)


        #handling result
        self.entryResult_group = tk.LabelFrame(
                                    self, 
                                    padx=15, 
                                    pady=10, 
                                    width=100,
                                    text='Result: ')

        self.entryResult_group.pack(pady=5, padx=10)
        self.result = tk.Label(self.entryResult_group, text="").grid(row=0, column=1, sticky=tk.EW)
        tk.Button(self, text='submit', width=10, command= self.solveFunc).pack(padx=10, pady=10, side=LEFT)
        tk.Button(self, text='reset', width=10, command= self.resetFunc).pack(padx=10, pady=10, side=RIGHT)



        #exit part
        btn_thoat = tk.Button(self, text='thoat', width=10, command=self.btn_thoat_click).pack(padx=10, pady=10, side= LEFT)
        self.protocol('WN_DELETE_WINDOW', self.btn_thoat_click)


    def btn_thoat_click(self):
        tra_loi = msg.askquestion(message='Do u wanna exit ?')
        if tra_loi == 'yes': 
            self.destroy()


    def resetFunc(self): 
        self.varA = tk.StringVar(value='')
        self.varB = tk.StringVar(value='')
        self.varC = tk.StringVar(value='')
        

    def solveFunc(self): 
        try: 
            a = float(self.varA.get())
            b = float(self.varB.get())
            c = float(self.varC.get())

            delta = b ** 2 - 4 * a * c
            if delta < 0: 
                self.result = tk.Label(self.entryResult_group, text="the function has none solution").grid(row=0, column=1, sticky=tk.EW)
                return

            if delta == 0:
                self.result = tk.Label(self.entryResult_group, text=f'the function has only 1 solution: {-0.5* b / a}').grid(row=0, column=1, sticky=tk.EW)
                return
            else:
                x = math.sqrt(delta)
                self.result = tk.Label(self.entryResult_group, text=f'the function has 2 solution: {(- b + x) / (2 * a )} and {(- b - x) / (2 * a )}').grid(row=0, column=1, sticky=tk.EW)
                return

        except:
            self.result = tk.Label(self.entryResult_group, text=f'wrong entries, plese write it again').grid(row=0, column=1, sticky=tk.EW)
            return


if __name__ == "__main__":
    app = App()
    app.mainloop()