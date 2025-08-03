queries = [
    "смотреть сериалы онлайн",
    "новости спорта",
    "афиша кино",
    "курс доллара",
    "сериалы этим летом",
    "курс по питону",
    "сериалы про спорт",
]

# Создаем словарь для подсчета количества запросов по числу слов
word_counts = {}

# Подсчитываем количество слов в каждом запросе
for query in queries:
    num_words = len(query.split())
    if num_words in word_counts:
        word_counts[num_words] += 1
    else:
        word_counts[num_words] = 1

# Общее количество запросов
total_queries = len(queries)

# Выводим результат в требуемом формате
for num_words, count in word_counts.items():
    percentage = (count / total_queries) * 100
    print(f"Поисковых запросов, содержащих {num_words} слов(а): {percentage:.2f}%")

"""
# немного оптимизирования при помощи set comprehension и list comprehension:

for i in {len(i.split()) for i in queries}:
    print(f'Поисковых запросов, содержащих {i} слов(а): {len([s for s in queries if len(s.split()) == i ]) / len(queries) :.2%}')
    
"""