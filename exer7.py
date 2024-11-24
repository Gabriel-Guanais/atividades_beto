def palavra_invertida(palavra):
    return palavra[::-1]

palavra = input('Escolha uma palavra para inverter:').strip

resposta = palavra_invertida(palavra)

print(f'{palavra} invertido(a) fica {resposta}')