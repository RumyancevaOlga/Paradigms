from Paradigms.Seminar_6.task3 import merge_sort


# для написания бинарного поиска использовалась структурная и функциональная парадигмы
# в функцию поиска необходимо передать отсортированный массив,, в котором будет производится поиск
# величину, которую мы ищем, минимальный и максимальные индексы массива
def binary_search(lst: list, value: int, min_: int, max_: int) -> int:
    # сначала прописываем условия выхода из рекурсии, если индексы встретились, а число так и не нашлось, возвращаем код ошибки -1
    if max_ < min_:
        return -1
    # иначе ищем среднюю точку
    else:
        midpoint = int((max_ - min_) / 2 + min_)
    # проверяем по условию больше или меньше искомое значение, значения середины и рекурсивно вызываем функцию откусывая от массива значения слева или справв в зависимости от результата
    if lst[midpoint] < value:
        return binary_search(lst, value, midpoint + 1, max_)
    else:
        if lst[midpoint] > value:
            return binary_search(lst, value, min_, midpoint - 1)
        # возвращаем значение, если оно совпало
        else:
            return midpoint


if __name__ == '__main__':
    lst = [20, 0, 11, 56, 14, 5, 18]
    # сортируем список при помощи метода сортировки слиянием из семинара
    merge_sort(lst)
    print(lst)
    print(binary_search(lst, 14, 0, len(lst) - 1))
