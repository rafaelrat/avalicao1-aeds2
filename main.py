import random
class Node():
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
                temp =temp.esquerda

            elif valor > temp.valor:
                temp = temp.direita
            
            else:
                return (temp.valor, comp)
        print(f"Não foi encontrado o número desejado: {valor}")
        print(f"Número de comparações: {comp}")
        return

for i in range(10_001, 100_001, 10_000):
    raiz = Node(1)
    for n in range (2, i):
        raiz.insere(n)
    busca = raiz.busca(100_001)
   

