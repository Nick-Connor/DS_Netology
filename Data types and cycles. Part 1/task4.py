# формула преобразования - Цельсий = (Фаренгейт - 32) × 5/9
countries_temperature = [
    ['Таиланд', [75.2, 77, 78.8, 73.4, 68, 75.2, 77]],
    ['Германия', [57.2, 55.4, 59, 59, 53.6]],
    ['Россия', [35.6, 37.4, 39.2, 41, 42.8, 39.2, 35.6]],
    ['Польша', [50, 50, 53.6, 57.2, 55.4, 55.4]]
]

print("Средняя температура в странах:")

for country_data in countries_temperature:
    country = country_data[0]
    fahrenheit_temps = country_data[1]

    # Конвертируем все температуры в Цельсии и вычисляем среднее
    celsius_temps = [(f - 32) * 5/9 for f in fahrenheit_temps]
    avg_celsius = sum(celsius_temps) / len(celsius_temps)

    # Округляем до одного знака после запятой
    print(f"{country} - {avg_celsius:.1f} C")

# :.2f — спецификатор формата, который означает:

# 2 — округлить число до 2 знаков после запятой.

# f — выводить как число с плавающей точкой (float).

"""
# совсем не обязательно создавать новый список, можно сразу делать вывод:

print("Средняя температура в странах:")
for element in countries_temperature:
   avg_temp = sum(element[1]) / len(element[1])
   print(f"{element[0]} - {(avg_temp - 32)*5/9 :.1f} C")

"""