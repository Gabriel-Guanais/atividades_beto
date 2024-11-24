def primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):  
        if numero % i == 0: 
            return False
    return True  

primos = []
for num in range(10, 51):
    if primo(num):    
        primos.append(num)

print("Números primos de 10 a 50:", primos)
