import tkinter as tk

dimension = 500
clic_list = []

def draw_circle(x,y):
    default_size = 25
    canvas.create_oval(x+default_size,y+default_size,x-default_size,y-default_size,fill='red')

def draw_clic(event):
    global clic_list
    draw_circle(event.x,event.y)
    clic_list.append((event.x,event.y))

    
    

root = tk.Tk()
canvas = tk.Canvas(root,height=dimension,width=dimension,bg='black')
canvas.bind("<Button-1>", draw_clic)
canvas.grid(row=0,column=0)
tk.mainloop()