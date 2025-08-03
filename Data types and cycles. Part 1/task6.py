import re

def calculate_average_views(stream):
    total_views = 0
    unique_users = set()

    pattern = re.compile(r'^(.+?),.+?;(\d+)$')  # Имя пользователя и просмотры

    for log in stream:
        match = pattern.match(log)
        if match:
            user, views = match.groups()
            unique_users.add(user)
            total_views += int(views)

    if not unique_users:
        return 0.0  # На случай пустого списка

    average = total_views / len(unique_users)
    return round(average, 2)  # Округляем до 2 знаков после запятой

# Примеры использования
stream1 = [
    'user4,2021-01-01;3',
    'user3,2022-01-07;4',
    'user2,2022-03-29;1',
    'user1,2020-04-04;13',
    'user2,2022-01-05;7',
    'user1,2021-06-14;4',
    'user3,2022-07-02;10',
    'user4,2021-03-21;19',
    'user4,2022-03-22;4',
    'user4,2022-04-22;8',
    'user4,2021-05-03;9',
    'user4,2022-05-11;11'
]

stream2 = [
    'user100,2022-01-01;150',
    'user99,2022-01-07;205',
    'user1001,2022-03-29;81'
]

avg1 = calculate_average_views(stream1)
avg2 = calculate_average_views(stream2)

print(f"Среднее количество просмотров на уникального пользователя: {avg1}")
print(f"Среднее количество просмотров на уникального пользователя: {avg2}")