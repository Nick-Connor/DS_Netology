# Задание 1

- Даны 2 переменных, в которых хранятся строки произвольной длины: phrase_1 и phrase_2.

- Напишите код, который проверяет какая из этих строк длиннее.

- Примеры работы программы:

phrase_1 = 'Насколько проще было бы писать программы, если бы не заказчики'  

phrase_2 = '640Кб должно хватить для любых задач. Билл Гейтс (по легенде)'

# Task 1

- Two variables are given in which strings of arbitrary length are stored: phrase_1 and phrase_2.

- Write a code that checks which of these lines is longer.

- Examples of how the program works:

phrase_1 = "How much easier would it be to write programs if it weren't for the customers".

phrase_2 = "640Kb should be enough for any task. Bill Gates (according to legend)".

***
# Задание 2

- Дана переменная, в которой хранится число (год). Необходимо написать программу, которая выведет, является ли данный год високосным или обычным.

- Пример работы программы: year = 2020, year = 2019
- 
# Task 2

- A variable is given in which the number (year) is stored. It is necessary to write a program that outputs whether a given year is a leap year or a regular one.

- Example of the program: year = 2020, year = 2019

***
# Задание 3
- Необходимо написать программу, которая будет запрашивать у пользователя месяц и дату рождения и выводить соответствующий знак зодиака.

- Пример работы программы:
Введите день:
30
Введите месяц:
Август
Результат:
Ваш знак зодиака: Дева

# Task 3
- It is necessary to write a program that will ask the user for the month and date of birth and display the corresponding zodiac sign.

- An example of how the program works:
Enter the day:
30
Enter the month:
August
Result:
Your zodiac sign: Maid

***
# Задание 4

- Вам нужно написать программу для подбора упаковок по размерам товара. Размеры (ширина, длина, высота) хранятся в переменных (в сантиметрах):

- Используйте следующие правила:
<br> - если каждое из трех измерений менее или равно 15 сантиметрам, то выведите на экран "Коробка №1";
<br> - если хотя бы одно из измерений больше 2 метров, то выводите "Упаковка для лыж";
<br> - если хотя бы одно из измерений больше 15 сантиметров, но менее 50 сантиметров, то выводите "Коробка №2";
<br> - во всех остальных случаях выводите "Коробка №3".
- Пример работы программы:

ширинf (width) = 15;  
длина (length) = 55;  
высота (height) = 15;  
Результат:  
Коробка №3

# Task 4

- You need to write a program for selecting packages according to the size of the product. Dimensions (width, length, height) are stored in variables (in centimeters):

- Use the following rules:
<br> - if each of the three measurements is less than or equal to 15 centimeters, then display "Box No. 1" on the screen;
<br> - if at least one of the measurements is more than 2 meters, then print "Ski packaging";
<br> - if at least one of the measurements is more than 15 centimeters, but less than 50 centimeters, then print "Box No. 2";
<br> - in all other cases, print "Box number 3".
- An example of how the program works:

widthf (width) = 15;
length = 55;
height = 15;  
Result:  
Box No. 3

***
# Задание 5

- Дана переменная, в которой хранится шестизначное число (номер проездного билета).
- Напишите программу, которая будет определять, является ли данный билет "счастливым". Билет считается счастливым, если сумма первых трех цифр совпадает с суммой последних трех цифр номера.

- Примеры работы программы:

ticket_number = 123456  
Результат:  
Несчастливый билет

# Task 5

- A variable is given, which stores a six-digit number (the number of the ticket).
- Write a program that will determine whether a given ticket is "lucky". A ticket is considered lucky if the sum of the first three digits matches the sum of the last three digits of the number.

- Examples of how the program works:

ticket_number = 123456  
The result:
An unlucky ticket

***
# Задание 6 (необязательное)

- Напишите программу, которая сможет вычислять площади трех фигур (круг, треугольник и прямоугольник). Тип фигуры запрашиваем через пользовательский ввод, после чего делаем запрос характеристик фигуры:
<br>- если пользователь выбрал круг, запрашиваем его радиус,
<br>- если треугольник – длины трех его сторон;
<br>- если прямоугольник – длины двух его сторон.

- Пример работы программы:  
Введите тип фигуры:  
Круг  
Введите радиус круга:  
10  
Результат:  
Площадь круга: 314.16 

# Task 6 

- Write a program that can calculate the areas of three shapes (circle, triangle and rectangle). We request the shape type through user input, after which we make a request for the shape's characteristics.:
<br>- if the user has selected a circle, we request its radius,
<br>- if a triangle is the length of its three sides;
<br>- if the rectangle is the length of its two sides.

- An example of how the program works:  
Enter the shape type:  
Circle  
Enter the radius of the circle:
10  
Result:
Circle area: 314.16