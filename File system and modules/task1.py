import json

# Чтение purchase_log.txt и создание словаря purchases
purchases = {}
with open("purchase_log.txt", "r", encoding="utf-8") as f:
    for line in f:
        data = json.loads(line.strip())
        purchases[data["user_id"]] = data["category"]

# Обрабатываем visit_log.csv и создаем funnel.csv
with open("visit_log.csv", "r", encoding="utf-8") as visits, open(
    "funnel.csv", "w", encoding="utf-8"
) as funnel:

    # Записываем заголовок в funnel.csv
    funnel.write("user_id,source,category\n")

    # Пропускаем заголовок visit_log.csv
    next(visits)

    for line in visits:
        parts = line.strip().split(",")
        if len(parts) >= 2:
            user_id = parts[0]
            source = parts[1]

            # Проверяем, есть ли user_id в нашем большом словаре
            if user_id in purchases:
                # Записываем совпадения в новый файл
                funnel.write(f"{user_id},{source},{purchases[user_id]}\n")

# Для проверки выведем количество записей в словаре
print(f"Всего записей в словаре purchases: {len(purchases)}")
print(f"Примеры записей: {list(purchases.items())[:5]}")
