import random


class Row:
    # randseq1 = []

    def __init__(self, name):
        self.name = name

    def numb(self):
        import random

        randseq1 = random.sample(range(1, 10), 9)
        print(randseq1)


row1 = Row("one")


class Row2(Row):
    def __init__(self, name):
        super().__init__(name)

    def numbnext(self):
        randseq2 = []

        for i in range(9):
            while True:
                x = random.sample(range(1, 10), 1)
                if x != row1.numb()[i - 1]:
                    randseq2.append(x)
                    return False
                else:
                    True
        print(randseq2)


row2 = Row2("two")
row1.numb()
row2.numb()


# one = random.sample(range(1, 10), 9)
# two = []
# for i in range(9):
#     while True:
#         x = random.sample(range(1, 10), 1)
#         if x != one[i - 1]:
#             two.append(x)
#             False
#         else:
#             True
# two


# def numbnext():
#     one = random.sample(range(1, 10), 9)
#     two = random.sample(range(1, 10), 9)
#     print(two)
#     for i in range(9):
#         if two[i - 1] == one[i - 1]:
#             two[i - 1] = random.sample(range(1, 10), 1)

#     print(f"{one}\n{two}")


# numbnext()

# pool = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in range(3):
#     m1 = random.sample(pool, 3)
#     for i in range(3):
#         pool.remove(m1[i - 1])
#     print(m1)
# print(m1[0][1])

# r1 = [0, 0, 0]
# r2 = [0, 0, 0]
# r3 = [0, 0, 0]
# master = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# pool = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# m1 = []
# for i in range(3):
#     for i in range(3):
#         master[i - 1][i - 1] = random.sample(pool, 1)
#         for i in range(3):
#             pool.remove(master[i - 1][i - 1])
# print(master)
# print(master[0])
# --------------------------------
# center = []
# masterpool = 1, 2, 3, 4, 5, 6, 7, 8, 9
# pool = list(masterpool)
# for i in range(3):
#     x = random.sample(pool, 3)
#     for i in range(3):
#         pool.remove(x[i - 1])
#     center.append(x)

# mac0_1 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# mac2_1 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# pool = list(masterpool)

# for i in range(3):
#     pool.remove(center[i - 1][0])
# y = random.sample(pool, 3)
# for i in range(3):
#     pool.remove(y[i - 1])
# for i in range(3):
#     mac0_1[i - 1][0] = y[i - 1]
# y2 = random.sample(pool, 3)
# for i in range(3):
#     mac2_1[i - 1][0] = y2[i - 1]
# print(f"{mac0_1[0]}\n{mac0_1[1]}\n{mac0_1[2]}")
# print(f"{center[0]}\n{center[1]}\n{center[2]}")
# print(f"{mac2_1[0]}\n{mac2_1[1]}\n{mac2_1[2]}")

# # można też sprawdzić opcję "if not in" i tworzyć listy pionowe
# pool = list(masterpool)

# temp_pool = []
# for i in range(3):
#     temp_pool.append(mac0_1[i - 1][0])
#     temp_pool.append(center[i - 1][1])
# temp_pool = list(set(temp_pool))

# for i in range(len(temp_pool)):
#     pool.remove(temp_pool[i - 1])

# print(pool)
