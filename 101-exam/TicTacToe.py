#this is my version of TicTacToe game



import random

matrix = [[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]
print(f"{matrix[0]}\n{matrix[1]}\n{matrix[2]}")
pool = [0.0, 0.1, 0.2, 1.0, 1.1, 1.2, 2.0, 2.1, 2.2]


def horizontal_win():
    for i in range(0,3):
        if (' ' in matrix[i]) == False and ('O' in matrix[i]) == False:
            print("You win!")
        elif (' ' in matrix[i]) == False and ('X' in matrix[i]) == False:
            print("I win!")
                
def vertical_win():
    matrix_vert = [[matrix[0][0], matrix[1][0], matrix[2][0]], [matrix[0][1], matrix[1][1], matrix[2][1]], [matrix[0][2], matrix[1][2], matrix[2][2]]]
    for i in range(0,3):
        if (' ' in matrix_vert[i]) == False and ('O' in matrix_vert[i]) == False:
            print("You win!")
        elif (' ' in matrix_vert[i]) == False and ('X' in matrix_vert[i]) == False:
            print("I win!")
                            
def diagonal_win():
    matrix_diag = [[matrix[0][0], matrix[1][1], matrix[2][2]], [matrix[0][2], matrix[1][1], matrix[2][0]]]
    for i in range(0,2):
        if (' ' in matrix_diag[i]) == False and ('O' in matrix_diag[i]) == False:
            print("You win!")
        elif (' ' in matrix_diag[i]) == False and ('X' in matrix_diag[i]) == False:
            print("I win!")
                
                
while len(pool) > 0:
    
    print(f"-----------------\n")
    
    chosen_by_player = input("Please place the 'X' ")
    player = chosen_by_player.split('.')
    matrix[int(player[0])][int(player[1])] = 'X'
    print(f"{matrix[0]}\n{matrix[1]}\n{matrix[2]}")
    horizontal_win()
    vertical_win()
    diagonal_win()
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
    horizontal_win()
    vertical_win()
    diagonal_win()
   
    
    
    
    
        
                
    