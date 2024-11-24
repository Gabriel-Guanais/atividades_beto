def contador_palavra(frase):
    palavra = frase.split()
    return len(palavra)

frase = input('Escreva uma frase')
resposta = contador_palavra(frase)

print(f'A frase possui {resposta} palavras') 