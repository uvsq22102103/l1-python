import tkinter as tk

CANVAS_WIDTH, CANVAS_HEIGHT = 300, 600

root = tk.Tk()

canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT)

# Début de votre code
x = CANVAS_WIDTH / 2
y0 = 100
y1 = CANVAS_HEIGHT - 100
canvas.create_line(x, y0, x, y1)
canvas.create_oval(x - 100, y1 + 100, x + 100, y1 - 100)
canvas.create_oval(x - 100, y0 + 100, x + 100, y0 - 100)
canvas.create_oval( x - 100, (y1 + y0) / 2 + 100, x + 100, (y1 + y0) / 2 - 100)
    
# Fin de votre code

canvas.grid(row=0,column=0)
root.mainloop()
