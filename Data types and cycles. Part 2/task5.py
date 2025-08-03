# Создает словарь с вложенностью, равной длине списка
def create_nested_dict(items):
        if len(items) == 1:
          return items[0] # возврат из рекурсии
        return {items[0]: create_nested_dict(items[1:])}

# Примеры из задачи
my_list1 = ['2018-01-01', 'yandex', 'cpc', 100]
result1 = create_nested_dict(my_list1)
print(result1)  # {'2018-01-01': {'yandex': {'cpc': 100}}}

my_list2 = ['a', 'b', 'c', 'd', 'e', 'f']
result2 = create_nested_dict(my_list2)
print(result2)  # {'a': {'b': {'c': {'d': {'e': 'f'}}}}}