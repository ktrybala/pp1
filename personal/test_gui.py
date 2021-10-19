import tkinter as tk

main = tk.Tk()
main.geometry("200x200")
main.title('Testing GUI programs')
main['bg']='#D8DCFF'

button = tk.Button(main, width=10, height=5, text='Bye', highlightbackground="green", fg="#565676", command=main.destroy)
button.pack()
main.mainloop()