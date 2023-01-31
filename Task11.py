#Дано натуральное число A > 1. Определите, каким по
#счету числом Фибоначчи оно является, то есть
#выведите такое число n, что φ(n)=A. Если А не
#является числом Фибоначчи, выведите число -1.

a = int(input('Введите число: '))

fib1 = 0
fib2 = 1
n = 2
while a > fib2:
    t = fib1
    fib1 = fib2
    fib2 = t + fib2
    n+=1
print(f'Число {a} по счету {n}-ое число фибоначчи' if a == fib2 else f'-1')