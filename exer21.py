def duplicados(lista):
    nova_lista = []
    for elemento in lista:
        if elemento not in nova_lista:
            nova_lista.append(elemento)
    return nova_lista

num = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
resultado = duplicados(num)
print("lista original:", num)
print("lista sem duplicados:", resultado)
