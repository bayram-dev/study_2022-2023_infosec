---
## Front matter
title: "Лабораторная работа No 4."
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

Получение практических навыков работы в консоли с расширенными атрибутами файлов.

# Выполнение лабораторной работы

1. От имени пользователя `guest` определим расширенные атрибуты файла `/home/guest/dir1/file1` (@fig:001).

![lsattr](./image/1.png){#fig:001} 
 
2. Установим на файл `file1` права, разрешающие чтение и запись для владельца файла (@fig:002).

![chmod 600](./image/2.png){#fig:002} 

3. Попробуем добавить расширенный атрибут `a` от имени `guest` (@fig:003).

![chattr +a от guest](./image/3.png){#fig:003} 

4. Зайдем под рута и повторим предыдущее действие. Проверим правильность установленных атрибутов (@fig:004).

![chattr +a от root](./image/4.png){#fig:004} 

5. Выполним дозапись в `dir1/file1` (@fig:005).

![echo append (>>)](./image/5.png){#fig:005} 

6. Сотрем текущую информацию из файла `dir1/file1`. Также, попробуем переименовать файл (@fig:006).

![echo replace (>)](./image/6.png){#fig:006} 

7. Попробуем изменить права доступа к файлу (@fig:007).

![chmod 000](./image/7.png){#fig:007} 

8. Снимим атрибут `a` и повторно запустим те действия, которые приводили к ошибке (@fig:008).

![Проваленные действия после снятия расширенного атрибута](./image/8.png){#fig:008} 

# Выводы

В результате выполнения работы я повысил свои навыки использования интерфейса командой строки (CLI), познакомился на примерах с тем, как используются основные и расширенные атрибуты при разграничении доступа. Имел возможность связать теорию дискреционного разделения доступа (дискреционная политика безопасности) с её реализацией на практике в ОС Linux. Составил наглядные таблицы, поясняющие какие операции возможны при тех или иных установленных правах. Опробовал действие на практике расширенных атрибутов «а» и «i».
