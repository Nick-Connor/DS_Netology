import re

def validate_car_numbers(car_ids):
    pattern = re.compile(
        r'^'
        r'[АВЕКМНОРСТУХ]\d{3}'  # 1 буква (из допустимых) + 3 цифры
        r'[АВЕКМНОРСТУХ]{2}'    # 2 буквы (из допустимых)
        r'\d{2,3}'               # 2 или 3 цифры (регион)
        r'$'
    )

    for car_id in car_ids:
        if re.fullmatch(pattern, car_id):
            # Разделяем номер и регион
            letters_part = car_id[:6]  # Первые 6 символов (буква + 3 цифры + 2 буквы)
            region = car_id[6:]       # Остальное — регион
            print(f"Номер {letters_part} валиден. Регион: {region}")
        else:
            print(f"Номер {car_id} не валиден")

# Пример использования
car_ids = ['А222ВС96', 'АБ22ВВ193']
validate_car_numbers(car_ids)