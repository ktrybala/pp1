from tkinter import *

main = Tk()
main.geometry("500x500")
main.title('tak koń')

button = Button(main, text = 'exit', highlightbackground = 'red', fg='white', command = main.destroy)
button.place(relx=0.5, rely=0.01, anchor=N)
#button.pack()
user_input = StringVar(main)
text_x = Label(main, text = "Number x: ").place(relx = 0.15, rely= 0.5, anchor=W)
x = Entry(main, textvariable = user_input)
x.pack()
x.place(relx=0.5, rely=0.5, anchor=CENTER)
main.mainloop()
print(user_input.get())
