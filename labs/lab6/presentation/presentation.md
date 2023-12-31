---
## Front matter
lang: ru-RU
title: Лабораторная работа No 6.
author:
  - Тагиев Б. А.
institute:
  - Российский университет дружбы народов, Москва, Россия
date: 14 октября 2023

## i18n babel
babel-lang: russian
babel-otherlangs: english

## Formatting pdf
toc: false
toc-title: Содержание
slide_level: 2
aspectratio: 169
theme: metropolis
section-titles: true
header-includes:
 - \metroset{progressbar=frametitle,sectionpage=progressbar,numbering=fraction}
 - '\makeatletter'
 - '\beamer@ignorenonframefalse'
 - '\makeatother'
---

## Цель работы

Развить навыки администрирования ОС Linux. Получить первое практическое знакомство с технологией SELinux.

# Выполнение лабораторной работы

## Подготовка лабораторного стенда

1. Установить `Apache2` при помощи `dnf`.

```
dnf install httpd
```

## Подготовка лабораторного стенда

2. В конфигурационном файле httpd.conf прописать параметр ServerName.

![ServerName](./image/3.png){#fig:001}

## Подготовка лабораторного стенда

3. Отключить пакетный фильтр при помощи `iptables`.

![iptables](./image/4.png){#fig:002} 

## Выполнение

1. Проверим правильность работы SELinux. Должен быть выставлен режим enforcing политики targeted.

![sestatus](./image/1.png){#fig:003} 

## Выполнение

2. Запустим Apache веб-сервер.

![httpd](./image/2.png){#fig:004} 

## Выполнение

3. В списке процессов найдем httpd.

![Контекст безопасности](./image/5.png){#fig:005} 

## Выполнение

:::::::::::::: {.columns align=center}
::: {.column width="70%"}

![переключатели SELinux](./image/6.png){#fig:006} 

:::
::: {.column width="30%"}

4. Посмотрим текущее состояние переключателей SELinux для Apache2.

:::
::::::::::::::


## Выполнение

:::::::::::::: {.columns align=center}
::: {.column width="30%"}

5. Также посмотрим текущую статистику по политике.

:::
::: {.column width="70%"}

![Статистика по политике](./image/7.png){#fig:007} 

:::
::::::::::::::


## Выполнение

6. Посмотрим текущий контекст безопасности для файлов и поддиректорий в директории `/var/www`.

 - Установлен контекст `httpd_sys_script_exec_t` для cgi-скриптов, чтобы был разрешен им доступ ко всем sys-типам.

 - Установлен контекст `httpd_sys_content_t` для содержимого, которое должно быть доступно для всех скриптов httpd и для самого демона.

## Выполнение

![Контекст безопасности](./image/8.png){#fig:008} 

## Выполнение

7. В директории `/var/www/html` пусто.

![/var/www/html](./image/9.png){#fig:009} 

## Выполнение

8. В директории `/var/www/html` создавать папки может только root.

## Выполнение

9. Создадим файл `/var/www/html/test.html`.

![test.html](./image/10.png){#fig:010} 

## Выполнение

10. Проверим контекст созданного нами файла.

![test.html](./image/11.png){#fig:011} 

## Выполнение

11. Перейдем в браузер и в нем проверим доступность данного файла.

![Проверка](./image/12.png){#fig:012} 

## Выполнение

12. Изменим конекст файла, чтобы Apache не смог получить доступ.

![test.html](./image/13.png){#fig:013} 

## Выполнение

13. Проверим, что доступ к файлу стал не доступен.

![Проверка](./image/14.png){#fig:014} 

## Выполнение

14. Посмотрим логи от веб-сервера Apache.

![/var/log/messages](./image/15.png){#fig:015} 

## Выполнение

Также проверим audit.log.

![/var/log/audit/audit.log](./image/15.1.png){#fig:0151} 

## Выполнение

15. Поменяем порт, на котором работает Apache.

![Порт 81](./image/16.png){#fig:016} 

## Выполнение

16. Перезапустим веб-сервер.

![Перезапуск](./image/17.png){#fig:017} 

## Выполнение

17. В логах наблюдаем запуск сервера на 81 порту.

![/var/log/messages](./image/18.png){#fig:018} 

## Выполнение

18. Добавим порт в `semanage` для `http_port_t` и проверим его добавление

![Добавление](./image/19.png){#fig:019} 

![Проверка](./image/19.1.png){#fig:0191} 

## Выполнение

19. Ввернем контекст файлу `test.html`.

20. Удалим привязку порта.

21. Удалим файл `test.html`.

## Выводы

В результате выполнения работы я выполнил цели работы.
