# lista = [3, 2, 5, 1, 9, 4]
# print(lista)

# for i in range(3):
#     for i in range(len(lista) - 1):
#         if lista[i] > lista[i + 1]:
#             print(lista[i])
#             lista.insert(i, lista.pop(i + 1))
#             print(lista)
#         else:
#             continue
# print(lista)

list_of_numbers = [
    5,
    4,
    3,
    2,
    1,
    0,
    0,
    2,
    1,
    1,
    0,
    1,
    7,
    6,
    3,
    0,
    2,
    0,
    2,
    0,
    1,
    0,
    0,
    1,
    0,
    2,
    4,
    3,
    2,
    1,
    0,
    0,
    2,
    1,
    1,
    0,
    1,
    7,
    6,
    3,
    0,
    2,
    0,
    2,
    0,
    1,
    0,
    0,
    1,
]


# print(lista)
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


bubble_sort(
    [
        1,
        2,
        3,
        0,
        0,
        0,
        -1,
        0,
        0,
        2,
        1,
        2,
        1,
        7,
        0,
        1,
    ]
)
