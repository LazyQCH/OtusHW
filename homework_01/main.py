"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [num**2 for num in numbers]

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def filter_numbers(numbers, filter):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if filter == ODD:
        return [num for num in numbers if num % 2]
    elif filter == EVEN:
        return [num for num in numbers if not num % 2]
    elif filter == PRIME:
        row = []
        for i in numbers:
            test = True
            if i < 2:
                test = False
            else:
                for j in range(2, i):
                    if i % j == 0:
                        test = False
                if test:
                    row.append(i)
        return row
