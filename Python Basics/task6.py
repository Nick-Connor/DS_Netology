import math

def calculate_area():
    print('Доступные фигуры: Круг, Треугольник, Прямоугольник')
    figure_type = input('Введите тип фигуры: ')

    if figure_type == 'Круг':
        radius = float(input('Введите радиус круга: '))
        area = math.pi * radius ** 2
        print('Площадь Круга:', area)
    elif figure_type == 'Треугольник':
        a = float(input('Введите длину первой стороны: '))
        b = float(input('Введите длину второй стороны: '))
        c = float(input('Введите длину третьей стороны: '))
# Проверка на возможность существования треугольника
        if a + b > c and a + c > b and b + c > a:
            # Формула Герона
            p = (a + b + c) / 2
            area = math.sqrt(p * (p - a) * (p - b) * (p - c))
            print('Площадь Треугольника:', area)
        else:
            print('Треугольник с такими сторонами не существует')
    elif figure_type == 'Прямоугольник':
        length = float(input('Введите длину Прямоугольника: '))
        width = float(input('Введите ширину Прямоугольника: '))
        area = length * width
        print('Площадь Прямоугольника:', area)
    else:
        print('Неизвестный тип фигуры')

calculate_area()