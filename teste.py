import pandas as pd

# 1. Definir os dados em um dicionário
dados = {
    'Produto': ['Maçã', 'Banana', 'Laranja'],
    'Preço': [2.50, 1.20, 3.00],
    'Quantidade': [10, 20, 15]
}

# 2. Criar o DataFrame (a tabela)
tabela = pd.DataFrame(dados)

# 3. Exibir a tabela
print(tabela)
