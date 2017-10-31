from tkinter import Tk, Button, Canvas, colorchooser

tk = Tk()

color = 'red'
def choose_color():
    global color
    color = colorchooser.askcolor()[1]

btn = Button(tk, text="color", command=choose_color)
btn.pack()

canvas = Canvas(tk, width=500, height=500, background='white')
canvas.pack()

current_coordinates = 0, 0

def mousedown(event):
    global current_coordinates
    current_coordinates = event.x, event.y

def mousemove(event):
    global current_coordinates
    print(event.x, event.y)
    canvas.create_line(
        current_coordinates[0], current_coordinates[1], 
        event.x, event.y,
        fill=color
    )
    current_coordinates = event.x, event.y


canvas.bind('<B1-Motion>', mousemove)
canvas.bind('<Button-1>', mousedown)

tk.mainloop()
