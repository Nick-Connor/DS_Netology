class Rate:
    def __init__(self, diff=False):
        self.diff = diff

    def get_currency_rate(self, currency_code):
        """Получает курс валюты по коду"""
        url = "https://www.cbr-xml-daily.ru/daily_json.js"
        response = requests.get(url)
        data = response.json()

        currency = data["Valute"][currency_code]

        if self.diff:
            # Возвращаем разницу с предыдущим значением
            return currency["Value"] - currency["Previous"]
        else:
            # Возвращаем текущий курс
            return currency["Value"]

    def eur(self):
        """Курс евро"""
        return self.get_currency_rate("EUR")

    def usd(self):
        """Курс доллара"""
        return self.get_currency_rate("USD")

    def get_all_currencies(self):
        """Вся информация о валютах (diff не используется)"""
        url = "https://www.cbr-xml-daily.ru/daily_json.js"
        response = requests.get(url)
        return response.json()["Valute"]


# Примеры использования
rate = Rate()
print(f"USD: {rate.usd()}")  # Текущий курс

rate_diff = Rate(diff=True)
print(f"USD изменение: {rate_diff.usd()}")  # Изменение курса

# Вся информация (diff игнорируется)
all_currencies = rate.get_all_currencies()
