# # Задаем четыре вопроса пользователю: шифр-дешифр, язык, шаг, текст.
# # За каждым вопросом стоит while-проверка, что введенный ответ является корректным значением.
#
# what_direction = input('Что мы должны сделать: шифровать или дешифровать? \n').lower()
# while what_direction != 'ш' and what_direction != 'д':
#     what_direction = input('Мы шифруем или дешифруем?  \n').lower()
#
# what_language = input('Какой нужен язык: русский или английский? \n').lower()
# while what_language != 'р' and what_language != 'а':
#     what_language = input('Какой язык "русский" или "английский"? \n').lower()
#
# how_step = input('На сколько символовов мы сдвигаем буквы по алфавиту? \n')
# while how_step.isdigit() != True:
#     how_step = input('Напиши число. \n')
#
# which_text = input('Какой текст нужно использовать сейчас? \n')
# while which_text.isspace() == True:
#     which_text = ('Введи текст. \n')
#
# # Объявляем функцию с четырьмя аргументами – соответственно четырем вопросам.
# def caesar(direction, language, step, text):
# # Четыре словаря под русские и английские символы, большие и маленькие.
# # В теории можно обойтись без них и обращаться к таблице Unicode.
# # Но мне было удобнее создать свои словари.
#     upper_eng_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     lower_eng_alphabet = 'abcdefghijklmnopqrstuvwxyz'
#     upper_rus_alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
#     lower_rus_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
#
# # Объявляем цикл for. Количество итераций равно длине строки text.
#     for i in range(len(text)):
#         # Задаем локальные переменные: длину алфавита и значения словарей.
#         if language == 'р':
#             alphas = 32
#             low_alphabet = lower_rus_alphabet
#             upp_alphabet = upper_rus_alphabet
#         if language == 'а':
#             alphas = 26
#             low_alphabet = lower_eng_alphabet
#             upp_alphabet = upper_eng_alphabet
#
#         # Если text[i] является буквой:
#         if text[i].isalpha():
#             # Находим место символа text[i] в словаре upp_alphabet либо low_alphabet.
#             if text[i] == text[i].lower():
#                 place = low_alphabet.index(text[i])
#             if text[i] == text[i].upper():
#                 place = upp_alphabet.index(text[i])
#
#             # Если нужно дешифровать, то:
#             if direction == 'д':
#                 # Находим индекс для измененного символа.
#                 # Новый ндекс = Старый индекс - Шаг % Длина алфавита
#                 index = (place - int(step)) % alphas
#
#             # Если нужно зашифровать, то:
#             elif direction == 'ш':
#                 # Находим индекс для измененного символа.
#                 # Новый ндекс = Старый индекс + Шаг % Длина алфавита
#                 index = (place + int(step)) % alphas
#
#             # Выводим измененный символ.
#             if text[i] == text[i].lower():
#                 print(low_alphabet[index], end='')
#             if text[i] == text[i].upper():
#                 print(upp_alphabet[index], end='')
#
#         # Если text[i] не является буквой:
#         else:
#             # Делаем print этого символа без изменений.
#             print(text[i], end='')
#
#
# # Вызываем функцию, передавая в аргументы четыре input`а из начала кода.
# caesar(what_direction, what_language, how_step, which_text)



#################################################################################################
#################################################################################################
#################################################################################################

print('Шифр Цезаря')

lang = input('Выберете язык. Русский или английский. Введите ru или en: ')
direction = input('Что вы ходите сделать? Шифрование или дешифрование? Введите cipher или decipher: ')
if direction == 'decipher':
    question = input('Вы знаете шаг сдвига? yes или no: ')
    if question == 'yes':
        step = input('Введите шаг сдвига: ')
else:
    step = input('Введите шаг сдвига: ')
original_text = input('Введите текст: ')

ru_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'  # 32 буквы (0-31)
en_alphabet = 'abcdefghijklmnopqrstuvwxyz'  # 26 букв (0-25)
symbols = '1234567890 .,?"!\'-'

# Алгоритм шифрования
def ceasar_cipher(text, alphabet, step):
    result_text = []
    for letter in text:
        steps = alphabet.find(letter.lower()) + int(step)  # Находим сдвиг буквы
        if letter in symbols:  # Если есть символы оставляем без изменений
            result_text.append(letter)
            continue
        elif steps < len(alphabet):  # Если шаг в пределах индексов списка алфатвитов
            if steps < 0:  # Действия при расшифровки
                if lang == 'en':
                    steps += 26
                else:
                    steps += 32
            if letter == letter.upper():  # Если была прописная буква, то новая будет в том же регистре
                ch_letter = alphabet[steps]
                result_text.append(ch_letter.upper())
            else:
                ch_letter = alphabet[steps]
                result_text.append(ch_letter)
        elif steps >= len(alphabet):  # Если шаг вышел за пределы индексов списка алфатвитов
            if letter == letter.upper():
                ch_letter = alphabet[steps - len(alphabet)]
                result_text.append(ch_letter.upper())
            else:
                ch_letter = alphabet[steps - len(alphabet)]
                result_text.append(ch_letter)
    result_text = ''.join(result_text)
    return result_text


def is_valid_input(direction, lang):
    if direction == 'cipher' or direction == 'decipher':
        if lang == 'ru' or lang == 'en':
            return True
    else:
        return False


if is_valid_input(direction, lang):
    if direction == 'cipher':
        if lang == 'en':
            print(ceasar_cipher(original_text, en_alphabet, step))
        else:
            print(ceasar_cipher(original_text, ru_alphabet, step))
    elif direction == 'decipher':
        if lang == 'en':
            if question == 'yes':
                print(ceasar_cipher(original_text, en_alphabet, -(int(step))))
            else:
                for i in range(len(en_alphabet)):
                    print('Вариант', i, ceasar_cipher(original_text, en_alphabet, i))
        elif lang == 'ru':
            if question == 'yes':
                print(ceasar_cipher(original_text, ru_alphabet, -(int(step))))
            else:
                for i in range(len(ru_alphabet)):
                    print('Вариант', i, ceasar_cipher(original_text, ru_alphabet, i))
else:
    print('Вы ошиблись в вводе, повторите попытку')