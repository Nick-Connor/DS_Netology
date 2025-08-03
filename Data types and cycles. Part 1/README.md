# Задание 1
Дана переменная, в которой хранится слово из латинских букв. Напишите код, который выводит на экран:  

- среднюю букву, если число букв в слове нечетное;  
- две средних буквы, если число букв четное.  

Примеры работы программы:  
=
word = 'test'  
Результат:es  
=
word = 'testing'  
Результат:t  

# Task 1
A variable is given in which a word of Latin letters is stored. Write the code that outputs to the screen:  

- the middle letter, if the number of letters in the word is odd;  
- two middle letters, if the number of letters is even.  

Program examples:
=
word = 'test'  
Result:es  
=
word = 'testing'  
Result:t

***

# Задание 2
Напишите программу, которая последовательно запрашивает у пользователя числа (по одному за раз) и после первого нуля выводит сумму всех ранее введенных чисел.  

Примеры работы программы:

Введите число:1  

Введите число:4  

Введите число:6  

Введите число:0  

Результат:11  


# Task 2
Write a program that sequentially asks the user for numbers (one at a time) and outputs the sum of all previously entered numbers after the first zero.  

Examples of how the program works:

Enter a number:1  

Enter a number:4  

Enter a number:6  

Enter a number:0  

Result:11

***

# Задание 3
Мы делаем MVP dating-сервиса, и у нас есть список парней и девушек.
Выдвигаем гипотезу: лучшие рекомендации мы получим, если просто отсортируем имена по алфавиту и познакомим людей с одинаковыми индексами после сортировки! Но мы не будем никого знакомить, если кто-то может остаться без пары:

Примеры работы программы:  
-
boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']  
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']  
Результат:
-
Идеальные пары:    
Alex и Emma    
Arthur и Kate  
John и Kira  
Peter и Liza  
Richard и Trisha
boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard', 'Michael']  
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']  
-
Результат:   
Внимание, кто-то может остаться без пары!  

# Task 3
We are making an MVP of a dating service, and we have a list of guys and girls.
We hypothesize that we will get the best recommendations if we simply sort the names alphabetically and introduce people to the same indexes after sorting! But we won't introduce anyone if someone might be left without a date.:

Examples of the program:
-
boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']  
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']  
Result:
-
Perfect couples:    
Alex and Emma    
Arthur and Kate  
John and Kira  
Peter and Liza  
Richard and Trisha
boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard', 'Michael']  
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
-
Result:   
Attention, someone may be left without a pair!

***

# Задание 4

У нас есть список, содержащий информацию о среднедневной температуре в Фаренгейтах за произвольный период по странам (структура данных в примере).   

Необходимо написать код, который рассчитает среднюю температуру за период в Цельсиях(!) для каждой страны.

Пример работы программы:

countries_temperature = [  
    ['Таиланд', [75.2, 77, 78.8, 73.4, 68, 75.2, 77]],  
    ['Германия', [57.2, 55.4, 59, 59, 53.6]],  
    ['Россия', [35.6, 37.4, 39.2, 41, 42.8, 39.2, 35.6]],  
    ['Польша', [50, 50, 53.6, 57.2, 55.4, 55.4]]  
]  

Результат:  

Средняя температура в странах:  
Таиланд  -  23.9 С  
Германия  -  13.8 С  
Россия  -  3.7 С  
Польша  -  12.0 С  

# Task 4

We have a list containing information about the average daily temperature in Fahrenheit for an arbitrary period by country (the data structure in the example).   

It is necessary to write a code that will calculate the average temperature for the period in Celsius(!) for each country.

An example of how the program works:

countries_temperature = [  
    ['Thailand', [75.2, 77, 78.8, 73.4, 68, 75.2, 77]],
[' Germany', [57.2, 55.4, 59, 59, 53.6]],
[' Russia', [35.6, 37.4, 39.2, 41, 42.8, 39.2, 35.6]],
['Poland', [50, 50, 53.6, 57.2, 55.4, 55.4]]
]  

Result:  

The average temperature in the countries of
Thailand is 23.9 C  
Germany - 13.8 C  
Russia - 3.7 S  
Poland - 12.0 C

***

# Задание 5

Имеется список с транспортными номерами. Необходимо написать код, который проверит каждый номер на валидность (1 буква, 3 цифры, 2 буквы, 2-3 цифры). Обратите внимание, что не все буквы кириллического алфавита используются в транспортных номерах.  

Если номер валиден, то вывести его в нужном формавте (пример ниже), а если не валиден — вывести текст. При решении помогут регулярные выражения, с которыми будет знакомство на практике.  

Примеры работы программы:  

car_ids = ['А222ВС96', 'АБ22ВВ193']  

Результат:  

Номер А222ВС валиден. Регион: 96  
Номер АБ22ВВ193 не валиден  

# Task 5

There is a list with transport numbers. It is necessary to write a code that will check each number for validity (1 letter, 3 digits, 2 letters, 2-3 digits). Please note that not all letters of the Cyrillic alphabet are used in transport numbers.  

If the number is valid, then output it in the required format (example below), and if it is not valid, output the text. Regular expressions, which will be familiar in practice, will help with the solution.  

Examples of how the program works:  

car_ids = ['A222BC96', 'AB22BV193']  

Result:  

The A222BC number is valid. Region: 96  
The AB22BV193 number is not valid

***

# Задание 6

Дан поток логов по количеству просмотренных страниц для каждого пользователя (пользователь,дата;просмотры). Вам необходимо написать алгоритм, который считает среднее значение просмотров на пользователя. Т. е. надо посчитать отношение суммы всех просмотров к количеству уникальных пользователей. И тут регулярные выражения облегчат немного реализацию.  

Примеры работы программы:  

stream = [  
    'user4,2021-01-01;3',  
    'user3,2022-01-07;4',  
    'user2,2022-03-29;1',  
    'user1,2020-04-04;13',  
    'user2,2022-01-05;7',  
    'user1,2021-06-14;4',  
    'user3,2022-07-02;10',  
    'user4,2021-03-21;19',  
    'user4,2022-03-22;4',  
    'user4,2022-04-22;8',  
    'user4,2021-05-03;9',  
    'user4,2022-05-11;11'  
]  


Результат:  
Среднее количество просмотров на уникального пользователя: 23.25  
  
stream = [  
    'user100,2022-01-01;150',  
    'user99,2022-01-07;205',  
    'user1001,2022-03-29;81'  
]  


Результат:  
Среднее количество просмотров на уникального пользователя: 145.33  

# Task 6

A log stream is given by the number of pages viewed for each user (user, date; views). You need to write an algorithm that calculates the average number of views per user. That is, you need to calculate the ratio of the sum of all views to the number of unique users. And here regular expressions will make the implementation a little easier.  

Examples of how the program works:  

stream = [  
    'user4,2021-01-01;3',  
    'user3,2022-01-07;4',  
    'user2,2022-03-29;1',  
    'user1,2020-04-04;13',  
    'user2,2022-01-05;7',  
    'user1,2021-06-14;4',  
    'user3,2022-07-02;10',  
    'user4,2021-03-21;19',  
    'user4,2022-03-22;4',  
    'user4,2022-04-22;8',  
    'user4,2021-05-03;9',  
    'user4,2022-05-11;11'  
]  


Result:  
Average number of views per unique user: 23.25  
  
stream = [  
    'user100,2022-01-01;150',  
    'user99,2022-01-07;205',  
    'user1001,2022-03-29;81'  
]  


Result:  
Average number of views per unique user: 145.33