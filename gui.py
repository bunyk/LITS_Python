from tkinter import *

tk = Tk()

btn = Button(tk, text="yo!")
btn.pack()

canvas = Canvas(tk, width=500, height=500)
canvas.pack()
canvas.create_line(0, 0, 500, 500)

tk.mainloop()
