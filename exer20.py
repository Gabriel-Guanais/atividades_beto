def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

numero = int(input("digite um número para calcular o fibonacci: "))
resultado = fibonacci(numero)
print(f"O {numero}-ésimo número de fibonacci é: {resultado}")