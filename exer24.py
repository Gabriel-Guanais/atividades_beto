palavra1 = input("gigite a primeira palavra: ").lower()
palavra2 = input("gigite a segunda palavra: ").lower()


if sorted(palavra1) == sorted(palavra2):
    print("as palavras são anagramas!")
else:
    print("as palavras não são anagramas.")
