while True:
    try:
        num = int(input("Tábuada do número: "))
        if num <= 0:
            raise ValueError
        break
    except ValueError:
        print('Escreva um número inteiro positivo!')

for i in range(1, 11):
    print(num, 'X', i, '=', num*i)