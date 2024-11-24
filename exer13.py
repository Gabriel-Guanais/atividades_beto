def media(n1, n2, n3, n4):
    media_resultado = (n1 + n2 + n3 + n4) / 4
    
    notas_mmedia = []
    
    for nota in [n1, n2, n3, n4]:
        if nota > 4:
            notas_mmedia.append(nota)
            
    return media_resultado, notas_mmedia

notas, lista_notas_maiores = media(3 ,5 ,6 ,4)

print(f'A Media das notas foi: {notas}')
print(f'Notas maiores que a media: {lista_notas_maiores}')
