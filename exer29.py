def remover_duplicados(lista):
    return [list(set(sublista)) for sublista in lista]

lista_aninhada = [[1, 2, 2, 3], [4, 4, 5, 5], [6, 7, 7, 6]]

nova_lista = remover_duplicados(lista_aninhada)

print(nova_lista)
