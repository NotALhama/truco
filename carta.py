import random

class Carta:
    valor = 0
    naipe = 0
    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe

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

