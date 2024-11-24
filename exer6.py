# def media(nota1, nota2, nota3):
#     return nota1 + nota2 + nota3 / 3

# resposta = media(6, 5, 8)
    
# print(resposta)

def media (notas):
    return sum(notas) / len(notas)
    
quantidade = int(input('Informe a quantidade de notas : '))

notas = []
for i in range(1, quantidade +1):
    nota = float(input(f'Digite a nota {i} : '))
    notas.append(nota)

resposta = media(notas)

print(f'A media das {quantidade} notas sao : {resposta :.2f}')