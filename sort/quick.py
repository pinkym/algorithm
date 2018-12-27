toSort = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]


def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    else:
        pivot_index = 0
        sorted_idnex = pivot_index + 1

        for i, num in enumerate(numbers[pivot_index + 1:]):
            if num < numbers[pivot_index]:
                tmp = num
                numbers[pivot_index + 1 + i] = numbers[pivot_index + sorted_idnex]
                numbers[sorted_idnex] = tmp

                sorted_idnex += 1

        tmp2 = numbers[pivot_index]
        numbers[pivot_index] = numbers[sorted_idnex - 1]
        numbers[sorted_idnex - 1] = tmp2

        return quick_sort(numbers[:sorted_idnex - 1]) + [tmp2] + quick_sort(numbers[sorted_idnex:])


print(quick_sort(toSort))
