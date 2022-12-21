# Напишите программу, которая принимает на вход число N и выдает последовательность из N членов
'''
n = int(input("Введите число:  "))
num = 1
print(num, end = ", ")
for i in range(1,n):
    num *= -3
    print(num, end = ", ")
'''

# для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1
'''
n = int(input())
a = {}
for i in range(1, n+1):
    a[i] = i*3 + 1
print(a)
'''

# Напишите программу, в которой пользователь будет задавать две строки, а программа определять количество 
# вхождений одной строки в другой
'''
line1 = input()
line2 = input()
count = 0
for i in range (len(line1) - len(line2)):
    if line1[i:i + len(line2)] == line2:
        count+=1
print(count)
# print(line1.count(line2)) - второй вариант решения в одну строку.
'''

# создайте список из случайных чисел. Найдите максимальное количество его одинаковых элементов
'''
import random
n = int(input())
list = []
for i in range(n):
    list.append(random.randint(2,5))
print(list)
max = 0
for i in range(n):
    if list.count(list[i]) > max:
        max = list.count(list[i])
print(max)
'''

# 2-й вармант
# создайте список из случайных чисел. Найдите максимальное количество его одинаковых элементов
'''
import random

list_num = []
max = 0
for i in range(10):
    a = random.randint(2,5)
    list_num.append(a)
for i in set(list_num):
    if list_num.count(i) > max:
        max = list_num.count(i)
print(max)
'''

# Данная программа должна вывести n рядов, заполненных знаком '*' определенным образом. А именно: 
# в первом ряду должно быть n звездочек, во втором n-1 и так далее
'''
n = int(input())
for i in range(n, 0, - 1):
    print("*"*i, ) 
'''
