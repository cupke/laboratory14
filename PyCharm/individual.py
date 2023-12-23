def calculate_extremum(type='max'):
    def inner_function(lst):
        if type == 'max':
            return max(lst)
        else:
            return min(lst)

    return inner_function

# Получаем от пользователя список чисел
user_input = input("Введите числа через пробел: ")
numbers = [int(x) for x in user_input.split()]

# Задаем тип по умолчанию как 'max' и вызываем внутреннюю функцию замыкания
result_function = calculate_extremum()
result = result_function(numbers)

print(f"Результат: {result}")
