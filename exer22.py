
frase = input("Digite uma frase: ")

contador_vogais = 0
contador_consoantes = 0

vogais = "aeiou"

for i in frase:
    if i.isalpha():
        if i.lower() in vogais:
            contador_vogais += 1
        else:
            contador_consoantes += 1

print(f"O numero de vogais é: {contador_vogais}")
print(f"O numero de consoantes é: {contador_consoantes}")
