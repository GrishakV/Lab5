#!/usr/bin/env python3
# -*- config: utf-8 -*-

# Вариант 7
# Дано предложение. Напечатать все его буквы и.
if __name__ == '__main__':
    p = input("Введите предложение: ")

    for i in p:
        if i == 'и':
            print(f"{i}")
