# Задание 1
Дана переменная, в которой хранится словарь, содержащий гео-метки для каждого пользователя (пример структуры данных приведен ниже). Вам необходимо написать программу, которая выведет на экран множество уникальных гео-меток всех пользователей.

Пример работы программы:

ids = {‘user1’: [213, 213, 213, 15, 213],   
‘user2’: [54, 54, 119, 119, 119],  
‘user3’: [213, 98, 98, 35]}  
Результат: {98, 35, 15, 213, 54, 119}

# Task 1
A variable is given that stores a dictionary containing geo tags for each user (an example of the data structure is given below). You need to write a program that displays a variety of unique geo-tags for all users.

An example of how the program works:

ids = {‘user1’: [213, 213, 213, 15, 213],   
‘user2’: [54, 54, 119, 119, 119],  
‘user3’: [213, 98, 98, 35]}  
The result: {98, 35, 15, 213, 54, 119}

***

# Задание 2
Дана переменная, в которой хранится список поисковых запросов пользователя (пример структуры данных приведен ниже, но запросы потенциально могут быть любые). Вам необходимо написать программу, которая выведет на экран распределение количества слов в запросах в требуемом виде.

Пример работы программы:  

queries = [  
‘смотреть сериалы онлайн’,  
‘новости спорта’,  
‘афиша кино’,  
‘курс доллара’,  
‘сериалы этим летом’,  
‘курс по питону’,  
‘сериалы про спорт’,  
]  

Результат:  

Поисковых запросов, содержащих 2 слов(а): 42.86%  
Поисковых запросов, содержащих 3 слов(а): 57.14%  

# Task 2
A variable is given that stores a list of the user's search queries (an example of the data structure is given below, but the queries can potentially be any). You need to write a program that displays the distribution of the number of words in the queries in the required form.

An example of how the program works:  

queries = [  
‘watch TV series online’,  
‘sports news’,  
‘movie poster’,  
‘dollar exchange rate’,  
‘TV series this summer’,  
‘python course’,  
‘series about sports',
]  

Result:  

Search queries containing 2 words(a): 42.86%  
Search queries containing 3 words(a): 57.14%

***

# Задание 3
Дана переменная, в которой хранится информация о затратах и доходе рекламных кампаний по различным источникам. Необходимо дополнить исходную структуру показателем ROI, который рассчитаем по формуле: ((revenue / cost) - 1) * 100

Пример работы программы:  

results = {  
‘vk’: {‘revenue’: 103, ‘cost’: 98},  
‘yandex’: {‘revenue’: 179, ‘cost’: 153},  
‘facebook’: {‘revenue’: 103, ‘cost’: 110},  
‘adwords’: {‘revenue’: 35, ‘cost’: 34},  
‘twitter’: {‘revenue’: 11, ‘cost’: 24},  
}  

Результат:  

{‘adwords’: {‘revenue’: 35, ‘cost’: 34, ‘ROI’: 2.94},  
‘facebook’: {‘revenue’: 103, ‘cost’: 110, ‘ROI’: -6.36},  
‘twitter’: {‘revenue’: 11, ‘cost’: 24, ‘ROI’: -54.17},  
‘vk’: {‘revenue’: 103, ‘cost’: 98, ‘ROI’: 5.1},  
‘yandex’: {‘revenue’: 179, ‘cost’: 153, ‘ROI’: 16.99}}  

# Задание 3
Дана переменная, в которой хранится информация о затратах и доходе рекламных кампаний по различным источникам. Невозможно повысить рентабельность инвестиций, которая рассчитывается следующим образом: ((выручка / затраты) - 1) * 100

Пример работы программы:  

результаты = {  
‘вконтакте’: {‘доход": 103, "стоимость": 98},
"яндекс": {"доход": 179, "стоимость": 153},
"facebook": {"доход": 103, ‘стоимость’: 110},
‘adwords’: {‘доход’: 35, "стоимость": 34},
‘твиттер’: {‘доход’: 11, ‘стоимость’: 24},  
}  

Результат:  

{‘adwords’: _BOS_"доход": 35, "стоимость": 34, "Рентабельность инвестиций’: 2,94},  
‘facebook’: {‘доход": 103, "стоимость": 110, "рентабельность инвестиций": -6,36},
"twitter": {"доход": 11, "стоимость": 24, "рентабельность инвестиций": -54,17},
"вконтакте": {"доход": 103, "стоимость": 98, "рентабельность инвестиций": 5,1},
"яндекс": {"доход": 179, "стоимость": 153, "рентабельность инвестиций": 16,99}}

***

# Задание 4
Дана переменная, в которой хранится статистика рекламных каналов по объемам продаж (пример структуры данных приведен ниже). Напишите программу, которая возвращает название канала с максимальным объемом продаж.  

Пример работы программы:  

stats = {‘facebook’: 55, ‘yandex’: 115, ‘vk’: 120, ‘google’: 99, ‘email’: 42, ‘ok’: 98}  

Результат: Максимальный объем продаж на рекламном канале: vk  

# Task 4
A variable is given in which the statistics of advertising channels by sales volumes are stored (an example of the data structure is given below). Write a program that returns the name of the channel with the maximum sales volume.  

An example of how the program works:  

stats = {‘facebook’: 55, ‘yandex’: 115, ‘vk’: 120, ‘google’: 99, ‘email’: 42, ‘ok’: 98}  

Result: Maximum sales volume on the advertising channel: vk

***

# Задание 5
Дан список произвольной длины. Необходимо написать код, который на основе исходного списка составит словарь такого уровня вложенности, какова длина исхондого списка.

Примеры работы программы:  

my_list = [‘2018-01-01’, ‘yandex’, ‘cpc’, 100]   
Результат: {‘2018-01-01’: {‘yandex’: {‘cpc’: 100}}}  

my_list = [‘a’, ‘b’, ‘c’, ‘d’, ‘e’, ‘f’]  
Результат: {‘a’: {‘b’: {‘c’: {‘d’: {‘e’: ‘f’}}}}}  

# Task 5
A list of available lengths is given. You need to write code that, based on the source list, will make up a dictionary of such an attachment level as the length of the source list.

Examples of how the program works:  

my_list = [‘2018-01-01’, ‘yandex’, ‘cpc’, 100]   
Result: {‘2018-01-01': {'yandex': {'cpc': 100}}}  

my_list = [‘a’, ‘b’, ‘c’, ‘d’, ‘e’, ‘f’]  
Result: {'a‘: {'b': {'c': {'d': {'e':’f'}}}}}

***

# Задание 6 (необязательно)
Дана книга рецептов с информацией о том, сколько ингредиентов нужно для приготовления блюда в расчете на одну порцию (пример данных представлен ниже).
Напишите программу, которая будет запрашивать у пользователя количество порций для приготовления этих блюд и отображать информацию о суммарном количестве требуемых ингредиентов в указанном виде.  
Внимание! Одинаковые ингредиенты с разными размерностями нужно считать раздельно!  

Пример работы программы:  
   
cook_book = {  
‘салат’: [  
{‘ingridient_name’: ‘сыр’, ‘quantity’: 50, ‘measure’: ‘гр’},  
{‘ingridient_name’: ‘томаты’, ‘quantity’: 2, ‘measure’: ‘шт’},  
{‘ingridient_name’: ‘огурцы’, ‘quantity’: 20, ‘measure’: ‘гр’},  
{‘ingridient_name’: ‘маслины’, ‘quantity’: 10, ‘measure’: ‘гр’},  
{‘ingridient_name’: ‘оливковое масло’, ‘quantity’: 20, ‘measure’: ‘мл’},  
{‘ingridient_name’: ‘салат’, ‘quantity’: 10, ‘measure’: ‘гр’},  
{‘ingridient_name’: ‘перец’, ‘quantity’: 20, ‘measure’: ‘гр’}  
],  
‘пицца’: [  
{‘ingridient_name’: ‘сыр’, ‘quantity’: 20, ‘measure’: ‘гр’},  
{‘ingridient_name’: ‘колбаса’, ‘quantity’: 30, ‘measure’: ‘гр’},  
{‘ingridient_name’: ‘бекон’, ‘quantity’: 30, ‘measure’: ‘гр’},  
{‘ingridient_name’: ‘оливки’, ‘quantity’: 10, ‘measure’: ‘гр’},  
{‘ingridient_name’: ‘томаты’, ‘quantity’: 20, ‘measure’: ‘гр’},  
{‘ingridient_name’: ‘тесто’, ‘quantity’: 100, ‘measure’: ‘гр’},  
],  
‘лимонад’: [  
{‘ingridient_name’: ‘лимон’, ‘quantity’: 1, ‘measure’: ‘шт’},  
{‘ingridient_name’: ‘вода’, ‘quantity’: 200, ‘measure’: ‘мл’},  
{‘ingridient_name’: ‘сахар’, ‘quantity’: 10, ‘measure’: ‘гр’},  
{‘ingridient_name’: ‘лайм’, ‘quantity’: 20, ‘measure’: ‘гр’},  
]  
}  

Введите количество порций:  
3  
Результат:  

Сыр: 210 гр   
Томаты: 6 шт  
Огурцы: 60 гр  
Маслины: 30 гр  
Оливковое масло: 60 мл  
Салат: 30 гр  
Перец: 60 гр  
Колбаса: 90 гр  
Бекон: 90 гр  
Оливки: 30 гр  
Томаты: 60 гр  
Тесто: 300 гр  
Лимон: 3 шт  
Вода: 600 мл  
Сахар: 30 гр  
Лайм: 60 гр  

# Task 6 (optional)
A recipe book is provided with information on how many ingredients are needed to prepare a dish per serving (an example of the data is presented below).
Write a program that will ask the user for the number of servings to prepare these dishes and display information about the total number of required ingredients in the specified form.  
Attention! The same ingredients with different dimensions must be counted separately!  

Example of the program:

cook_book = {  
‘salad': [  
{‘ingridient_name': ‘cheese', ‘quantity': 50, ‘measure’: ‘gr’},  
{‘ingridient_name': ‘tomatoes', ‘quantity': 2, ‘measure’: ‘pcs’},  
{‘ingridient_name': ‘cucumbers', ‘quantity’: 20, ‘measure’: ‘gr’},  
{‘ingridient_name': ‘olives', ‘quantity’: 10, ‘measure’: ‘gr’},  
{‘ingridient_name': ‘olive oil', ‘quantity’: 20, ‘measure’: ‘ml’},  
{‘ingridient_name': ‘salad', ‘quantity’: 10, ‘measure’: ‘gr’},  
{‘ingridient_name': ‘pepper', ‘quantity’: 20, ‘measure’: ‘gr’}
],  
‘pizza': [  
{‘ingridient_name': ‘cheese', ‘quantity’: 20, ‘measure’: ‘gr’},  
{‘ingridient_name': ‘sausage', ‘quantity’: 30, ‘measure’: ‘gr’},  
{‘ingridient_name': ‘bacon', ‘quantity’: 30, ‘measure’: ‘gr’},  
{‘ingridient_name': ‘olives', ‘quantity’: 10, ‘measure’: ‘gr’},  
{‘ingridient_name': ‘tomatoes', ‘quantity’: 20, ‘measure’: ‘gr’},  
{‘ingridient_name': ‘dough', ‘quantity': 100, ‘measure’: ‘gr’},
],  
‘lemonade': [  
{‘ingridient_name': ‘lemon', ‘quantity’: 1, ‘measure’: ‘pcs’},  
{‘ingridient_name': ‘water', ‘quantity': 200, ‘measure’: ‘ml’},  
{‘ingridient_name': ‘sugar', ‘quantity': 10, ‘measure’: ‘gy’},  
{‘ingridient_name': ‘lime', ‘quantity’: 20, ‘measure’: ‘gr’},
]
}  

Enter the number of servings:
3  
Result:  

Cheese: 210 g   
Tomatoes: 6 pieces  
Cucumbers: 60 g  
Olives: 30 g  
Olive oil: 60 ml  
Salad: 30 g  
Pepper: 60 g  
Sausage: 90 g  
Bacon: 90 g  
Olives: 30 g  
Tomatoes: 60 g  
Dough: 300 g  
Lemon: 3 pieces  
Water: 600 ml  
Sugar: 30 grams  
Lime: 60 g