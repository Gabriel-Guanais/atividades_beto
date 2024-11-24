numeros = input("liste  numeros inteiros  separados por espaço: ")

numeros = list(map(int, numeros.split()))

pares = [num for num in numeros if num % 2 == 0]

print(f"numeros pares: {pares}")
