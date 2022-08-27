# import numpy
# import numpy as np
# n = int(input())
# s = []
# m = []
# for i in range(1, n+1):
#     x = int(input())
#     s.append(x)
#
#     a = min(s)
#     b = max(s)
#     while b != 0:
#         a, b = b, a % b
#         m.append(a)
# print(min(m))
import string

# from math import gcd
# from functools import reduce
# a = []
# for i in range(int(input())):
#     x = int(input())
#     a.append(x)
#     n = len(a)
# print(reduce(gcd, a))

# n = 6
# a = int(input())
# for i in range(1, n):
#     b = int(input())
#     while b != 0:
#         a, b = b, a % b
# print(a)

# n = int(input())
# m = []
# for i in range(1, n+1):
#     x = int(input())
#     m.append(x)
#     a = min(m)
#     b = max(m)
#     while b != 0:
#         a, b = b, a % b
#     v = a
# print(v)
# d = 2
# while d * d <= v and v % d != 0:
#     d += 1
# print('YES' if d * d > v and v != 1 else 'NO')

# import time
# start = time.time()
# from math import gcd
# from functools import reduce
# m = []
# for i in range(1, int(input())+1):
#     m.append(int(input()))
#     a = gcd(min(m), max(m))
# d = 2
# while d * d <= a and d != a:
#     d += 1
# print('YES' if d * d > a and a != 1 else 'NO')
# end = time.time()
# print(end - start)

# m = []
# for i in range(int(input())):
#     x = int(input())
#     if x % 10 == 4:
#         m.append(x)
# print(min(m))

# t = 0
# for i in range(int(input())):
#     x = int(input())
#     if x % 6 == 0:
#         t += x
# print(t)


# n = (-6483, 8748, -6163, -5053, 7795, -6963, -3722, 159, 3395, -2035, 7669, 7156, 3012, -5502, -3317, -2458, -750, -3445, -9885, -2685)
# t = 0
# for i in range(len(n)):
#     for j in range(0, i+1):
#         if len(n) != i+1:
#             if (n[i] + n[j+1]) % 3 == 0 and (n[i] + n[j+1]) % 9 != 0:
#                 t += 1
# print(t)


# n = (-6483, 8748, -6163, -5053, 7795, -6963, -3722, 159, 3395, -2035, 7669, 7156, 3012, -5502, -3317, -2458, -750, -3445, -9885, -2685)
# t = 0
# for i in range(len(n)):
#     if len(n)-1 != i:
#         if (n[i] + n[i+1]) % 3 == 0 and (n[i] + n[i+1]) % 9 != 0:
#             t += 1
# print(t)


# n = (78.43, 51.68, 28.72, 17.01, 74.79, 28.27, 62.05, 64.72, 67.25, 59.56, 36.85, 3.3, 57.58, 32.44, 63.29, 88.23, 51.5, 15.56, 54.36, 72.3, 76.86, 77.43, 44.13, 75.13, 95.15, 72.95, 30.71, 23.72, 61.82, 30.6, 11.07, 18.86, 13.62, 68.72, 11.62, 83.31, 1.15, 96.49, 29.59, 21.49)
# t = 0
# m = -10
# for i in range(len(n)-1):
#     if abs(n[i] - n[i+1]) > m:
#         m = abs(n[i] - n[i + 1])
#         a = n[i]
#         b = n[i+1]
# print(n[i], n[i+1])


# x = input()
# m = []
# while x != '.':
#     if not '.' in x:
#         x = int(x)
#         if x % 2 == 0:
#             m.append(x)
#     x = input()
# print(*m[::-1])


# x = input()
# m = []
# flag = False
# while x != '.':
#     m.append(x)
#     x = input()
#     if len(m) % 2 != 0:
#         a = len(m) // 2
#         a = m[a]
#         flag = a
#     elif len(m) % 2 == 0:
#         a = len(m) // 2
#         b = (int(m[a-1]) + int(m[a])) / 2
#         flag = b
# print(flag)


# n = 5
# m = []
# s = []
# s1 = []
# for i in range(n):
#     x = int(input())
#     m.append(x)
# for j in range(len(m)):
#
#     if m[j] % 2 == 0:
#         s.append(m[j])
#         a = min(s)
#     elif len(s) == 0:
#         a = 0
#
#     if m[j] % 2 != 0:
#         s1.append(m[j])
#         b = min(s1)
#     if len(s1) == 0:
#         b = 0
#
# for k in range(len(m)):
#     if m[k] < (a + b):
#         m[k] += (a + b)
# print(*m)

# s = input().upper()
# m = []
# while s != '.':
#     m.append(s)
#     s = input().upper()
# for i in range(len(m)):
#     print(*m[i])

# s = input()
# m = []
# n = []
# while s != '.':
#     m.append(s)
#     s = input()
# for i in range(int(input())):
#     x = int(input())
#     a = m[x-1]
#     n.append(a)
# print(*n, sep='')

# Шпаргалка политика
# s1 = ['Товарищи!', 'с другой стороны', 'равным образом', 'Не следует, однако, забывать, что', 'Таким образом', 'Повседневная практика показывает, что', 'Значимость этих проблем настолько очевидна, что', 'Разнообразный и богатый опыт', 'Задача организации, в особенности же', 'Идейные соображения высшего порядка, а также']
# s2 = ['реализация намеченных планов', 'рамки и место обучения кадров', 'постоянный количественный рост и сфера нашей активности', 'сложившаяся структура организации', 'новая модель организационной деятельности', 'постоянное информационно-пропагандистское обеспечение нашей деятельности', 'укрепление и развития структуры', 'консультация с широким активом', 'начало повседневной работы по формированию позиции', 'дальнейшее развитие различных форм деятельности']
# s3 = ['играет важную роль в формировании', 'требуют от нас анализа', 'требуют определения и уточнения', 'способствуют подготовке и реализации', 'обеспечивает широкому кругу (специалистов) участие в формировании', 'позволяет выполнить важные задания по разработке', 'в значительной степени обусловливает создание', 'позволяет оценить значение', 'представляет собой интересный эксперимент проверки', 'влечет за собой процесс внедрения и модернизации']
# s4 = ['существующих финансовых и административных условий', 'дальнейших направлений', 'системы массового участия', 'позиций, занимаемых участниками в отношении поставленных задач', 'новых предложений', 'направлений прогрессивного развития', 'системы обучения кадров, соответствующей насущным потребностям', 'соответствующй условий активизации', 'модели развития', 'форм воздействия']


# s = input().split('.')
# print(s)
# for i in range(len(s)):
#     s[i] = int(s[i])
# print(sum(s))


# t = 0
# m = []
# for i in range(1, 10**6):
#     s = input()
#     if s == '.':
#         break
#     s = s.lower().split()
#     print(s)
#     if 'python' in s:
#         t += 1
#     m.append(s)
# print(t)


# for b in list(input().lower()):
#     if b not in ';:,.?!-':
#         print(b, end='')
# s = 'Кажется, можно, наверное, правилам. Верно?'.lower().replace('?', '')
# import re
# b = (re.split("; |. |! |, |: |- ", s))
# print(b)
# print(' '.join(b))


# n = int(input())
# s = input()
# m = []
# while '.' != s:
#     m.append(s)
#     s = input()
# for i in range(len(m)):
#     if len(m[i]) > n:
#         print(f'{m[i][:n]}... Читайте продолжение в источнике...')
#     elif len(m[i]) < n:
#         print(f'{m[i]}')

# s = 'Наш хлебушек это парад еще вздумай не черепаха конец черепица роскомнадзор'.split()
# k, n = int(input()), int(input())
# print(*s[k - 1::n])

# for i in range(1, 10**6):
#     s = input().split()
#     if '.' in s:
#         break
#     if s[0] == '@@' and s[-1] == '@@':
#         print('ошибка')
#     elif s[0] == '!!' and s[-1] == '!!':
#         print('предупреждение')
#     elif s[0] == '//' and s[-1] == '//':
#         print('информация')
#     elif s[0] == '**' and s[-1] == '**':
#         print('подробное сообщение')

# error, warning, inf, descript = 'ошибка', 'предупреждение', 'информация', 'подробное сообщение'
# while True:
#     s = input()
#     if s == '.':
#         break
#     if a[0] + a[1] and a[-1] + a[-2] == '@@':
#         print('{0}'.format(error, warning, inf, descript))
#     elif a[0] + a[1] and a[-1] + a[-2] == '!!':
#         print('{1}'.format(error, warning, inf, descript))
#     elif a[0] + a[1] and a[-1] + a[-2] == '//':
#         print('{2}'.format(error, warning, inf, descript))
#     elif a[0] + a[1] and a[-1] + a[-2] == '**':
#         print('{3}'.format(error, warning, inf, descript))

# m = []
# while True:
#     s = input()
#     if s == '.':
#         break
#     if s[0] == 'P':
#         n = s.replace('POST', '').lstrip()
#         m.append(n)
#     elif s[0] == 'G':
#         a = m[-1]
#         print(a)
#     elif s[0] == 'D':
#         del m[-1]
# print(*m)

# a, b, c = map(int, input().split())
# if a + b == c:
#     print('{} + {} = {}'.format(a, b, c))
# elif a - b == c:
#     print('{} - {} = {}'.format(a, b, c))
# elif a * b == c:
#     print('{} * {} = {}'.format(a, b, c))
# elif a / b == c:
#     print('{} / {} = {}'.format(a, b, c))
# else:
#     print(f'Error')

# s = 'Карл у Клары украл кораллы'
# m = []
# for i in range(len(s)):
#     if s[i] not in m:
#         m.append(s[i])
# print(*m, sep='')


# n = list(map(int, input().split(',')))
# t = 0
# for i in range(len(n)):
#     if min(n) == n[i]:
#         t += i
# print(t)

# s = input()
# m = []
# while s != s.upper() and s != s.lower():
#     m.append(s.swapcase())
#     s = input()
# print(*m, sep='\n', end='')

#l = list(map(int, input().split(',')))
# s1 = sorted(s, key=abs)
# print(*s1[-2:])


#s = '1Аргентина манит негра'.replace(' ', '').lower().split()
# s1 = list(map(str, input().replace(' ', '').lower().split()))
# s1.reverse()
# print(s1)


# s = [99, 259, 76, 1457, 1097, 99, 259, 76, 1502, 1457, 1235, 1213, 1457]
# s1 = 1200
# m = []
# n = []
# k = []
# b = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in range(len(s)):
#     if s1 < s[i]:         # все числа больше заданного, отправляются в список
#         k.append(s[i])
#         k.sort()
#     while s[i] > 0:       # немного другое решение, перепутал условие задачи и разложил все елементы на целые числа
#         m.append(s[i] % 10)
#         s[i] = s[i] // 10
# for i in m:
#     if i not in n:
#         n.append(i)
#         print(n)
# result = list((set(b)) - set(n))     # выявление разности списков(8 из списка b нет в списке n)
# print(*result, k[0], sep='\n')
#

# s = [99, 259, 76, 1457, 1097, 99, 259, 76, 1502, 1457, 1235, 1213, 1457]
# m = []
# k = []
# s1 = 1200
# for i in s:
#     if i not in m:        # исключает повторяющие элементы
#         m.append(i)
# print(len(m))
# for i in range(len(s)):
#      if s1 < s[i]:
#          k.append(s[i])
#          k.sort()
# print(k[0])

# s = 'C-3P0 & R2-D2 r c0m1n9 4 u'
# m = []
# count = 0
# def try_to_int(value):      # функция для поиска чисел
#     try:
#         return int(value) + 1 if int(value) != 9 else 0     # добавляет 1 к числу, и заменяет 9 на 0
#     except ValueError:
#         return value
# a = list(map(try_to_int, s))
# b = ''.join(map(str, a))
# print(b)
# for i in b:
#     if i in '0123456789':
#         i = int(i)
#         count += i
# print(count)
#
# text = 'C-3P0 & R2-D2 r c0m1n9 4 u'
# m = []
# count = 0
# for i in text:
#     if i in '0123456789':
#         i = int(i)
#         if i == 9:
#             i = 0
#             count += i
#         else:
#             i += 1
#             count += i
#     i = str(i)
#     m.append(i)
# print(*m, sep='')
# print(count)

# s = list(map(int, input().split()))
# print(*[i ** s[2] for i in range(s[0], s[1] + 1)])



# lst = [input().split(', ') for i in range(int(input()))]
#lst = [['Guidonia 140', 'Cecchignola 84', 'Torresina 68'], ['Guidonia 140', 'Cecchignola 84', 'Torresina 168']]
# m = []
# for i in lst:
#     new = []
#     for j in i:
#         new.append((int(j.split()[1]), j.split()[0]))      # добавляем кортеж из цифр и городов
#         # new = [(140, 'Guidonia'), (84, 'Cecchignola'), (168, 'Torresina')]
#     m.append(sorted(new)[0][1])     # добавляем город(по индексу 1 из кортежа под индексом 0
# print(m)

# можно записать иначе
# lst = [input().split(', ') for _ in range(int(input()))]
# lst = [['Guidonia 140', 'Cecchignola 84', 'Torresina 68'], ['Guidonia 140', 'Cecchignola 84', 'Torresina 168']]
# m = [sorted([(int(city.split()[1]), city.split()[0]) for city in line])[0][1] for line in lst]
# m = ['Torresina', 'Cecchignola']

# и потом превратить в функциональный вариант
#[print(*[sorted([(int(city.split()[1]), city.split()[0]) for city in line])[0][1] for line in lst], sep=', ') for lst in [[input().split(', ') for _ in range(int(input()))]]]

# n1 = 4
# n2 = 1500
# m = []
# lst = [320, 110, 37, 42, 277, 189, 99, 84]
# for i in range(len(lst)):
#     a = lst[i] * (n1 ** 2)
#     if a <= n2:
#         m.append(a)
# print(len(m))

# Уничтожение популяции.
# n = [4, 1500]
# lst = [320, 110, 37, 42, 277, 189, 99, 84]
# n1 = list(map(int, input().split(' ')))
# lst = list(map(int, input().split(', ')))
# print(len([i for i in lst if i * (2 ** n1[0]) <= n1[1]]))



# с помощью ASCII таблицы, заполняем списки латиницей и кирилицей + символы пунктуации
# latin_signs = [chr(i) for i in range(32, 127)]
#
# ru_signs = [chr(i) for i in range(32, 65)]
# ru_signs += [chr(i) for i in range(1040, 1104)]
# ru_signs += [chr(i) for i in range(91, 97)]
# ru_signs += [chr(i) for i in range(123, 127)]
#
# # вычисляем по первым двум знакам на каком языке пользователь ввел фразу
# for i in phrase[:2]:
#     if i not in latin_signs:
#         set_symbols = ru_signs
#     else:
#         set_symbols = latin_signs

# print(*[chr(i) for i in [72, 69, 76, 76, 79, 58, 41]], sep='')

# d = {'Константная': 'O(1)',
#      'Линейная': 'O(n)',
#      'Квадратичная': 'O(n^2)',
#      'Кубическая': 'O(n^3)',
#      'Логарифмическая': 'O(log n)'
# }
# print(*[d[i] for i in iter(input, 'Я запомнил')], 'Молодец, Вася!', sep='\n')  # вводимое значение в iter находит в словаре


# arr = [1351, 1, 18, 29, 34, 12, 9, 0, 128, 62]
# сортиврока выбором
# for i in range(len(arr)-1):
#     idx = i
#     for j in range(i + 1, len(arr)):
#         if arr[j] < arr[idx]:
#             idx = j
#     arr[i], arr[idx] = arr[idx], arr[i]
# print(arr)

# сортировка вставками
# for i in range(1, len(arr)):
#     save = arr[i]     # первый элемент из неотсортированой части списка
#     j = i
#     while j != 0 and arr[j-1] > save:
#         arr[j] = arr[j-1]
#         j -= 1
#     arr[j] = save
# print(arr)

# сортиврока пузырьком
# j = len(arr) - 1
# is_not_ordered = True
# while is_not_ordered:
#     is_not_ordered = False
#     for i in range(j):
#         if arr[i] > arr[i+1]:
#             arr[i], arr[i+1] = arr[i+1], arr[i]
#             is_not_ordered = True
#     j -= 1
# print(arr)
# другая версия пузырьковой сортировки
# for i in range(len(arr)-1):
#     for j in range(len(arr) - i - 1):
#         if arr[j] > arr[j+1]:       # если порядок элементов не правильный
#             arr[j], arr[j+1] = arr[j+1], arr[j]     # то меняем местами пары элементов местами
# print(arr)




# Уничтожение популяции вместо чисел, указать индексы.
# num = list(map(int, input().split(' ')))
# n, k = map(int, input().split())
# # n, k = 4 1500
# lk = [int(i) * 2 ** n for i in input().split(', ')]
# lk = [5120, 1760, 592, 672, 4432, 3024, 1584, 1344]
# lb = [j + 1 for j in range(len(lk)) if lk[j] <= k]
# lb = [3, 4, 8]

# n = list(map(int, input().split(' ')))
# s = list(map(int, input().split(',')))
# m, m2 = [], []
# for i in range(len(s)):
#     if s[i] * (2 ** n[0]) <= n[1]:
#         m.append(s[i])
#         for j in range(len(m)):
#             if s[i] == m[j]:
#                 a = s.index(m[j])
#                 m2.append(a+1)
#             print(m2)



# Подсчет отрицательных.
# s = list(map(int, input().split(' ')))
# arr = [320, 110, -37, 42, -277, 189, -99, 84, -10, 87, 73]
#
# def counting_sor(arr):
#     min_elem = min(arr)
#     max_elem = max(arr)
#     support = [0 for i in range(max_elem - min_elem + 1)]
#     for i in arr:
#         support[i - min_elem] += 1
#     index = 0
#     for i in range(len(support)):
#         for j in range(support[i]):
#             arr[index] = i + min_elem
#             index += 1
#     return None
#
# arr = list(map(int, input().split(' ')))
# counting_sor(arr)
# print(arr)


# function
# def factorial(n):
#     t = 1
#     for i in range(1, n+1):
#         t *= i
#     return t
#
# def factorial_two(a, b):
#     t = 0
#     for i in range(a, b+1):
#         t += factorial(i)
#     return t
# print(factorial_two(int(input()), int(input())))


#
# def factorial(n):
#     t = 1
#     for i in range(1, n+1):
#         t *= i
#     return t
#
# def fib(n):
#     a = 0
#     b = 1
#     for i in range(1, n+1):
#         i = a
#         b += a
#         a, b = b, a
#     return a
#
# n = int(input())
# print(factorial(n) + fib(n))


# # Перестановки разрешены!
# функция 1. маx число из цифр
# def reverse_n(n):
#     m = []
#     n = abs(n)
#     while n != 0:
#         last = n % 10
#         n = n // 10
#         m.append(last)
#         m.sort(reverse=True)
#     return ''.join(map(str, m))
# # num = 294 => 942
#
# функция 2. список переводит в числа
# def str_int(s):
#     for i, elem in enumerate(s):
#         s[i] = int(elem)
#     return s
# # string = ['942', '543', '781', '50', '184']  => [942, 543, 781, 50, 184]
#
# # код
# m = []
# m1 = []
# for i in range(int(input())):
#     n = int(input())
#     m1.append(n)        # список с входными данными
#     func1 = reverse_n(n)        # функция 1
#     m.append(func1)             # список с измененными мах числами
#     func2 = str_int(m)      # функция 2
#     index = m.index(max(func2))   # нахождение индекса мах числа
# print(m1[index])



# Называем переменные правильно.
# функция убирает нижнее подчеркивание и определяет 1 символ на цифрку, и на содрежание букв/цифр
# def check_variable(v):
#     v = v.replace('_', '')
#     if v.isalnum() == True and v[0].isdigit() != True:
#         return 'Можно использовать'
#     else:
#         return 'Нельзя использовать'
#
# v = input()
# while v != 'Поработали, и хватит':
#     print(check_variable(v))
#     v = input()


# Бинарный аукцион.
# def winner(abcde):
#     index = a.index(max(abcde))
#     sp = {
#     0: 'Первый',
#     1: 'Второй',
#     2: 'Третий',
#     3: 'Четвертый',
#     4: 'Пятый'
#     }
#     return sp[index]
#
# a = list(map(int, input().split()))
# if len(a) <= 5:
#     print(winner(a))
# else:
#     print('#$%#&$^#@!')



# Жадность – корень всех зол.
# def weight(a):
#     t = 0
#     for i in range(len(a)):
#         t += a[i]
#     return t
#
# treasures = list(map(float, input().split()))
# max_weight = int(input())
#
# if weight(treasures) > max_weight:
#     print('Не повезло')
# else:
#     print('Повезло')


# Корректная дата.
# def str_int(s):           # функция для изменения строки в числа '19.12.1990' => [19, 12, 1990]
#     s = list(map(int, s.split('.')))
#     for i, elem in enumerate(s):
#         s[i] = int(elem)
#         return s
#
# def years(year):         # проверка на високосность
#     if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#         return True
#     else:
#         return False
#
# def days(a, b, c):         # проверка на день и месяц + високосный год для февраля
#     if a <= 30 and b == 4 or a <= 30 and b == 6 or a <= 30 and b == 9 or a <= 30 and b == 11:
#         return 'Корректная'
#     if a <= 31 and b == 1 or a <= 31 and b == 3 or a <= 31 and b == 5 or a <= 31 and b == 7 or a <= 31 and b == 8 or a <= 31 and b == 10 or a <= 31 and b == 12:
#         return 'Корректная'
#     if (a <= 29 and b == 2 and years(c) == True) or a <= 28 and b == 2:
#         return 'Корректная'
#     else:
#         return 'Некорректная'
#

# date = input()            # блок программы
# t = 0
# while date != '.':
#         print(days(str_int(date)[0], str_int(date)[1], str_int(date)[2]))
#         if days(str_int(date)[0], str_int(date)[1], str_int(date)[2]) == 'Корректная':
#             t += 1
#         date = input()
# print(t)



# Необычная сортировка.
# def summ(n):
#     t = 0
#     while n != 0:
#         last = n % 10
#         n = n // 10
#         t += last
#     return t
#
# list_num = list(map(int, input().split()))
# list_sum = []
# for i in range(len(list_num)):
#     a = summ(list_num[i])
#     list_sum.append(a)
#
# unity = zip(list_sum, list_num)
# unity_sort = sorted(unity, key=lambda x: x[0])     # обьединяет два списка в один [27, 156305340] и сортирует по элементу [0]
# list_us_0 = [unity[0] for unity in unity_sort]                 # вывод списка [0] => [27, 28, 34 , ..]
# list_us = [unity[1] for unity in unity_sort]                 # вывод списка [1] => [156305340, 295011343, 856232107б]
#
# print(*list_us)


# Циклический сдвиг.
# def shift_list(lst, shift=0):
#     a = shift % len(lst)     # бирающую часть сдвига, кратную длине списка, в случае, если сдвиг больше длины списка.
#     return lst[-a:] + lst[:-a]
# # s = list(map(int, input().split()))
# # n = int(input())
# # print(*shift_list(s, n))



# Системы счисления. Этап 1.
# def binary_to_decimal(n):
#     m = []
#     while n != 0:
#         a = n
#         if a % 2 == 0:
#             a = '0'
#             m.append(a)
#         elif a % 2 != 0:
#             a = '1'
#             m.append(a)
#         n = n // 2
#     m.reverse()
#     return ''.join(m)
#
# def decimal_to_binary(s):
#     t = 0
#     s = s[::-1]
#     for i, elem in enumerate(s):
#         elem = int(elem)
#         a = elem * (2 ** i)
#         t += a
#     return t

# функция факториала.
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
#
# # функция аккермана.
# def func_akkermana(m, n):
#     if m == 0:
#         return n + 1
#     if m > 0 and n == 0:
#         return func_akkermana(m-1, 1)
#     if m > 0 and n > 0:
#         return func_akkermana(m - 1, func_akkermana(m, n - 1))




# Цифры числа.
# def digits(n):
#   if n < 10:   # если число меньше 10, то отправляется в строку
#     return str(n)
#   else:
#     return digits(n // 10) + ' ' + str(n % 10)  # 12 + 3

# Длина объекта
# def get_length(obj):
#   if obj in [[], (), '']:        # или if not obj
#     return 0                # 0 прибавляется в конце (плюсуется к 1)
#   else:
#     return get_length(obj[1:]) + 1  # делает срез из [1, 2, 3] => [2, 3]

# Степень двойки.
# from math import log
# Logn = log(n, 2)
# if Logn == int(log(n, 2)):
#   print("True")
# else:
#   print('False')
#
# a = [True if Logn == int(log(n, 2)) else False]

# def is_power(n):
#   if n == 2:
#     return True
#   elif n < 2:
#     return False
#   else:
#     return is_power(n/2)
# print(is_power(1))


# Быстрое возведение в степень.
# def get_pow(a, n):
#   if n == 0:
#     return 1
#   elif n % 2 == 0:
#     return get_pow(a, n/2)**2
#   else:
#     return a * get_pow(a, n-1)
# print(get_pow(2,3))

# def get_pow(a, n):
#   if n == 0:
#     return 1
#   elif n == 1:
#     return a
#   elif n % 2 != 0:
#     return a * get_pow(a, n-1)
#   elif n % 2 == 0:
#     return get_pow(a*a, n/2)
# print(get_pow(2,3))

# def get_pow(a, n):
#   if n == 0:
#     return 1
#   elif n == 1:
#     return a
#   elif n % 2 == 0:
#     return get_pow(a*a, n/2)
#   elif n % 2 != 0:
#     return a * get_pow(a, n-1)
#
# print(get_pow(2,3))



# Кэширование
# ФИБОНАЧЧИ
# рекурсия
# fib = lambda n: fib(n-1) + fib(n-2) if n > 2 else 1

# запоминание
# M = {0: 0, 1: 1}
# def fib(n):
#     if n in M:      # исключает повторение рекурсии
#         return M[n]
#     M[n] = fib(n - 1) + fib(n - 2)
#     return M[n]

# динамическое программирование
# def fib(n):
#   a = 0
#   b = 1
#   for _ in range(n):
#     a, b = b, a+b
#   return a


# MATRIX.
# m = 2   # длинна
# n = 3   # строки
# row = [0] * m

#a = []
# матрица имеет вид [[0, 0], [0, 0], [0, 0]]
# for i in range(n):
#     a.append([0]*m)
# print(a)

# a = [ [0]*m for i in range(n) ]
# for i in a:
#     for elem in i:
#         print(elem, end=' ')
#     print()

# для вывода одной строки матрицы, можно использовать метод join
# row in a
# print(' '.join(list(map(str, row))))


# m = 5
# n = 4
# a = [[0]*m for i in range(n)]
# # a[0][1] = 1
# # a[0][3] = 1
#
# # a[1][0] = 1
# # a[1][2] = 1
# # a[1][4] = 1
#
# # a[2][1] = 1
# # a[2][3] = 1
#
# # a[3][0] = 1
# # a[3][2] = 1
# # a[3][4] = 1
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         if (i % 2 == 0 and j % 2 != 0) or (i % 2 != 0 and j % 2 == 0):
#             a[i][j] = 1
#         print(a[i][j], end=' ')
#     print()


# №1.
#n, m = map(int, input().split())
# m = [[1, 2], [3, 4], [5, 6]]
# print(m)
# trans = [[0 for j in range(len(m))] for i in range(len(m[0]))]
# print(trans)
# for i in range(len(m)):
#   for j in range(len(m[0])):
#     trans[j][i] = m[i][j]
# print(m)
# print(trans)


# №2.
# n = 4
# a = []
# for i in range(n):              # Заполнение матрицы значениями с клавиатуры
#   a.append(list(map(int, input().split())))     # # метод list() создает список(массив)
#                                                 # из набора данных, указанных в скобках
#
# trans_m = [[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]     #  Внешний цикл предназначен для строк, а вложенный – для столбцов.
#
# for i in trans_m:       # Вывод двумерных массивов, по значениям массива
#   for j in i:
#     print(j, end=' ')
#   print()

# №3. сумма чисел матрицы
# n, m = map(int, input().split())
# a = []
# t = 0
# for i in range(n):
#   a.append(list(map(int, input().split())))
# for i in a:
#   for j in i:
#     t += j
# print(t)


# MATRIX.
# import sys
# #s = sys.stdin.readlines()
# #l = [list(map(int, x.strip().split())) for x in s]
# # [[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]]
# a = [[1, 0, 0, 0, 0], [0, 0, 1, 0, 1], [0, 0, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 0, 0]]
# flag = 'ДА'
# for i in range(1, len(a)-1):
#   for j in range(1, len(a)-1):
#     if a[i][j]:
#       if a[i][j+1] or a[i+1][j] or a[i+1][j+1]:
#        flag = 'НЕТ'
#        break
#   if not flag:
#     break
#
# print('ДА' if flag else 'НЕТ')



# Телефонная книга. Этап 1.
# tel = {}
# s = input()
# while s != '.':
#     two_s = s.split()
#     if len(two_s) == 2:
#         tel[two_s[0]] = two_s[1]
#     else:
#         print(tel[s])
#     s = input()


# Словарь программиста.
# s = input().split(' – ')
# sl = {}
# while s != ['.']:
#     sl[s[0].rstrip()] = s[1:]
#     s = input().split(' – ')
# print(sl)
#
# for i in range(int(input())):
#     s1 = input()
#     if s1 not in sl:
#         print('Не найдено')
#     else:
#         print(*sl[s1])


# Маленький частотный анализ.
# import string
# text = input().lower().split(' ')
# t = 0
# text = [''.join(c for c in s if c not in string.punctuation) for s in text]     # удаление знаков препинания в СПИСКЕ
# counts = {}
# for i in text:
#     counts[i] = counts.get(i, 0) + 1          # создание словаря с кол-вом повторений слов в списке
#
# key_max = max(counts, key=counts.get)         # нахождение ключа с мах значением
# print(key_max, counts[key_max])


# Права доступа.
# d_r = {
#     # {KEY: {key: [value_1, ... value_n]}}
#     # {ПОЛЬЗОВАТЕЛЬ: {действие: [тип_ф_1, ... тип_ф_n]}}
#     'admin': {'read': ['confidential', 'settings', 'system', 'ordinary'],
#               'edit': ['confidential', 'settings', 'system', 'ordinary']},
#     'experienced': {'read': ['settings', 'system', 'ordinary'],
#                     'edit': ['ordinary']},
#     'user': {'read': ['ordinary'],
#              'edit': ['ordinary']}
# }
#
# # d = {}      # cловарь файлов
#             # {имя_файла: тип}
#
# # a = input().split(' ')     # название файла а[0] - имя файла, а[1] - тип
# # while a != ['.']:
# #     d.setdefault(a[0], a[1])
# #     # {'revenue_data.txt': 'confidential'}
# #     a = input().split(' ')
#
# # user = input().split(' ')    # имя_файла действие ПОЛЬЗОВАТЕЛЬ (имя_файла - action[0], действие - action[1],
# # # ПОЛЬЗОВАТЕЛЬ - action[2]
# # # ['driver.drv', 'read', 'admin']
# # while user != ['.']:
# #     if d.get(user[0]) in d_r[user[2]].get(user[1]):   # если тип файла, полученный
# # # из d по ключу "имя файла", находится в значениях d_r по ключам "ПОЛЬЗОВАТЕЛЬ" и "действие"
# #         print('Access granted')
# #     else:
# #         print('Access denied')
# #     user = input().split(' ')


# Телефонная книга. Этап 2.
# d = {}
# s = input().replace(',', '').split(' ')
# while s != ['.']:
#     if len(s) >= 2:                 # если длина строки больше 2х (Ben 8123, +123, ......)
#         for key in d.keys():        # индекс key для всех ключей
#             if s[0] in key:            # если s[0] ('Ben') есть в списке
#                 d[s[0]] += s[1:]        # то добавляем в значения список после имени
#                                         # [89001234050, +70504321009]
#         else:
#             d.setdefault(s[0], s[1:])       # если ['Alice', '210-220'], то добавляем в словарь
#             # {'Alice': ['210-220']}
#
#     if len(s) == 1:                 # если длинга строки равне 1 (Ben)
#         if s[0] in d.keys():        # если s[0] ('Ben') есть в ключах
#             print(*d.get(s[0]), sep=', ')      # то делаем вывод по ключу s[0]
#         else:
#             print('Не найдено')         # иначе не найдено
#
#     s = input().replace(',', '').split(' ')



# Инверсия справочника.
# создаем словарь из стран и столиц
# d = {}
# s = input().split(': ')
# while s != ['.']:
#     d.setdefault(s[0], s[1])
#     s = input().split(': ')
# # ответы
# s1 = input()
# while s1 != '.':
#     if s1 in d.keys():      # если s1 есть в ключах, то вывод значение
#         print(d.get(s1))
#     elif s1 in d.values():      # если s1 есть в значениях
#         for i, elem in d.items():       # через цикл находим ключ по значению
#             if s1 == elem:          # если s1 равен значению, вывод ключа
#                 print(i)
#     else:
#         print('Нет данных')
#     s1 = input()



# Жаркий аукцион.
# prod = input().split(', ')                      # товар
# price = int(input())                            # цена
# name = input().split(', ')                      # участники
#
# prod_price = dict.fromkeys(prod, price)        # словарь с товаром и ценой
# name_prod = dict.fromkeys(name, 0)             # словарь с участником, по умолчанию задано 0
# # аукцион
# auction = input().split()
# while auction != ['Аукцион', 'закончен!']:
#     ar = ' '.join(auction[1:-1])                        # срез с поступающего значения Jane [Macintosh LC520] 5000
#
#     if auction[0] in name_prod.keys():                  # если срез [Jane] находится в словаре (имя/товар) (ключ)
#         if int(auction[-1]) > prod_price.get(ar):           # если цена больше > price
#             prod_price[ar] = int(auction[-1])                   # price = новая цена
#
#             if ar in name_prod.values():                # если срез [Macintosh LC520] находится в словаре в виде ЗНАЧЕНИЯ
#                 for key, val in name_prod.items():          # поиск среди ключей/значений
#                     if ar == val:                                  # если срез с названием уже есть в словаре
#                         name_prod[key] = 0                              # то присваивается значение 0
#             name_prod[auction[0]] = ar                  # если среза нет, то значение добавляется
#     auction = input().split()
#
# def get_key(val):                                       # функция по поиску значения, в словаре имя/товар
#     for key, value in name_prod.items():
#         if val == value:                                # если входящее значение есть в словаре
#             return key                                      # дать ключ
#
# for key, val in prod_price.items():
#     if key not in name_prod.values():                   # если ключа нет в значениях словаря имя/товар
#         val = 'Предложений не было'                         # придать значение "Предложений не было" вместо 1500
#         print(key, val)                                         # напечатать
#     else:                                               # если ключ есть
#         print(key, get_key(key), val)                          # то печатать ответ + без None, тк not in



# Bookflix.
import string

# text = 'Булгаков "Собачье сердце" (сатира), Толкин "Властелин колец" (фэнтези), Дойл "Затерянный мир" (научная фантастика), Кристи "Десять негритят" (детектив), Кинг "Сияние" (ужасы), Дойл "Отравленный пояс" (научная фантастика), Лавкрафт "Зов Ктулху" (ужасы), Лутц "Изучаем Python" (учебная литература), Рао "C++ за 21 день" (ужасы), Толкин "Хоббит" (фэнтези), Дойл "Долина ужаса" (детектив), Кинг "Оно" (ужасы), Кристи "Убийство в доме викария" (детектив), Кинг "Противостояние" (ужасы), Вейер "Марсианин" (научная фантастика)'.replace(',', '"').split('"')
text = 'Булгаков "Собачье сердце" (фэнтези), Толкин "Властелин колец" (фэнтези), Дойл "Затерянный мир" (научная фантастика)'.replace(',', '"').split('"')
ls = [''.join(i for i in x if i not in string.punctuation)for x in text]       # убираем все знаки препинания => ['Булгаков ', 'Собачье сердце', ' сатира']
ls1 = [ls[i].strip() for i in range(len(ls))]                                  # избавляемся от пробелов => ['Булгаков', 'Собачье сердце', 'сатира']
# print(ls1)

a = [ls1[i] for i in range(0, len(ls1), 3)]
print(a)
n = [ls1[i] for i in range(1, len(ls1), 3)]
j = [ls1[i] for i in range(2, len(ls1), 3)]

m = []
for i in range(2, len(ls1), 3):
    if ls1[i] not in m:
        m.append(ls1[i])
md = dict.fromkeys(m, '')
print(md)



m1 = []

for i in range(0, len(ls1), 3):
    if ls1[i] not in m1:
        m1.append(ls1[i])
md1 = dict.fromkeys(m)








#ja = dict(zip(a, n))







# # ['Булгаков', 'Собачье сердце', 'сатира']
# d.setdefault(ls1[2], [ls1[0], ls[1]])
# # # {'Булгаков ': 'Собачье сердце'}
# print(d)





# ввод книг
# text = input().split()
# while text != ['.']:
#     text = input().split()
