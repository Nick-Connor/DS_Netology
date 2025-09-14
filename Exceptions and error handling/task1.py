from datetime import datetime

# Форматы дат для каждой газеты
date_formats = {
    "The Moscow Times": "%A, %B %d, %Y",  # Wednesday, October 2, 2002
    "The Guardian": "%A, %d.%m.%y",  # Friday, 11.10.13
    "Daily News": "%A, %d %B %Y",  # Thursday, 18 August 1977
}

# Пример использования
dates = {
    "The Moscow Times": "Wednesday, October 2, 2002",
    "The Guardian": "Friday, 11.10.13",
    "Daily News": "Thursday, 18 August 1977",
}

for newspaper, date_str in dates.items():
    fmt = date_formats[newspaper]
    date_obj = datetime.strptime(date_str, fmt)
    print(f"{newspaper}: {date_obj}")
