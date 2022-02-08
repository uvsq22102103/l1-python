import tkinter as tk

dimension = 500

def draw_clic(event):
    if event.x > 250:
        canvas.create_oval(event.x-5,event.y-5,event.x+5,event.y+5,fill='red')
    else:
        canvas.create_oval(event.x-5,event.y-5,event.x+5,event.y+5,fill='blue')

root = tk.Tk()
canvas = tk.Canvas(root,height=dimension,width=dimension,bg='black')
canvas.bind("<Button-1>", draw_clic)
canvas.create_line(dimension//2,0,dimension//2,dimension,fill='white')
canvas.grid(row=0,column=0)
tk.mainloop()