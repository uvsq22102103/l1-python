import tkinter as tk

dimension = 500
square = 100

nb_clics = 0
nc = 0
def draw_clic(event):
    global nb_clics,nc
    if dimension/2-square < event.x < dimension/2+square and dimension/2-square < event.y < dimension/2+square:
        if nc == 0:
            canvas.create_rectangle(dimension/2+square,dimension/2+square,dimension/2-square,dimension/2-square,fill='white')
            nb_clics += 1
            nc += 1
            if nb_clics >= 10:
                root.destroy()
        else:
            if nb_clics >= 10:
                root.destroy()
            canvas.create_rectangle(dimension/2+square,dimension/2+square,dimension/2-square,dimension/2-square,fill='black')
            nb_clics += 1
            nc = 0
    

root = tk.Tk()
canvas = tk.Canvas(root,height=dimension,width=dimension,bg='black')
canvas.bind("<Button-1>", draw_clic)
canvas.create_rectangle(dimension/2+square+3,dimension/2+square+3,dimension/2-(square+3),dimension/2-(square+3),fill='white',)
canvas.create_rectangle(dimension/2+square,dimension/2+square,dimension/2-square,dimension/2-square,fill='black',)
canvas.grid(row=0,column=0)
tk.mainloop()