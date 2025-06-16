C = input("Введите символ C: ")
A = input("Введите строковую последовательность A: ")

elements = A.split()

count = 0
for element in elements:
    if len(element) > 1 and element.startswith(C) and element.endswith(C):
        count += 1

print(f"Количество элементов, которые содержат более одного символа и начинаются и заканчиваются символом '{C}': {count}")
