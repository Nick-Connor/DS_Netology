cook_book = {
    'салат': [
        {'ingridient_name': 'сыр', 'quantity': 50, 'measure': 'гр'},
        {'ingridient_name': 'томаты', 'quantity': 2, 'measure': 'шт'},
        {'ingridient_name': 'огурцы', 'quantity': 20, 'measure': 'гр'},
        {'ingridient_name': 'маслины', 'quantity': 10, 'measure': 'гр'},
        {'ingridient_name': 'оливковое масло', 'quantity': 20, 'measure': 'мл'},
        {'ingridient_name': 'салат', 'quantity': 10, 'measure': 'гр'},
        {'ingridient_name': 'перец', 'quantity': 20, 'measure': 'гр'}
    ],
    'пицца': [
        {'ingridient_name': 'сыр', 'quantity': 20, 'measure': 'гр'},
        {'ingridient_name': 'колбаса', 'quantity': 30, 'measure': 'гр'},
        {'ingridient_name': 'бекон', 'quantity': 30, 'measure': 'гр'},
        {'ingridient_name': 'оливки', 'quantity': 10, 'measure': 'гр'},
        {'ingridient_name': 'томаты', 'quantity': 20, 'measure': 'гр'},
        {'ingridient_name': 'тесто', 'quantity': 100, 'measure': 'гр'},
    ],
    'лимонад': [
        {'ingridient_name': 'лимон', 'quantity': 1, 'measure': 'шт'},
        {'ingridient_name': 'вода', 'quantity': 200, 'measure': 'мл'},
        {'ingridient_name': 'сахар', 'quantity': 10, 'measure': 'гр'},
        {'ingridient_name': 'лайм', 'quantity': 20, 'measure': 'гр'},
    ]
}

def calculate_ingredients(cook_book, portions):
    # Создаем словарь для агрегации ингредиентов
    ingredients_sum = {}

    # Перебираем все блюда в книге рецептов
    for dish in cook_book.values():
        # Для каждого ингредиента в блюде
        for ingredient in dish:
            # Создаем уникальный ключ из названия и единицы измерения
            key = (ingredient['ingridient_name'], ingredient['measure'])
            # Умножаем количество на число порций
            quantity = ingredient['quantity'] * portions

            # Если ингредиент уже встречался, суммируем количество
            if key in ingredients_sum:
                ingredients_sum[key] += quantity
            else:
                ingredients_sum[key] = quantity

    return ingredients_sum

# Запрашиваем количество порций у пользователя
portions = int(input("Введите количество порций: "))

# Получаем суммарные количества ингредиентов
result = calculate_ingredients(cook_book, portions)

# Выводим результат в требуемом формате
print("\nРезультат:\n")
for (name, measure), quantity in result.items():
    print(f"{name.capitalize()}: {quantity} {measure}")