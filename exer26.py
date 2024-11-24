dicionario1 = {'a': 10, 'b': 20, 'c': 30}
dicionario2 = {'b': 15, 'c': 25, 'd': 35}


dicionario_mesclagem = dicionario1.copy()  

for chave, valor in dicionario2.items():
    if chave in dicionario_mesclagem:
        dicionario_mesclagem[chave] += valor  
    else:
        dicionario_mesclagem[chave] = valor  


print(dicionario_mesclagem)
