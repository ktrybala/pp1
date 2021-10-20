from tkinter import*
from PIL import ImageTk, Image

main = Tk()
main.geometry("400x400")
main.title('SKUTE BOBO')
icopath = r"/users/ktrybala/documents/bobo.ico"
main.iconbitmap(icopath)
main['bg']='pink'

frame_a = Frame()
frame_b = Frame()

def photo():
	global img
	path = r"/users/ktrybala/documents/bobo.png"
	img = ImageTk.PhotoImage(Image.open(path))
	panel = Label(main, image=img)
	panel.pack()

greeting = Label(text='matczak roku', bg='pink')

button = Button(
	master = frame_a, 
	text='skuter bejbe',
	highlightbackground='white',
	fg='black',
	command = photo)

button.pack()
frame_a.pack()
frame_b.pack()
greeting.pack()

main.mainloop()
