import tkinter as tk


def decalage(lettre_message,lettre_cle):
    return chr((ord(lettre_message) + ord(lettre_cle)) % 256)

def rev_decalage(lettre_message,lettre_cle):
    return chr((ord(lettre_message)+(256-ord(lettre_cle))) % 256)


def chif_texte():
    texte, cle = msg.get(), key.get()
    if len(texte) == 0 or len(cle) == 0:
        result.set("\Erreur/")
    else:
        s = ""
        for i in range(len(texte)):
            s += decalage(texte[i],cle[i%len(cle)])
        result.set(s)


def dechif_text():
    texte, cle = msg.get(), key.get()
    if len(texte) == 0 or len(cle) == 0:
        result.set("\Erreur/")
    else:
        s = ""
        for i in range(len(texte)):
            s += rev_decalage(texte[i],cle[i%len(cle)])
        result.set(s)


root = tk.Tk()
root.title("Chiffrage basique par clé")

key = tk.StringVar(value="clée")
msg = tk.StringVar(value="message")
result = tk.StringVar()

button_chiffrage = tk.Button(root,text="Chiffrage",command=chif_texte)
button_dechiffrage = tk.Button(root,text="Déchiffrage",command=dechif_text)
entry_cle = tk.Entry(root,textvariable=key)
entry_msg = tk.Entry(root,textvariable=msg)
entry_result = tk.Entry(root,textvariable=result)

button_dechiffrage.grid(row=1,column=0)
button_chiffrage.grid(row=1,column=1)
entry_msg.grid(row=0,column=0)
entry_cle.grid(row=0,column=1)
entry_result.grid(row=4,column=0,columnspan=2)

root.mainloop()
