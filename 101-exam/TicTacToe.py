#this is my version of TicTacToe game
# print("This is an ampty matrix we will use to play a TicTacToe game: ")
# matrix_proj = ['[ ]', '[ ]', '[ ]']
# for i in matrix_proj:
#     print(f"{i} {i} {i}")
# print("every cell has its own coordinates")
# matrix_num = [[1.1, 1.2, 1.3], [2.1, 2.2, 2.3], [3.1, 3.2, 3.3]]
# print(f"{matrix_num[0]}\n{matrix_num[1]}\n{matrix_num[2]}")

# print(f"If you want to choose one, input its coordinates: for example (2,2). \
# You can see below how we have chenged the value in the cell: ")
# matrix_num[1][1] = 'X'
# print(f"{matrix_num[0]}\n{matrix_num[1]}\n{matrix_num[2]}")
# matrix_empty = [' ',' ',' '], [' ',' ',' '], [' ',' ',' ']
# first_turn_player = input("So, let's start. Please place the 'X' or 'O' ").split('.')
# matrix_empty[int(first_turn_player[0])-1][int(first_turn_player[1])-1] = 'X'
# print(f"{matrix_empty[0]}\n{matrix_empty[1]}\n{matrix_empty[2]}")


import random


matrix = [' ',' ',' '], [' ',' ',' '], [' ',' ',' ']
# print(f"{matrix[0]}\n{matrix[1]}\n{matrix[2]}")
pool = [0.0, 0.1, 0.2, 1.0, 1.1, 1.2, 2.0, 2.1, 2.2]
while len(pool) > 0:
    
    print(f"-----------------\n")
    
    chosen_by_player = input("Please place the 'X' ")
    player = chosen_by_player.split('.')
    matrix[int(player[0])][int(player[1])] = 'X'
    print(f"{matrix[0]}\n{matrix[1]}\n{matrix[2]}")
    pool.remove(float(chosen_by_player))
    if (len(pool)==0):
        print("The End")
        break
    
    print(f"-----------------\n")
    print(f"Now it's my turn\n\n")
    
    random_from_pool = random.choice(pool)
    pool.remove(float(random_from_pool))
    chosen_by_comp = str(random_from_pool).split('.')
    # matrix[int(player[0])][int(player[1])] = 'X'
    matrix[int(chosen_by_comp[0])][int(chosen_by_comp[1])] = 'O'
    print(f"{matrix[0]}\n{matrix[1]}\n{matrix[2]}")
    
   
    
    