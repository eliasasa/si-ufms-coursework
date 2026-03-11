import random

numbers = []

while len(numbers) < 100: 
    x = random.randint(1, 100)
    if x in numbers:
        pass
    else: numbers.append(x)

print(numbers)


def sortList(lst: list) -> list:
    sortedList = lst.copy()
    n = len(sortedList)
    for i in range(n):
        for j in range(0, n-i-1):
            if sortedList[j] > sortedList[j+1]:
                sortedList[j], sortedList[j+1] = sortedList[j+1], sortedList[j]
    return sortedList

print('=======================')
print(sortList(numbers))
        
        