import pandas as pd
import numpy as np

# 1 Importar Dados
opened = open("AtividadePedagogica4_10793_02.csv", "r")
dados = pd.read_csv("AtividadePedagogica4_10793_02.csv")
print(dados)

# 2.1 Ordenação com o algoritmo bubble_sort -> erro

def bubble_sort(listoflists, index):

    n = len(listoflists)
    for i in range(n - 1):
        for j in range(n - i - 1):
            # Comparar os valores na coluna "quantidade_vendida"
            if listoflists[j][index] > listoflists[j + 1][index]:
                # Trocar as linhas
                listoflists[j], listoflists[j + 1] = listoflists[j + 1], listoflists[j]

# conversão da matriz numa lista de listas
dados_listoflists = np.array(dados).tolist()

# Chamada da função bubble_sort
index = 3
bubble_sort(dados_listoflists, index)

dados_bubble_sort = pd.DataFrame(dados_listoflists) 
dados_bubble_sort.columns = dados.columns 
print("Lista de produtos ordenada por vendas:\n",dados_bubble_sort)

    
# 3 Apresentar resultados

# 3.1 Calcular total de vendas de cada produto

def calcular_total_vendas_por_produto(dados):
    global produto
    total_vendas = {}
    for venda in dados:
        produto = venda[1]
        quantidade = int(venda[3])
        if produto in total_vendas:
            total_vendas[produto] += quantidade
        else:
            total_vendas[produto] = quantidade
    return total_vendas

total_vendas = calcular_total_vendas_por_produto(dados_listoflists)
total_vendas_list = list(total_vendas.items())

index = 1    
bubble_sort(total_vendas_list, index)

total_vendas_arr = np.array(total_vendas_list)

# 3.2 Gerar gráfico

import matplotlib.pyplot as plt 

plt.bar(total_vendas_arr[:,0],total_vendas_arr[:,1].astype(np.int16),color='#AA0000',label='Total vendas por produto')
plt.title('Total vendas por produto')
plt.ylabel('Total de Vendas')
plt.xlabel('Produto')
plt.legend()
plt.show()