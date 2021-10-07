import tkinter as tk
from tkinter.constants import BOTH, BOTTOM, HORIZONTAL, RIGHT, S, VERTICAL, W, X, Y, YES
from PIL import ImageTk, Image
from tkinter import PhotoImage, Scrollbar, filedialog

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        #memory variable
        self.title('image loader')
        self.fileName = ''
        self.image = Image
        self.imageDisplay = PhotoImage

        self.geometry("500x350")

        #button control
        self.resizable(width = True, height = True)
        btn = tk.Button(self, text="control", width=10)
        btn.pack(anchor=tk.NW, padx=8, pady=10)
        btn.bind('<Button-3>', self.getMenuPopUp)

        #display image erea
        self.imageFrame = tk.Canvas(self, borderwidth=0, width=500, height=300)
        self.imageFrame.pack(anchor=tk.W, expand=YES, fill=BOTH)


    def getMenuPopUp(self, event):
        btnMenu = tk.Menu(self, tearoff=0)
        btnMenu.add_command(label='open', command=self.openImage)
        btnMenu.add_command(label='delete', command=self.deleteImage)
        btnMenu.add_separator()
        btnMenu.add_command(label='quit', command=self.quit)

        try:
            btnMenu.tk_popup(event.x_root, event.y_root)
        finally:
            btnMenu.grab_release()


    def openFileName(self):
        self.fileName = filedialog.askopenfilename(title='image need')


    def openImage(self):
        if len(self.fileName) > 0:
            return


        self.openFileName()
        self.image = Image.open(self.fileName)

        width,height=self.image.size

        self.imageDisplay = ImageTk.PhotoImage(self.image)
        self.imagetk = self.imageFrame.create_image(0,0, image=self.imageDisplay, anchor=tk.NW, tags='image')

        self.sbarV = Scrollbar(self.imageFrame, orient=VERTICAL)
        self.sbarH = Scrollbar(self.imageFrame, orient=HORIZONTAL)

        self.sbarV.config(command=self.imageFrame.yview)
        self.sbarH.config(command=self.imageFrame.xview)

        self.imageFrame.config(yscrollcommand=self.sbarV.set)
        self.imageFrame.config(xscrollcommand=self.sbarH.set)

        self.sbarV.pack(side=RIGHT, fill=Y)
        self.sbarH.pack(side=BOTTOM, fill=X)

        self.imageFrame.config(scrollregion=(0,0,width,height))


    def deleteImage(self):
        self.fileName = ''
        self.imageFrame.delete('image')
        self.sbarH.destroy()
        self.sbarV.destroy()


    def quit(self):
        self.destroy()



if __name__ == "__main__":
    app = App()
    app.mainloop()