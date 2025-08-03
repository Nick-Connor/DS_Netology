ids = {
    'user1': [213, 213, 213, 15, 213],
    'user2': [54, 54, 119, 119, 119],
    'user3': [213, 98, 98, 35]
}

# Создаем множество для хранения уникальных гео-меток
unique_geo_tags = set()

# Перебираем всех пользователей и их гео-метки
for user_geo_tags in ids.values():
    unique_geo_tags.update(user_geo_tags)

print(unique_geo_tags)

"""
# вариант использования функции sum с доп. параметром для суммирования списков:

print(set(sum(ids.values(), [])))

"""