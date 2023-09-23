---
## Front matter
title: "Лабораторная работа No 3."
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

Получение практических навыков работы в консоли с атрибутами файлов для групп пользователей.

# Выполнение лабораторной работы

## Настройка пользователей, групп и папок

1. Создать пользователя guest, guest2. Добавить guest2 в группу guest. 

![Создание необходимых пользователей](image/2.png){#fig:001}

2. Зайти в сессии данных пользователей и посмотреть вывод команды `pwd`.

![pwd](image/3.png){#fig:002}

3. Проверим идентификаторы групп. Значения из `id` совпадают с `groups`.

![Группы 1](image/4.png){#fig:003}

![Группы 2](image/5.png){#fig:004}

4. В файле `/etc/group` можем наблюдать GID наших групп.

![Группы 3](image/6.png){#fig:005}

5. Обнулим права на `/home/guest/dir1` и выдадим группе `guest` права 7 на "хомяка" пользователя.

![Права](image/7.png){#fig:006}

## Таблица с правами

### Установленные права и разрешённые действия для групп

![Права файла 000](image/t1.png){#fig:007} 

![Права файла 010](image/t2.png){#fig:008} 

![Права файла 020](image/t3.png){#fig:009} 

![Права файла 030](image/t4.png){#fig:010} 

![Права файла 040](image/t5.png){#fig:011} 

![Права файла 050](image/t6.png){#fig:012} 

![Права файла 060](image/t7.png){#fig:013} 

![Права файла 070](image/t8.png){#fig:014} 

### Минимальные права для совершения операций от имени пользователей входящих в группу

![Минимальные права](image/t0.png){#fig:015} 

# Выводы

По итогам выполнения работы, я приобрел навыки работы в консоли с атрибутами файлов для групп пользователей.
