#15. Иван Васильевич пришел на рынок и решил
#купить два арбуза: один для себя, а другой для тещи.
#Понятно, что для себя нужно выбрать арбуз
#потяжелей, а для тещи полегче. Но вот незадача:
#арбузов слишком много и он не знает как же выбрать
#самый легкий и самый тяжелый арбуз? Помогите ему!
#Пользователь вводит одно число N – количество
#арбузов. Вторая строка содержит N чисел,
#записанных на новой строчке каждое. Здесь каждое
#число – это масса соответствующего арбуза
import random
n = int(input('Введите число: '))
numb = random.randint(1,9)
min1 = numb
max1 = numb

for i in range(n):
    numb = random.randint(1,9)
    print(numb, end=' ')
    if numb > max1:
        max = numb
    if numb < min1:
        min1 = numb
print(f'\n {min1} {max1}')    