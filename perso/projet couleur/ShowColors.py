import tkinter as tk

def Show(input):
    input = input.split()

    espacement = 500/len(input)

    root = tk.Tk()
    root.title('ShowColors -  V1')

    canvas = tk.Canvas(root,height=500,width=500,bg='white')
    canvas.grid()

    for i in range(len(input)):
        canvas.create_rectangle(espacement*i,0,espacement*(i+1),500,fill=input[i])

    root.mainloop()