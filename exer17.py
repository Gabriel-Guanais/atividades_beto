def ordenar(lista):
    negativos = [num for num in lista if num < 0]
    positivos = [num for num in lista if num >= 0]
    return negativos + positivos


numeros = [1, -1, -2, 2, 3, -3, 4, 5, -4, 6, -5, -6,]
resultado = ordenar(numeros)

print("Lista inicial:", numeros)
print("Lista ordenada (negativos antes dos positivos):", resultado)