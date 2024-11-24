numero = [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10]

def tabuada(n1):
    for i in numero:
        print(f'{i} x {n1} = {i * n1}')

n1 = int(input('digite um numer: '))
tabuada(n1)


