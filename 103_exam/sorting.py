def bubble_sort(list_of_numbers):
    for i in range((len(list_of_numbers))):
        for i in range(len(list_of_numbers) - 1):
            if list_of_numbers[i] > list_of_numbers[i + 1]:
                # print(lista[i])
                list_of_numbers.insert(i, list_of_numbers.pop(i + 1))
                # print(lista)
            else:
                continue
    print(list_of_numbers)
