---
## Front matter
title: "Лабораторная работа No 6."
author: "Тагиев Байрам Алтай оглы"

## Generic otions
lang: ru-RU
toc-title: "Содержание"

## Bibliography
bibliography: bib/cite.bib
csl: pandoc/csl/gost-r-7-0-5-2008-numeric.csl

## Pdf output format
toc: true # Table of contents
toc-depth: 2
lof: true # List of figures
lot: true # List of tables
fontsize: 12pt
linestretch: 1.5
papersize: a4
documentclass: scrreprt
## I18n polyglossia
polyglossia-lang:
  name: russian
  options:
	- spelling=modern
	- babelshorthands=true
polyglossia-otherlangs:
  name: english
## I18n babel
babel-lang: russian
babel-otherlangs: english
## Fonts
mainfont: PT Serif
romanfont: PT Serif
sansfont: PT Sans
monofont: PT Mono
mainfontoptions: Ligatures=TeX
romanfontoptions: Ligatures=TeX
sansfontoptions: Ligatures=TeX,Scale=MatchLowercase
monofontoptions: Scale=MatchLowercase,Scale=0.9
## Biblatex
biblatex: true
biblio-style: "gost-numeric"
biblatexoptions:
  - parentracker=true
  - backend=biber
  - hyperref=auto
  - language=auto
  - autolang=other*
  - citestyle=gost-numeric
## Pandoc-crossref LaTeX customization
figureTitle: "Рис."
tableTitle: "Таблица"
listingTitle: "Листинг"
lofTitle: "Список иллюстраций"
lotTitle: "Список таблиц"
lolTitle: "Листинги"
## Misc options
indent: true
header-includes:
  - \usepackage{indentfirst}
  - \usepackage{float} # keep figures where there are in the text
  - \floatplacement{figure}{H} # keep figures where there are in the text
---

# Цель работы

Освоить на практике применение режима однократного гаммирования.

# Выполнение лабораторной работы

1. Напишем функцию для генерации случайной последовательности, которая будет являться нашим ключем.

```python
import random

def generate_key_hex(word):
    key = ""
    for _ in range(len(word)):
        key += random.choice("0123456789abcdef")
    return key

```

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

5. После запуска программы мы получим следующее. 

```
Ключ: dc924107ba191baa4710c3
Зашифрованный текст: хCФЌІѺЌѱџЅЇЍNAѕѴѴІѼЬ
Дешифрованный текст: С Новым Годом, друзья!
Возможные ключи: ['dc92410', 'ѢЄ\x118HGЫ',
```

# Выводы

По мере выполнения лабораторной работы были выполнены все цели.
