# Входные данные
day = int(input('Введите день: '))
month = input('Введите месяц: ')

# Определяем знак зодиака
if (month == 'Декабрь' and day >= 22) or (month == 'Январь' and day <= 19):
    sign = 'Козерог'
elif (month == 'Январь' and day >= 20) or (month == 'Февраль' and day <= 18):
    sign = 'Водолей'
elif (month == 'Февраль' and day >= 19) or (month == 'Март' and day <= 20):
    sign = 'Рыбы'
elif (month == 'март' and day >= 21) or (month == 'Апрель' and day <= 19):
    sign = 'Овен'
elif (month == 'Апрель' and day >= 20) or (month == 'Май' and day <= 20):
    sign = 'Телец'
elif (month == 'Май' and day >= 21) or (month == 'Июнь' and day <= 20):
    sign = 'Близнецы'
elif (month == 'Июнь' and day >= 21) or (month == 'Июль' and day <= 22):
    sign = 'Рак'
elif (month == 'Июль' and day >= 23) or (month == 'Август' and day <= 22):
    sign = 'Лев'
elif (month == 'Август' and day >= 23) or (month == 'Сентябрь' and day <= 22):
    sign = 'Дева'
elif (month == 'Сентябрь' and day >= 23) or (month == 'Октябрь' and day <= 22):
    sign = 'Весы'
elif (month == 'Октябрь' and day >= 23) or (month == 'Ноябрь' and day <= 21):
    sign = 'Скорпион'
elif (month == 'Ноябрь' and day >= 22) or (month == 'Декабрь' and day <= 21):
    sign = 'Стрелец'
else:
    sign = 'Неизвестно (проверьте введенные данные)'

print('Ваш знак зодиака:', sign)
# Определяем знак зодиака
sign = None
for (m, d), zodiac in zodiac_signs.items():
    if month == m and day >= d:
        sign = zodiac

# Если знак не найден (например, введены некорректные данные)
if sign is None:
    sign = 'Неизвестно (проверьте введенные данные)'

print('Ваш знак зодиака:', sign)