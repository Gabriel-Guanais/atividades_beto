def maioridade(idade):
    if idade >= 18 :
        print(f'Parabens...com {idade_usuario} anos vc atingiu a maioridade')
    else:
        print(f'Voce com {idade_usuario} anos nao atingiu a maior idade')
    return

ano_atual = int(input('Em que ano estamos : '))
ano_nascimento = int(input('Em que ano voce nasceu: '))
idade_usuario = ano_atual - ano_nascimento
maioridade(idade_usuario)


