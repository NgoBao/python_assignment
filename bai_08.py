import tkinter as tk
from tkinter import  PhotoImage, filedialog
from tkinter.constants import BOTH, BOTTOM, LEFT, RIGHT, YES
from PIL import ImageTk, Image

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        #memory variable
        self.title('image loader')
        self.fileName = str
        self.image = Image
        self.imageSize = Image
        self.imageDisplay = PhotoImage

        #button control
        self.resizable(width = True, height = True)
        btn = tk.Button(self, text="control", width=10)
        btn.pack(anchor=tk.NW, padx=8, pady=10)
        btn.bind('<Button-3>', self.getMenuPopUp)

        #display image erea
        self.imageFrame = tk.Canvas(self, borderwidth=0, width=500, height=300)
        self.imageFrame.pack(anchor=tk.W, expand=YES, fill=BOTH)
        self.imageFrame.bind('<Configure>', self.resizer)
        
        #info image
        groupDisplayInfoImage = tk.LabelFrame(self, borderwidth=0, bd=0, highlightthickness=0)
        groupDisplayInfoImage.pack(anchor=tk.SW, expand=YES, fill=tk.X, padx=8)
        self.labelFileName = tk.Label(groupDisplayInfoImage ,text="file name", padx=8, pady=10)
        self.labelFileName.pack(side=LEFT)
        self.labelSize = tk.Label(groupDisplayInfoImage, text="size", pady=10, padx=8)
        self.labelSize.pack(side=RIGHT)


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
        self.openFileName()
        self.image = Image.open(self.fileName)
        width, hieght = self.image.size
        realSize = f'{width} x {hieght}'
        self.labelSize['text'] = realSize
        self.imageSize = self.image.resize((500, 300), Image.ANTIALIAS)
        self.imageDisplay = ImageTk.PhotoImage(self.imageSize)
        self.imagetk = self.imageFrame.create_image(0,0, image=self.imageDisplay, anchor=tk.NW, tags='image')
        self.labelFileName['text'] = self.fileName


    def resizer(self, e):
        self.image = Image.open(self.fileName)
        self.imageSize = self.image.resize((e.width, e.height), Image.ANTIALIAS)
        self.imageDisplay = ImageTk.PhotoImage(self.imageSize)
        self.imageFrame.itemconfig(self.imagetk, image=self.imageDisplay)


    def deleteImage(self):
        self.imageFrame.delete('image')
        self.labelFileName['text'] = 'file name'
        self.labelSize['text'] = 'size'


    def quit(self):
        self.destroy()



if __name__ == "__main__":
    app = App()
    app.mainloop()

