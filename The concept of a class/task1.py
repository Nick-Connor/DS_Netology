import requests
import json


def get_max_rate_currency():
    """Возвращает название валюты с максимальным значением курса"""
    url = "https://www.cbr-xml-daily.ru/daily_json.js"
    response = requests.get(url)
    data = response.json()

    max_rate = 0
    max_currency = ""

    for currency in data["Valute"].values():
        if currency["Value"] > max_rate:
            max_rate = currency["Value"]
            max_currency = currency["Name"]

    return max_currency


# Пример использования
print(get_max_rate_currency())
