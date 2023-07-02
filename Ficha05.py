import csv

# 1 Importar Dados
def ler_dados_csv(caminho_ficheiro):
    with open(caminho_ficheiro, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return [row for row in reader]
    
dados = ler_dados_csv('AtividadePedagogica4_10793_02.csv')    

# 2.1 Ordenação com o algoritmo bubble_sort -> erro
def bubble_sort(matriz):

    n = len(matriz)
    for i in range(n - 1):
        for j in range(n - i - 1):
            # Comparar os valores na coluna "produto"
            if matriz[j][3] > matriz[j + 1][3]:
                # Trocar as linhas
                matriz[j], matriz[j + 1] = matriz[j + 1], matriz[j]

# Chamada da função bubble_sort
bubble_sort(dados)

# Exibir a matriz ordenada
for linha in dados:
    print(linha)


    
# 3 Apresentar resultados

# 3.1 Calcular total de vendas de cada produto

def calcular_total_vendas_por_produto(dados):
    total_vendas = {}
    for venda in dados:
        produto = venda['produto']
        quantidade = int(venda['quantidade_vendida'])
        if produto in total_vendas:
            total_vendas[produto] += quantidade
        else:
            total_vendas[produto] = quantidade
    return total_vendas

total_vendas = calcular_total_vendas_por_produto(dados)
print("Total de vendas por produto:")
for produto, vendas in total_vendas.items():
    print(f"{produto}: {vendas} unidades")
    
# 3.2 Gerar gráfico

# import matplotlib.pyplot as plt -> 

# plt.bar(produto,total_vendas,color='#AA0000',label='Total vendas por produto')
# plt.title('Total vendas por produto')
# plt.ylabel('Total de Vendas', fontdict='Bahnschrift')
# plt.xlabel('Produto', fontdict='Bahnschrift')
# plt.legend()
# plt.show()