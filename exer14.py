def ver_palindromo(palavra):
    if palavra == palavra[::-1]:
        print('é um palindromo')
    else: 
        print('nao é um palindromo')

texto = input('Digite uma palavra: ').strip()
ver_palindromo(texto)