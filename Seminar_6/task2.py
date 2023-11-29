def min_square_error(lst1, lst2):
    return sum(map(lambda x: (x[0] - x[1]) ** 2, zip(lst1, lst2))) / len(lst1)


if __name__ == '__main__':
    lst1 = [1, 2, 3, 4]
    lst2 = [5, 6, 7, 8]
    print(min_square_error(lst1, lst2))
