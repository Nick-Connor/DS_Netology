boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

# Проверяем, равны ли длины списков
if len(boys) != len(girls):
    print("Внимание, кто-то может остаться без пары!")
else:
    # Сортируем оба списка по алфавиту
    boys_sorted = sorted(boys)
    girls_sorted = sorted(girls)

    # Формируем пары
    print("Идеальные пары:")
    for boy, girl in zip(boys_sorted, girls_sorted):
        print(f"{boy} и {girl}")