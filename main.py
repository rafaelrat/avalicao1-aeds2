import random
import pandas as pd
import matplotlib.pyplot as plt
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
                print(f"O valor {valor} foi encontrado, Comparações: {comp}")
                return comp
        print(f"O valor {valor} não foi encontrado, Comparações: {comp}")
        return comp

#Parte Ordenada
comp_ordenada = []

for j in range(10_000, 100_001, 10_000):
    raiz = Node(1)
    for n in range (2, j + 1):
        raiz.insere(n)
    comp_ordenada.append(raiz.busca(100_001))
   

#Parte Desordenada
comp_aleatoria = []

for i in range(10_000, 100_001, 10_000):
    lista = list(range(1, i + 1))      #coloca do 1 até a última dezena de milhar desejada
    random.shuffle(lista)

    raiz = Node(lista[0])              #começa a árvore com o primeiro número

    for n in range(1, i):
        raiz.insere(lista[n])          #insere os demais números na ordem aleatória

    comp_aleatoria.append(raiz.busca(100_001))                #ao final, busca o 100_001

values = list(range(10_000, 100_001, 10_000))

dados ={'Valores': values,
        'Comparações (Aleatória)': comp_aleatoria,
        'Comparações (Ordenada)': comp_ordenada}

tabela = pd.DataFrame(dados)
print(f"\tTabela da Árvore Binária \n{tabela}") 


plt.figure(figsize=(10, 6))
plt.plot(values, comp_aleatoria, marker='o', linestyle='-', color='g', label='BST - Inserção Aleatória')
plt.plot(values, comp_ordenada, marker='o', linestyle='-', color='b', label='BST - Inserção Ordenada')

plt.title('Árvore Binária de Busca: Comparações vs Tamanho de N')
plt.xlabel('Número de Elementos (N)')
plt.ylabel('Número de Comparações na Busca')

plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.xticks(values)
plt.tight_layout()

plt.savefig('grafico_bst_comparacoes.png')
plt.close()
