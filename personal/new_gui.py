from tkinter import *

main = Tk()
main.geometry("500x500")
main.title('tak koń')

frame = Frame(main)
frame.pack()
frame_b = Frame(main).pack()
button = Button(frame, text = 'exit', highlightbackground = 'red', fg='white', command = main.destroy)
button.pack()
#button.place(relx=0.5, rely=0.01, anchor=N)

def output():
	output = user_input.get()
	label = Label(frame_b, text = output).pack(side = TOP)

button2 = Button(frame_b, text = 'show', highlightbackground = 'pink', fg = 'blue', command = output).pack()
user_input = StringVar(main)
text_x = Label(frame, text = "Number x: ")#.place(relx = 0.15, rely= 0.5, anchor=W)
x = Entry(frame, textvariable = user_input)
text_x.pack(side = LEFT)
x.pack(side = LEFT)
#x.place(relx=0.5, rely=0.5, anchor=CENTER)
output()
main.mainloop()
print(user_input.get())
