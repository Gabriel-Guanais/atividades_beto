import random

print(34 * '*')
print('Bem-Vindo ao Jogo das Adivinhaoes')
print(34* '*')

numero_aleatorio = random.randint(0,100)
ganhou = False
tentativas = 1

while not ganhou:
    jogador = int(input('De 1 a 100 qual foi o numero que pensei: '))

    if jogador == numero_aleatorio:
        print('Parabens voce acertou')
        print(f'Voce consiguiu com {tentativas} tentativas')
        ganhou = True
    else:
        print('Por favor tente novamente...')
        tentativas += 1
        
        if numero_aleatorio > jogador:
            print(f'O numero secreto é maior que {jogador}')
        else:
            print(f'O numero secreto é menor que {jogador}')