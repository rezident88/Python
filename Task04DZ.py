#Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе
#они сделали S журавликов. Сколько журавликов сделал каждый
#ребенок, если известно, что Петя и Сережа сделали одинаковое
#количество журавликов, а Катя сделала в два раза больше журавликов,
#чем Петя и Сережа вместе?



a = int(input('Введите количество изготовленных журавликов: '))
k = int((a/3)*2)
p = int((k/2)/2)
s = int(p)
print(p, k, s)