from carta import *
import socket
import random

Valores = {
    2: "truco",
    4: "6",
    8: "10",
    10: "12"
}

class Player:
    mao = []
    nome = ""
    def __init__(self, nome):
        self.nome = nome
    

bots = [Player("residente de itaúna"), Player("baixinho"), Player("cacique")]

jogador = Player("Deus do truco")

class Jogo:
    baralho = Baralho()

    players = []
    p_atual = 0 # player atual
    p_proximo = 0 # proximo jogador
    p_inicial = 0 # numero que representa o jogador que começa jogando
    p_ganhando = 0 #jogador que jogou a maior carta em um turno
    cartas_jogadas = []
    placar = [0, 0]
    placar_turno = [0, 0]
    valor_da_rodada = 2

    def __init__(self):
        dupla_uno = [jogador, random.choice(bots)]
        bots.remove(dupla_uno[1])
        dupla_dos = bots
        self.players = [dupla_uno[0], dupla_dos[0], dupla_uno[1], dupla_dos[1]]
        self.baralho.gen()

    def aumentar_valor(self):
        if self.valor_da_rodada == 2:
            self.valor_da_rodada = 4
        elif self.valor_da_rodada == 4:
            self.valor_da_rodada = 8
        elif self.valor_da_rodada == 8:
            self.valor_da_rodada = 10
        else: self.valor_da_rodada = 12
    
    def novaRodada(self):
        self.baralho.gen()
        self.baralho.embaralhar()
        for i in self.players:
            i.mao = []
            for c in range(3):
                i.mao.append(self.baralho.pop())
        
        if self.p_inicial+1 == 4:
            self.p_inicial = 0
        else:
            self.p_inicial += 1

        self.p_atual = self.p_inicial
        if self.p_atual+1 == 4:
            self.p_proximo = 0
        else:
            self.p_proximo = self.p_atual + 1

    def registrarCarta(self, carta):
        maior = 0
        for i in self.cartas_jogadas:
            if i.getValue() > maior:
                maior = i.getValue()
        if carta.getValue > maior:
            self.p_ganhando = self.p_atual
        self.cartas_jogadas.append(carta)
    



        





"""
c = Cliente("127.0.0.1", 6969, "jp")
c.connect()
"""
    
j = Jogo()

while True:
    while 12 != j.placar[0] or j.placar[1]:
        j.novaRodada()
        while 3 != j.placar_turno[0] or j.placar_turno[1]:
            if(j.players[j.p_atual] == jogador):
                print(f"Sua mão: {jogador.mao}\n")
                while True:
                    carta = int(input(f"Jogue uma carta ({[i for i in range(len(jogador.mao))]}): "))
                    if carta in [i for i in range(len(jogador.maoclient.py))]:
                        break
                    print("Insira um número válido\n")
                j.registrarCarta(jogador.mao.pop(carta))
            
            else:
                p_atual = j.players[j.p_atual]
                carta = random.choice(p_atual.mao)
                j.registrarCarta(carta)
                p_atual.mao.remove(carta)
                print(f"[{p_atual.nome}]: Jogar carta {carta}")

            j.p_atual = j.p_proximo
            if len(j.cartas_jogadas) == 4:
                if j.p_ganhando.is_even():
                    j.placar_turno[0] += 1
                else:
                    j.placar_turno[1] += 1
                j.p_atual = j.p_ganhando
                if j.p_atual + 1 == 4:
                    j.p_proximo = 0
                else: j.p_proximo = j.p_atual + 1
            
            if j.p_proximo + 1 == 4:
                j.p_proximo = 0
            else: j.p_proximo += 1
             
