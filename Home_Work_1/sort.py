# Задача №1
# Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
# сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.

def sort_list_imperative(numbers: list):
    # находим длину массива
    len_numbers = 0
    for _ in numbers:
        len_numbers += 1
    # используем алгоритм пузырьковой сортировки
    for i in range(len_numbers):
        for j in range(len_numbers - 1):
            if numbers[j] < numbers[j + 1]:
                temp = numbers[j]
                numbers[j] = numbers[j + 1]
                numbers[j + 1] = temp
    return numbers

# Задача №2
# Написать точно такую же процедуру, но в декларативном стиле


def sort_list_declarative(numbers: list):
    # используем встроенную функцию sorted
    return sorted(numbers, reverse=True)


if __name__ == '__main__':
    num = [5, 10, 2, 35, 48, 354, 56, 12]
    print(sort_list_imperative(num))
    num = [5, 10, 2, 35, 48, 354, 56, 12]
    print(sort_list_declarative(num))
