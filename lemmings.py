import os

class Lemming:
    def __init__(self, jeu, ligne, colonne):
        self.j = jeu
        self.l = ligne
        self.c = colonne
        self.d = 1

    def __str__(self):
        if self.d == 1:
            return ">"
        else:
            return "<"

    def affiche(self):
        out = """"""
        for line in self.j:
            for case in line:
                out += str(case)
            out += "\n"
        print(out[:-1])
        
    def deplacement(self, l, c):
        self.j[self.l][self.c].depart()
        if self.j[l][c].libre():
            self.l = l
            self.c = c
            self.j[l][c].arrivee(self)
            return True

    def action(self):
        hasMoved = False

        if str(self.j[self.l + 1][self.c]) == " ":
            self.deplacement(self.l + 1, self.c)
            hasMoved = True
        
        if not hasMoved:
            if self.d == 1:
                if str(self.j[self.l][self.c + 1]) == "#":
                    self.deplacement(self.l, self.c - 1)
                    self.d = -1
                    hasMoved = True
            else:
                if str(self.j[self.l][self.c - 1]) == "#":
                    self.deplacement(self.l, self.c + 1)
                    self.d = 1
                    hasMoved = True
    
        if not hasMoved:
            if self.d == 1:
                self.deplacement(self.l, self.c + 1)
            else:
                self.deplacement(self.l, self.c - 1)

        return self.j

    def sort(self):
        self.j[self.l][self.c].depart()

class Case:
    def __init__(self, game, char):
        self.game = game
        self.terrain = char
        self.lemming = None
    
    def __str__(self):
        if self.lemming == None:
            return self.terrain
        else:
            return str(self.lemming)

    # def __repr__(self):
    #     return self.terrain

    def depart(self):
        self.lemming = None
    
    def libre(self):
        return self.lemming == None and not self.terrain == '#'
    
    def arrivee(self, lemming):
        if self.terrain == 'O':
            self.depart()
            lemming.sort()
            self.game.finir()
        else:
            self.lemming = lemming

class Jeu:
    def __init__(self, nom_fichier):
        self.finished = False
        self.lemmings = []
        self.game = []
        with open(nom_fichier, "r") as f:
            for line in f:
                self.game.append([])
                for char in line:
                    if char != "\n":
                        self.game[-1].append(Case(self, char))

    def getitem(self, i):
        return self.game[i]
    
    def affiche(self):
        out = """"""
        for line in self.game:
            for case in line:
                out += str(case)
            out += "\n"
        print(out[:-1])

    def finir(self):
        self.finished = True
        print('Bravo !')
        exit()
    
    def ajouteLemming(self):
        if self.game[1][1].libre():
            newLemming = Lemming(self.game, 1, 1)
            self.game[1][1].arrivee(newLemming)
            self.lemmings.append(newLemming)
            newLemming.action()
            print("Un lemming a été ajouté")
        else:
            print('Case non vide')

    def tour(self):
        for lemming in self.lemmings:
            self.game = lemming.action()

    def demarre(self):
        while not self.finished:
            print()
            self.affiche()
            cmd = input("- 1 : Ajouter un Lemming\n- ENTREE : Jouer un tour\n- Q : Quitter\nVotre commande : ")
            if cmd == "1":
                self.ajouteLemming()
            elif cmd == "Q":
                self.finished = True
            else:
                self.tour()

jeu = Jeu(os.path.dirname(__file__) + "/map.txt")
jeu.demarre()
