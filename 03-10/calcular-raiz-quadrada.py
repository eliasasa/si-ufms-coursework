while True:
    try:
        number = int(input("Número: "))
        if number <= 0:
            raise ValueError
        break
    except ValueError:
        print('Escreva um número inteiro!')

result = number**.5

print("A raiz quadrada de ", number, "é ", result)