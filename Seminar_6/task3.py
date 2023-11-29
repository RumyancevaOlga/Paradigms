def merge_sort(lst: list):
    if len(lst) > 1:
        half_len= len(lst) // 2
        left = lst[:half_len]
        right = lst[half_len:]
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1

            k += 1

        if i < len(left):
            lst[k:] = left[i:]
        else:
            lst[k:] = right[j:]


if __name__ == '__main__':
    lst = [20, 0, 11, 56, 14, 5]
    merge_sort(lst)
    print(lst)
    