steps = 2
nums = []
total = 0

while True:
    try:
        for i in range(steps):
            nums.append(float(input(f'Insira seu número para dividir por {steps}\n')))
        break
    except ValueError:
        print('Escreva um número real!')
        nums.clear()

for i in range(len(nums)):
    total += nums[i]

total = total / len(nums)

print(total)