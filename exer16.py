def recursiva(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * recursiva(n - 1)
    
fatorial = recursiva(5)
print(fatorial)