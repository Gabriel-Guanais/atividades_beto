from collections import Counter

texto = input("Digite um texto: ")

palavras = ''.join(char if char.isalnum() or char.isspace() else ' ' for char in texto).lower().split()

frequencia = Counter(palavras)

top_5 = frequencia.most_common(5)

print("as 5 palavras mais frequentes são:")
for palavra, contagem in top_5:
    print(f"{palavra}: {contagem} vezes")
