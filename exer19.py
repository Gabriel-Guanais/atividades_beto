def contador(frase):
    contagem = {}
    for caractere in frase:
        if caractere in contagem:
            contagem[caractere] += 1
        else:
            contagem[caractere] = 1
    return contagem

frase = input("Digite uma frase: ")
resultado = contador(frase)

for caractere, quantidade in resultado.items():
    print(f"'{caractere}': {quantidade}")