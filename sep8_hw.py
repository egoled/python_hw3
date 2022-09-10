# ЗАДАЧА 1
# Задайте список из нескольких чисел. Напишите программу, которая найдёт
# сумму элементов списка, стоящих на нечётной позиции.
# # Пример:
# # - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# РЕШЕНИЕ
# new_list = [int(input('Введите элемент: ')) for i in range (int(input('Введите количество элементов: ')))]
# sum_odd = 0
# for i in range (1, len(new_list), 2):
#      sum_odd = sum_odd + new_list[i]
# print(sum_odd)


# ЗАДАЧА 2
# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый
# и последний элемент, второй и предпоследний и т.д.
## Пример:
## - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# РЕШЕНИЕ
# def mult_pair(list):
#     return [list[i] * list[-i - 1] for i in range((len(list) + 1) // 2)]
#
# new_list = [2, 3, 4, 5, 6]
# print(new_list)
# print('произведение пар чисел списка: ', mult_pair(new_list))


# ЗАДАЧА 3
# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# РЕШЕНИЕ
# n = int(input('Введите длину списка: '))
# list_fl = [float(input('Введите вещественное число: ')) for i in range(n)]
# list_new = []
# for i in range(0, len(list_fl)):
#     list_new.append(list_fl[i] % 1)
# max_el = max(list_new)
# min_el = min(list_new)
# dif = max_el - min_el
# print(f'Разница между максимальным {max_el} и минимальным значением {min_el} дробной части элементов равна {round(dif, 4)}')


# ЗАДАЧА 4
# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

#РЕШЕНИЕ
# n = int(input('Введите десятичное число: '))
# bi = ''
# while n > 0:
#     bi = str(n % 2) + bi
#     n = n//2
# print (f' -> {bi}')


# ЗАДАЧА 5
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]


# РЕШЕНИЕ
# def fib (neg_pos):
#     if neg_pos == 0:
#         return [0]
#     fib_list = [1, 0]
#     for i in range(neg_pos):
#         fib_list.append(fib_list[len(fib_list) - 2] - fib_list[len(fib_list) - 1])
#     fib_list.reverse()
#     for i in range(neg_pos - 1):
#         fib_list.append(fib_list[len(fib_list) - 2] + fib_list[len(fib_list) - 1])
#     return fib_list
# n = int (input("Введите число: "))
# print(f'Список чисел Фибоначчи от -{n} до {n} равен ',fib(n))