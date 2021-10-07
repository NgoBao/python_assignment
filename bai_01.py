import tkinter as tk
from tkinter import messagebox as msg

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("bai thuc hanh dau tien")
        lbl_chao = tk.Label(self, text=['chao mung khoa CNTT'], 
                            bg='white', fg='blue', relief=tk.SUNKEN, font=('Calibri', 20))
        lbl_chao.grid(row=0, column=0, pady=10)

        btn_thoat = tk.Button(self, text='thoat', width=10, command=self.btn_thoat_click)
        lbl_chao.grid(row=0, column=0, padx= 10, pady=10)
        btn_thoat.grid(row=1, column=0, pady=10, padx=10)

        self.protocol('WN_DELETE_WINDOW', self.btn_thoat_click)


    def btn_thoat_click(self):
        tra_loi = msg.askquestion('Do u wanna exit ?')
        if tra_loi == 'yes': 
            self.destroy()



if __name__ == "__main__":
    app = App()
    app.mainloop()
