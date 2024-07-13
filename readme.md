# Для удобства использовал подключение через SSH

![alt text](img/image.png)

# Задание

## Задание 1

Создаём два файла:

![alt text](img/image-1.png)

Далее заполняем эти два файла случайными животными(можно через cat в терминале, но поскольку есть ssh удобнее через vscode):

![alt text](img/image-2.png)

![alt text](img/image-3.png)

Теперь объединяем два файла в один:

![alt text](img/image-4.png)

Если смотреть содержимое в терминале: 

![alt text](img/image-5.png)

Переименование через терминал:

![alt text](img/image-6.png)

![alt text](img/image-7.png)

## Задание 2

Создаём дерикторию и перемещаем файл туда:

![alt text](img/image-8.png)

![alt text](img/image-9.png)

Если необходимо, проверка через терминал:

![alt text](img/image-10.png)

## Задание 3

Поскольку на Linux у меня не было ничего из SQL поставлю всё с нуля:

![alt text](img/image-12.png)

Теперь ставим сам MySQL из репо, добавленного в apt

![alt text](img/image-13.png)

Думаю весь процесс загрузки вставлять не нужно, оставил конец:

![alt text](img/image-14.png)

Проверяем статус: 

![alt text](img/image-15.png)

## Задание 4

Насколько я понимаю оно и так выполнено в задании 3, осталось только удалить пакет:

![alt text](img/image-16.png)

Теперь проверим грепом что пакета не осталось:

![alt text](img/image-17.png)

## Задание 5 

Историю команд сохранил в файл, однако там не только финальные команды попавшие в отчёт, но и неудачные попытки (были проблемы с некоторыми репозиториями).

Так же там сохранилась история с прошлых заданий, история для текущего задания начинается со строки 199-200.

![alt text](img/image-18.png)

## Задание 6

Для диаграммы использовал draw.io, чтобы не захламлять сократил кол-во представителей классов до необходимого в задании 

![alt text](img/image-19.png)

## Задание 7 

Захожу в MySQL под рутом и создаю базу:

![alt text](img/image-20.png)

## Задание 8

Создаём таблицы в соответсвии с иерархией

Для всех животных: 

![alt text](img/image-21.png)

Для дочерних:

![alt text](img/image-22.png)

![alt text](img/image-23.png)

Для Конкретных видов:

![alt text](img/image-24.png)

### На всякий случай описание таблиц:

![alt text](img/image-25.png)

## Задание 9 

Создаем столбцы под данные в низших таблицах:

![alt text](img/image-27.png)

Теперь заполняем столбцы:

![alt text](img/image-26.png)

## Задание 10

Удаляем верблюдов(как я понимаю именно конкретного верблюда а не таблицу целиком):

![alt text](img/image-28.png)

Создаём таблицу под объединение лошадей и ослов:

![alt text](img/image-29.png)

Теперь вставляем данные из таблиц, затем удаляем их

![alt text](img/image-30.png)

## Задание 11

Создаем таблицу молодые_животные:

![alt text](img/image-31.png)

Вносим всех попавших(перед этим специально добавил животных подходящих под условия):

![alt text](img/image-32.png)

Результат:

![alt text](img/image-33.png)

## Задание 12

Создаём таблицу для объединения

![alt text](img/image-34.png)

Переносим данные из старых таблиц:

![alt text](img/image-35.png)

Результат:

![alt text](img/image-36.png)

## Задание 13-15 

В файле AnimalReg.py.