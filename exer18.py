def soma_diagonais(matriz):
    n = len(matriz)
    soma_principal = 0
    soma_secundaria = 0

    for i in range(n):
        soma_principal += matriz[i][i]
        soma_secundaria += matriz[i][n-1-i]

    return soma_principal, soma_secundaria

# Função para criar uma matriz quadrada
def criar_matriz(n):
    matriz = []
    for i in range(n):
        linha = []
        for j in range(n):
            elemento = int(input(f"Digite o elemento da posição [{i}][{j}]: "))
            linha.append(elemento)
        matriz.append(linha)
    return matriz

# Tamanho da matriz
n = int(input("Digite o tamanho da matriz quadrada: "))

# Criar a matriz
matriz = criar_matriz(n)

# Calcular a soma das diagonais
soma_principal, soma_secundaria = soma_diagonais(matriz)

# Imprimir resultados
print("\nMatriz:")
for linha in matriz:
    print(linha)

print(f"\nSoma da diagonal principal: {soma_principal}")
print(f"Soma da diagonal secundária: {soma_secundaria}")