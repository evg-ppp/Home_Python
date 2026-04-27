# подключить модуль math
# использовать math.ceil
import math
# Напишите функцию square, принимающую один аргумент— сторону квадрата


def square(side):
    return math.ceil(side * side)


# проверки можно добавить запрос стороны
side = float(input("Введите длину стороны квадрата: "))
area = square(side)
print(f"Площадь квадрата: {area}")
