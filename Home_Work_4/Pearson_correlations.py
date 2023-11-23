# Написать скрипт для расчета корреляции Пирсона между
# двумя случайными величинами (двумя массивами). Можете
# использовать любую парадигму, но рекомендую использовать
# функциональную, т.к. в этом примере она значительно
# упростит вам жизнь.

# решим задачу используя функциональную, процедурную и структурную парадигмы

from functools import reduce


def correlations(x: list, y: list) -> float:
    # находим среднее значения в обоих списках
    x_mean = sum(x) / len(x)
    y_mean = sum(y) / len(y)
    # сщставляем списки разностей для каждого списка
    difference_x = list(map(lambda x: x - x_mean, x))
    difference_y = list(map(lambda y: y - y_mean, y))
    # находим числитель
    numerator = sum(list(map(lambda x, y: x * y, difference_x, difference_y)))
    # возводим разности в квадрат и находим их сумму
    sum_of_squares_of_differences_x = sum(list(map(lambda x: x ** 2, difference_x)))
    sum_of_squares_of_differences_y = sum(list(map(lambda y: y ** 2, difference_y)))
    # находим знаменатель
    denominator = reduce(lambda x, y: x * y, list(map(lambda x: x ** 0.5, [sum_of_squares_of_differences_x, sum_of_squares_of_differences_y])))
    # находим и возвращаем коэффициент
    return round(numerator / denominator, 3)


if __name__ == '__main__':
    list_x = [2, 4, 6, 8]
    list_y = [2, 4, 10, 12]
    # ожидаем 0,976
    print(correlations(list_x, list_y))
    list_x = [60, 65, 72, 70, 74, 63, 66, 68, 67, 69, 70, 64]
    list_y = [120, 140, 180, 184, 190, 160, 155, 158, 170, 190, 210, 150]
    # ожидаем 0,836
    print(correlations(list_x, list_y))

