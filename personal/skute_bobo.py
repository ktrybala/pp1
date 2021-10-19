import io
import tkinter as tk
from PIL import ImageTk, Image
main = tk.Tk()
main.geometry("200x80")
main.title('SKUTE BOBO')
main['bg']='pink'

def photo():
	#image = Image.open(r"/Users/ktrybala/documents/bobo.png")
	#image = image.resize("200x200")
	#img = ImageTk.PhotoImage(image)
	img = Image.open(r"/Users/ktrybala/documents/bobo.png")
	img.show()
button = tk.Button(main, text='skuter bejbe', highlightbackground='white', fg='black', command=photo)
button.pack()

main.mainloop()
