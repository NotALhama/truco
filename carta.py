import random

valor = {
    9: "3",
    8: "2",
    7: "A",
    6: "K",
    5: "J",
    4: "Q",
    3: "7",
    2: "6",
    1: "5",
    0: "4" 
}

naipe = {
    0: "copas",
    1: "ouros",
    2: "paus",
    3: "espadas"
}

#lista de manilhas
manilhas = [[0,2], [7,3], [3,0], [3,3]]


class Carta:
    valor = 0
    naipe = 0
    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe
    def get_value(self):
        c = [self.valor, self.naipe]
        if c in manilhas:
            valor = 13
            return valor - manilhas.index(c)
        if c not in manilhas:
            return self.valor 
    def getName(self): 
        return valor[self.valor] + " de " + naipe[self.naipe]
         
class Baralho:
    cartas = []

    def gen(self):
        self.cartas = []        
        for i in range(4):
            for j in range(10):
                nova = Carta(i, j)
                self.cartas.append(nova)

    def embaralhar(self):
        random.shuffle(self.cartas)
    
    def pop(self):
        return self.cartas.pop(0)
