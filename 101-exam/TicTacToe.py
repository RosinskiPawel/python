#this is my version of TicTacToe game
print("This is an ampty matrix we will use to play a TicTacToe game: ")
matrix_proj = ['[ ]', '[ ]', '[ ]']
for i in matrix_proj:
    print(f"{i} {i} {i}")
print("every cell has its own coordinates")
matrix_num = [[1.1, 1.2, 1.3], [2.1, 2.2, 2.3], [3.1, 3.2, 3.3]]
print(f"{matrix_num[0]}\n{matrix_num[1]}\n{matrix_num[2]}")

print(f"If you want to choose one, input its coordinates: for example (2,2). \
You can see below how we have chenged the value in the cell: ")
matrix_num[1][1] = 'X'
print(f"{matrix_num[0]}\n{matrix_num[1]}\n{matrix_num[2]}")
matrix_empty = [' ',' ',' '], [' ',' ',' '], [' ',' ',' ']
first_turn_player = input("place the 'x' ").split('.')
matrix_empty[int(first_turn_player[0])-1][int(first_turn_player[1])-1] = 'X'
print(f"{matrix_empty[0]}\n{matrix_empty[1]}\n{matrix_empty[2]}")
