def contador(letra):
    return len(letra)


palavra = input("Digite uma palavra: ")
resposta = contador(palavra)

print(f'{palavra} contem {resposta} letras')