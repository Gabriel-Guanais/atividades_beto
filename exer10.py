def area_retangulo(a, b):
    return (a * b) / 2
    
base = int(input('Base Retangulo?: '))
altura = float(input('Altura Retangulo?: '))

resposta = area_retangulo(base, altura)

print(f'Area do retangulo:{resposta:.2f} ')