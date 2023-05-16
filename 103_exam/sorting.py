def bubble_sort(list_of_numbers):
    print(f"Unsorted list: {list_of_numbers}")
    for i in range((len(list_of_numbers))):
        for i in range(len(list_of_numbers) - 1):
            if list_of_numbers[i] > list_of_numbers[i + 1]:
                list_of_numbers.insert(i, list_of_numbers.pop(i + 1))
            else:
                continue
    print(f"Sorted list: {list_of_numbers}")


el_to_sort = [
    [],
    [1, 2, 5, 3, 1, 7, 9, 1, 12, 83, 1, 5, 3, 2],
    [1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1],
    [2, 2, 2, 2],
    [1, 2],
    [2, 1],
]
for el in el_to_sort:
    bubble_sort(el)
    print()
