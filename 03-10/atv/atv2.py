while True:
    try:
        h = float(input("Altura: "))
        B = float(input("Base maior: "))
        b = float(input("Base menor: "))
        if h <= 0 and b <= 0:
            raise ValueError
        break
    except ValueError:
        print('Escreva um número real positivo!')

print("Área do trapézio:", ((b+b)*h)/2)