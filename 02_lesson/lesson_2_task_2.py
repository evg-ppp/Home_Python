# Объявляем функцию is_year_leap

def is_year_leap(year):
    # Проверяем условие на високосный год
    if year % 4 == 0:
        return True
    else:
        return False


# Вызываем функцию и сохраняем результат
result = is_year_leap(2024)

# Выводим результат в консоль
print(f'Год 2024: {result}')
