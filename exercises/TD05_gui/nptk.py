from tkinter import *

CANVAS_WIDTH, CANVAS_HEIGHT = 600, 1000

root = Tk()
canvas = Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT)

# Début de votre code
x0 = 200
x1 = CANVAS_WIDTH - 200   
y = CANVAS_HEIGHT - 200
canvas.create_oval(x0 - 80, y + 80, x0 + 80, y - 80)
canvas.create_oval(x1 - 80, y + 80, x1 + 80, y - 80)
canvas.create_oval((x0 + x1) / 2 - 50, y + 50, (x0 + x1) / 2 + 50, 200)
canvas.pack()
root.mainloop()