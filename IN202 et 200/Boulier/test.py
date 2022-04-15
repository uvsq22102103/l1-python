import tkinter as tk

DIM_BOULIER = (17,9)
WITDH = 1300
HEIGHT = 700
ecart_width = WITDH/DIM_BOULIER[0]
ecart_height = HEIGHT/DIM_BOULIER[1]

def Start():
    pass

def clic(event):
    x, y = event.x, event.y
    print("Clic en",x,",",y)
    print(canvas1.find_closest(x,y)," est l'objet cliqué.")


racine=tk.Tk()
racine.title("Projet Boulier")

canvas1 = tk.Canvas(racine, width=WITDH, height=HEIGHT, bg="black", borderwidth=4 )

#Création des boules

for x in range(DIM_BOULIER[0]):
    for y in range(DIM_BOULIER[1]):
        if 2 <= y <= 4:
            canvas1.create_oval(x*ecart_width,y*ecart_height,x*ecart_width+ecart_width,y*ecart_height+ecart_height,fill="gray",tags="boules")
        else:
            canvas1.create_oval(x*ecart_width,y*ecart_height,x*ecart_width+ecart_width,y*ecart_height+ecart_height,fill="red",tags="boules")

button1 = tk.Button(racine, text="start", bg="red", command = Start)

canvas1.grid(column=1, row=1, rowspan=9, columnspan=17)
button1.grid(column=0, row=0)
canvas1.tag_bind("boules","<Button-1>",clic)

racine.mainloop()