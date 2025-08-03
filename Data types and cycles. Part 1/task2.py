total_number = 0

while True:
    number = int(input("Введите число: "))
    if number == 0:
      break
    total_number += number

print("Результат:", total_number)

"""
# альтернативное решение, можно было обойтись вообще без условия внутри цикла, 
# если сделать цикл while с проверкой на неравенства числа нулю:

number = True
sum_ = 0
while number != 0:
   number = int(input('Введите число '))
   sum_ += number
print(sum_)

"""

"""
# также можно было использовать моржовый оператор для оптимизации:

a = 0
while number := int(input("введите число: ")):
    a += number
print(a)

"""

"""
# итераторы помогли бы решить вторую задачу в одну строку:

print(sum([int(x) for x in iter(input, '0')]))

"""