import random

sorted = [1, 2, 3, 4, 5, 6, 7, 8, 9]
mac = [[], [], [], [], [], [], [], [], []]
rows = [[], [], [], [], [], [], [], [], []]

for i in range(9):
    mac[i] = random.sample(range(1, 10), 9)


def build_rows(a, b):
    for i in range(a, b):
        rows[a].append(mac[i][0:3])
        rows[a + 1].append(mac[i][3:6])
        rows[a + 2].append(mac[i][6:10])
    print(f"{rows[a]}\n{rows[a+1]}\n{rows[a+2]}")
    print("----------------------------------")


def check_rows():
    for row in rows:
        temp_row = [ele for sublist in row for ele in sublist]
        temp_row.sort()

        if sum(temp_row) == 45 and temp_row == sorted:
            print(f"***Wiersz {rows.index(row)+1}.  SPEŁNIA WARUNKI SUDOKU.****")

        else:
            print(f"Wiersz {rows.index(row)+1}. nie spełnia warunków sudoku.")


def check_columns():
    for i in range(9):
        temp_column = []
        for row in rows:
            newrow = [ele for sublist in row for ele in sublist]
            temp_column.append(newrow[i])
        temp_column.sort()
        if sum(temp_column) == 45 and temp_column == sorted:
            print(f"***Kolumna {i+1}. SPEŁNIA WARUNKI SUDOKU.****")
        else:
            print(f"Kolumna {i+1}. nie spełnia warunków sudoku.")


for a in range(0, 9, 3):
    build_rows(a, a + 3)

check_columns()
check_rows()
