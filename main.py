import random
class Node:
    def __init__(self, valor):
        self.esquerda = None
        self.direita = None
        self.valor = valor

    def insere(self, valor):
        temp = self
        
        while True:
            if valor < temp.valor:
                if temp.esquerda is None:
                    temp.esquerda = Node(valor)
                    return
                else:
                    temp = temp.esquerda
            else:
                if temp.direita is None:
                    temp.direita = Node(valor)
                    return
                else:
                    temp = temp.direita

    def busca(self, valor):
        temp = self
        comp = 0
        while temp is not None:        
            comp+=1
            if valor < temp.valor:    
                temp = temp.esquerda

            elif valor > temp.valor:
                temp = temp.direita
            
            else:
                print(f"O número {valor} foi encontrado!")
                print(f"Número de comparações: {comp}")
                return comp
        print(f"Não foi encontrado o número desejado: {valor}")
        print(f"Número de comparações: {comp}")
        return comp

for i in range(10_000, 100_001, 10_000):
    lista = list(range(1, i + 1))      #coloca do 1 até a última dezena de milhar desejada
    random.shuffle(lista)

    raiz = Node(lista[0])              #começa a árvore com o primeiro número

    for n in range(1, i):
        raiz.insere(lista[n])          #insere os demais números na ordem aleatória

    raiz.busca(100_001)                #agora está dentro do for principal                   #ao final, busca o 100_001

       