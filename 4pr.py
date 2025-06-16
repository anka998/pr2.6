s = [-5, -1, 2, 3, -4, 6, -7]

first_positive = None
last_negative = None

for number in s:
    if number > 0 and first_positive is None:
        first_positive = number
    if number < 0:
        last_negative = number

if first_positive is not None:
    print(f"Первый положительный элемент: {first_positive}")
else:
    print("Положительных элементов нет.")

if last_negative is not None:
    print(f"Последний отрицательный элемент: {last_negative}")
else:
    print("Отрицательных элементов нет.")
