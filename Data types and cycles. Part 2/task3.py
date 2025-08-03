# Для решения этой задачи нужно дополнить каждый элемент словаря results новым ключом ROI, рассчитанным по формуле:
# ROI = ((revenue / cost) - 1) * 100

results = {
    'vk': {'revenue': 103, 'cost': 98},
    'yandex': {'revenue': 179, 'cost': 153},
    'facebook': {'revenue': 103, 'cost': 110},
    'adwords': {'revenue': 35, 'cost': 34},
    'twitter': {'revenue': 11, 'cost': 24},
}

for source in results:
    revenue = results[source]['revenue']
    cost = results[source]['cost']
    roi = ((revenue / cost) - 1) * 100
    results[source]['ROI'] = round(roi, 2)  # Округляем до 2 знаков после запятой

print(results)

"""
# совсем не обязательно обновлять каждый ключ, можно только добавлять новый:

for info in results.values():
   info['ROI'] = round((info['revenue'] / info['cost'] - 1) * 100, 2)

print(results)

"""