import tkinter as tk

dimension = 500

nb_clics = 0
point = (0,0)
def draw_clic(event):
    global nb_clics,point
    canvas.create_line(event.x,event.y,event.x+1,event.y,fill='white')
    nb_clics += 1
    if nb_clics == 2:
        nb_clics = 0
        if point[0] > 250:
            if event.x > 250:
                canvas.create_line(point[0],point[1],event.x,event.y,fill='blue')
            else:
                canvas.create_line(point[0],point[1],event.x,event.y,fill='red')
        else:
            if event.x < 250:
                canvas.create_line(point[0],point[1],event.x,event.y,fill='blue')
            else:
                canvas.create_line(point[0],point[1],event.x,event.y,fill='red')
    else:
        point = (event.x,event.y)

        

root = tk.Tk()
canvas = tk.Canvas(root,height=dimension,width=dimension,bg='black')
canvas.bind("<Button-1>", draw_clic)
canvas.create_line(dimension//2,0,dimension//2,dimension,fill='white')
canvas.grid(row=0,column=0)
tk.mainloop()