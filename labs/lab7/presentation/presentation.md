---
## Front matter
lang: ru-RU
title: Лабораторная работа No 7.
author:
  - Тагиев Б. А.
institute:
  - Российский университет дружбы народов, Москва, Россия
date: 21 октября 2023

## i18n babel
babel-lang: russian
babel-otherlangs: english

## Formatting pdf
toc: false
toc-title: Содержание
slide_level: 2
aspectratio: 169
section-titles: true
theme: metropolis
header-includes:
 - \metroset{progressbar=frametitle,sectionpage=progressbar,numbering=fraction}
 - '\makeatletter'
 - '\beamer@ignorenonframefalse'
 - '\makeatother'
---

## Цель работы

Освоить на практике применение режима однократного гаммирования.

## Выполнение лабораторной работы

1. Напишем функцию для генерации случайной последовательности, которая будет являться нашим ключем.

```python
import random

def generate_key_hex(word):
    key = ""
    for _ in range(len(word)):
        key += random.choice("0123456789abcdef")
    return key

```

## Выполнение лабораторной работы

2. Также сделаем функцию шифрования. В основе используется XOR (бинарное ИЛИ НЕТ).

```python
def encrypt(plaintext, key):
    ciphertext = ""
    for i in range(len(plaintext)):
        char = plaintext[i]
        key_char = key[i % len(key)]
        encrypted_char = chr(ord(char) ^ ord(key_char))
        ciphertext += encrypted_char
    return ciphertext
```

## Выполнение лабораторной работы

3. Аналогичный принцип стоит за дешифрованием (XOR).

```python
def decrypt(ciphertext, key):
    decrypted_text = ""
    for i in range(len(ciphertext)):
        char = ciphertext[i]
        key_char = key[i % len(key)]
        decrypted_char = chr(ord(char) ^ ord(key_char))
        decrypted_text += decrypted_char
    return decrypted_text
```

## Выполнение лабораторной работы

4. А также функция нахождения возможного ключа.

```python
def find_possible_key(ciphertext, fragment):
    possible_keys = []
    for i in range(len(ciphertext) - len(fragment) + 1):
        possible_key = ""
        for j in range(len(fragment)):
            char = ciphertext[i + j]
            fragment_char = fragment[j]
            key_char = chr(ord(char) ^ ord(fragment_char))
            possible_key += key_char
        possible_keys.append(possible_key)
    return possible_keys
```

## Выполнение лабораторной работы

5. После запуска программы мы получим следующее. 

```
Ключ: dc924107ba191baa4710c3
Зашифрованный текст: хCФЌІѺЌѱџЅЇЍNAѕѴѴІѼЬ
Дешифрованный текст: С Новым Годом, друзья!
Возможные ключи: ['dc92410', 'ѢЄ\x118HGЫ',
```

## Выводы

По мере выполнения лабораторной работы были выполнены все цели.

