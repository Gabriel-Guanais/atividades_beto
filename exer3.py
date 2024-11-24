def temperatura (celsius):
    return celsius * 1.8 + 32

n1 = int(input("Me diaga a temperatura : "))

resposta = temperatura(n1)

print(f"{n1}° para Fahrensheit é {resposta}")
