steps = 4
nums = []
totalP = totalN = totalF = 0

while True:
    try:
        for i in range(steps):
            num = (float(input(f'Insira seu número para dividir por média aritimética\n')))
            weigth = float(input('Peso:\n'))
            nums.append((num, weigth))
        break
    except ValueError:
        print('Escreva um número real!')
        nums.clear()

for num, weigth in nums:
    totalN += num * weigth
    totalP += weigth

weightedTotal = totalN / totalP

print("Números e pesos:", nums)
print("Média ponderada:", weightedTotal)