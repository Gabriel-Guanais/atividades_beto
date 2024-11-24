def calculadora(escolha):
    if escolha == 1:
        num1 = float(input("digite o primeiro número: "))
        num2 = float(input("digite o segundo número: "))
        return num1 + num2
    
    elif escolha == 2:
        num1 = float(input("digite o primeiro número: "))
        num2 = float(input("digite o segundo número: "))
        return num1 - num2
    
    elif escolha == 3:
        num1 = float(input("digite o primeiro número: "))
        num2 = float(input("digite o segundo número: "))
        return num1 * num2
    
    elif escolha == 4:
        num1 = float(input("digite o primeiro número: "))
        num2 = float(input("digite o segundo número: "))
        if num2 == 0:
            return "não é possível dividir por zero."
        return num1 / num2
    
    else:
        return "opção inválida, Por favor tente novamente."
    

escolha = int(input("escolha uma operação: 1 - Soma 2 - Subtração 3 - Multiplicação 4 - Divisão"))
resultado = calculadora(escolha)
print(f"resultado: {resultado}")

    
    