from datetime import datetime


def is_valid_date(date_str):
    try:
        # Пытаемся преобразовать строку в дату
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        # Если возникает ошибка - дата некорректна
        return False


# Пример использования
stream = ["2018-04-02", "2018-02-29", "2018-19-02"]
results = []

for date in stream:
    is_valid = is_valid_date(date)
    results.append(is_valid)
    print(f"{date}: {is_valid}")
