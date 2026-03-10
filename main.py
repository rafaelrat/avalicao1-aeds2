class SemBalanceamento(object):
    "Define e inicializa um nó da árvore, rejeitando qualquer valor não inteiro"
    def __init__(self, key, value=None, left=None, right=None):
        if not isinstance(key, int):
            raise TypeError("A chave deve ser um número inteiro")

        self.key = key
        self.value = value
        self.left = left
        self.right = right
 
 
    "---------------------------------------------------------------------------"
    "BUSCA"
    def get(self, key):

        if not isinstance(key, int):
            raise TypeError("A chave de busca deve ser um número inteiro")

        if self.key == key:
            return self

        node = self.left if key < self.key else self.right
        if node is not None:
            return node.get(key)
    "---------------------------------------------------------------------------"
    "ADIÇÃO DE NÓS"
    def add(self, key):
        """Adiciona elemento à subárvore"""
        if not isinstance(key, int):
            raise TypeError("A chave deve ser um número inteiro")

        side = 'left' if key < self.key else 'right'
        node = getattr(self, side)

        if node is None:
            setattr(self, side, SemBalanceamento(key))
        else:
            node.add(key)
    "---------------------------------------------------------------------------"

# Demonstração
tree = SemBalanceamento(0)

for i in range(1, 10):
    tree.add(i)

node = tree.get(11)

if node:
    print("Nó encontrado:", node.key)
else:
    print("Nó não encontrado")

tree.add(11)

node = tree.get(10)

if node:
    print("Nó encontrado:", node.key)
else:
    print("Nó não encontrado")