class SemBalanceamento(object):
    
    def __init__(self, key, left=None, right=None):
        """método construtor dos nós"""
        if not isinstance(key, int): #rejeita qualquer valor não inteiro
            raise TypeError("A chave deve ser um número inteiro") 

        self.key = key #número do nó 
        self.left = left #nó 'filho' da esquerda
        self.right = right #nó 'filho' da direita
 
 
    # ---------------------------------------------------------------------------
   
    def get(self, key):
        """método de busca"""
        if not isinstance(key, int): #rejeita qualquer valor não inteiro
            raise TypeError("A chave de busca deve ser um número inteiro")

        if self.key == key: 
            return self #retorna o nó se encontrado

        node = self.left if key < self.key else self.right #busca o nó nas raízes da esquerda e direita
        if node is not None:
            return node.get(key) #busca recursivamente o nó desejado percorrendo as raízes

    # ---------------------------------------------------------------------------
    
    def add(self, key):
        """Adiciona elemento à subárvore"""
        if not isinstance(key, int): #rejeita qualquer valor não inteiro
            raise TypeError("A chave deve ser um número inteiro")

        side = 'left' if key < self.key else 'right' #organiza a árvore com valores menores à esquerda e maiores à direita
        node = getattr(self, side)

        if node is None:
            setattr(self, side, SemBalanceamento(key)) #adiciona o novo nó 
        else:
            node.add(key)  #percorre recursivamente a árvore até achar o lugar a ser implementado 

    # ---------------------------------------------------------------------------


# Demonstração
tree = SemBalanceamento(0) #cria um nó com chave '0'

for i in range(1, 10): #adiciona nós de 1 a 10 (organizados linearmente pelo exemplo)
    tree.add(i)
    
node = tree.get(11) #busca nó desejado

if node: #verificação
    print("Nó encontrado:", node.key) 
else:
    print("Nó não encontrado")