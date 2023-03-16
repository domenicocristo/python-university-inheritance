"""
Scrivete un metodo per Mazzo di nome dai_mani che prenda come parametri il numero di mani 
e il numero di carte da dare a ciascuna mano, e crei il numero stabilito di oggetti Mano, 
distribuisca il numero prefissato di carte a ogni mano e restituisca una lista delle Mani.
"""

import random

class Mazzo:
    def __init__(self):
        self.mazzo = []
        for seme in ["Cuori", "Quadri", "Fiori", "Picche"]:
            for valore in range(1, 14):
                if valore == 1:
                    self.mazzo.append("Asso di {}".format(seme))
                elif valore == 11:
                    self.mazzo.append("Jack di {}".format(seme))
                elif valore == 12:
                    self.mazzo.append("Regina di {}".format(seme))
                elif valore == 13:
                    self.mazzo.append("Re di {}".format(seme))
                else:
                    self.mazzo.append("{} di {}".format(valore, seme))
        
    def dai_mani(self, num_mani, num_carte):
        random.shuffle(self.mazzo)
        mani = []
        for i in range(num_mani):
            mano = Mano()
            for j in range(num_carte):
                carta = self.mazzo.pop()
                mano.aggiungi_carta(carta)
            mani.append(mano)
        return mani


class Mano:
    def __init__(self):
        self.carte = []
        
    def aggiungi_carta(self, carta):
        self.carte.append(carta)
        
    def __str__(self):
        if self.carte:
            return "\n".join(self.carte)
        else:
            return "Nessuna carta"

mazzo = Mazzo()
mani = mazzo.dai_mani(4, 5)

for i, mano in enumerate(mani):
    print(f"Mano {i+1}:")
    print(mano)
    print()