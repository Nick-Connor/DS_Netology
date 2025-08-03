word = input("Введите слово: ")

length = len(word)
middle_index = length // 2

if length % 2 == 1:
    # Нечетная длина - одна средняя буква
    result = word[middle_index]
else:
    # Четная длина - две средних буквы
    result = word[middle_index - 1:middle_index + 1]

print("Результат:", result)

"""
# альтернативное решение


print(word[(len(word)-1)//2:(len(word)+2)//2])

"""