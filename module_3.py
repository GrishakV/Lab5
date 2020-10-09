#!/usr/bin/env python 3
# -*- config: utf-8 -*-

import sys


if __name__ == '__main__':
    s = input('Введите предложение: ')
    n = int(input('Введите длину: '))

    # Проверить требуемую длину
    if len(s) >= n:
        print(
            "Заданная длина не может быть меньше длины предложения",
            file=sys.stderr
        )
        exit(1)

    # Разделить предложение на слова
    words = s.split(' ')
    # Проверить количество слов в предложении
    if len(words) < 2:
        print(
            "Предложение должно содержать несколько слов",
            file=sys.stderr
        )
        exit(1)

    # Количество пробелов для добавления
    delta = n
    for word in words:
        delta -= len(word)

    # Количесво пробелов на каждое слово
    w, r = delta // (len(words) - 1), delta % (len(words) - 1)

    # Сформировать список для хранения слов и пробелов
    lst = []

    # Пронумеровать все слова в списке и перебрать их
    for i, word in enumerate(words):
        lst.append(word)

        # Если слово не является последним, добавить пробелы
        if i < len(words) - 1:
            # Определить частоту пробелов
            width = w
            if r > 0:
                width += 1
                r -= 1

                # Добавть заданное количество пробелов в список
                if width > 0:
                    lst.append(' ' * width)
    # Вывести новое предложение, объединив все элементы списка lst
    print(''.join(lst))
