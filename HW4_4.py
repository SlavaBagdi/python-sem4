from random import randint
k = int(input('Введите натуральную степень k: '))
a = randint(0, 100)
b = randint(0, 100)
print(f'{a}*x^{k} + {b}*x + 5 = 0')
with open('task_4.txt', 'w') as data:
    data.write(f'{a}*x^{k} + {b}*x + 5 = 0')
