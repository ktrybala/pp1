from tkinter import *
from PIL import ImageTk, Image

main = Tk()

def open_img():
    global img
    path = r"/users/ktrybala/documents/bobo.png"
    img = ImageTk.PhotoImage(Image.open(path))
    panel = Label(main, image = img)
    panel.pack()

but1 = Button(main, text="click to get the image", command=open_img)
but1.pack()
main.mainloop()