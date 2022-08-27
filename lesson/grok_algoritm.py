
# ГЛАВА 1.Бинарный поиск.
# функция получает отсортированный массив и значение
# если значение присутствует в массиве, то функция возвращает его позицию
# def binary_search(list, item):     # в переменных low and high
#     low = 0                        # хранятся границы той части списка в которой выполняется поиск
#     high = len(list) - 1
#     while low <= high:          # пока эта часть не сократится до одного элемента..
#         mid = (low + high) // 2    # ...проверяем средний элемент (1 + 9) // 2
#         guess = list[mid]
#         if guess == item:       # значение найдено
#             return mid
#         if guess > item:        # много
#             high = mid - 1
#         else:                   # мало
#             low = mid + 1
#     return None                 # значение не существует
#
# my_list = [1, 3, 5, 7, 9, 10, 15, 20, 30]
# print(binary_search(my_list, 9))   # ответ будет индекс 3 равен 1
# print(binary_search(my_list, -1))

# ГЛАВА 2. Сортировка выбором.
# Сортировка выбором
# def find_Smallest(arr):
#     smallest = arr[0]          # для хранения наименьшего значения
#     smallest_index = 0          # для хранения индекса наименьшего значения
#     for i in range(1, len(arr)):
#         if arr[i] < smallest:
#             smallest = arr[i]
#             smallest_index = i
#     return smallest_index           # индекс наименьшего числа
#
# # функция сортировки выбором
# def selectionSort(arr):     # сортируем массив
#     newArr = []
#     for i in range(len(arr)):
#         smallest = find_Smallest(arr)   # находит наименьший элемент в массиве
#         newArr.append((arr.pop(smallest)))  # и добавляет в новый массив
#     return newArr
#
# print(selectionSort([5, 3, 6, 2, 10]))


# ГЛАВА 3. Рекурсия.
# обратный отчет
# def countdown(i):
#     print(i)
#     if i <= 0:
#         return
#     else:
#         countdown(i - 1)

# def greet(name):
#     print('hello', name,'!')
#     greet2(name)
#     print('getting ready to say bye...')
#     bye()

# def greet2(name):
#     print('how are you,', name, '?')
# def bye():
#     print('ok bye!')


# ГЛАВА 4. Быстрая сортировка.
# найти мах число из списка
# def recurs_sum(arr):
#     if len(arr) == 2:
#         return arr[0] if arr[0] > arr[1] else arr[1]
#     sub_max = max(arr[1:])
#     return arr[0] if arr[0] > sub_max else sub_max

# код быстрой сортировки
# def quicksort(arr):
#     if len(arr) < 2:
#         return arr              # базовый случай: массивы с 0 и 1 уже отсортированы
#     else:
#         pivot = arr[0]          # рекурсивный случай / опорная точка
#         less = [i for i in arr[1:] if i <= pivot]   # подмассив меньших
#         greater = [i for i in arr[1:] if i > pivot] # подмассив больших
#         return quicksort(less) + [pivot] + quicksort(greater)


# ГЛАВА 5. Хеш-таблицы.
book = dict()
book['milk'] = 1.49
book['avocado'] = 1.49
print(book['avocado'])