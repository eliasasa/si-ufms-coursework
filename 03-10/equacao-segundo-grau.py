vars = ["a", "b", "c"]
values = {}

for name in vars:
    while True:
        try:
            number = float(input(f"Número {name}:\n"))
            if number <= 0:
                raise ValueError
            values[name] = number
            break
        except ValueError:
            print("Escreva um número real positivo!")

result = values["b"]**2 - 4 * (values["a"] * values["c"])

print('Resultado:', result)