import random as rd


class Animal:
    def __init__(self, role: str, coords: tuple):
        self.vie = 5
        self.x = coords[0]
        self.y = coords[1]
        self.role = role
        if role == "proie":
            pass
        else:
            pass

    def show(self, canvas, rayon):
        if self.role == "proie":
            self.render = canvas.create_oval(self.x*rayon, self.y*rayon, self.x*rayon+rayon, self.y*rayon+rayon, fill="white")
        else:
            self.render = canvas.create_oval(self.x*rayon, self.y*rayon, self.x*rayon+rayon, self.y*rayon+rayon, fill="orange")

    def update(self, canvas, rayon):
        canvas.move(self.render, self.var_x*rayon, self.var_y*rayon)

    def move(self, les_autres):
        voisinage = []
        for i in range(3):
            i -= 1
            for j in range(3):
                j -= 1
                ij = (self.x+i, self.y+j)
                if ij not in les_autres or ij == (self.x, self.y):
                    voisinage.append(ij)
        if len(voisinage) != 1:
            xy = rd.choice(voisinage)
            self.var_x = self.x - xy[0]
            self.var_y = self.y - xy[1]
            self.x = xy[0]
            self.y = xy[1]
