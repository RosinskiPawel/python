import random
        
def check_if_hor_win(a, b):
    for i in range(0,3):
        if matrix[i].count(b) == 3:
            print(f'{a} wins!')
            return True 
    return False                                   

def check_if_vert_win(a, b):
    matrix_vert = [[matrix[0][0], matrix[1][0], matrix[2][0]], [matrix[0][1], matrix[1][1], matrix[2][1]], [matrix[0][2], matrix[1][2], matrix[2][2]]]
    for i in range(0,3):
        if matrix_vert[i].count(b) == 3:
            print(f'{a} wins!')
            return True 
    return False                            

def check_if_diag_win(a, b):
    matrix_diag = [[matrix[0][0], matrix[1][1], matrix[2][2]], [matrix[0][2], matrix[1][1], matrix[2][0]]]
    for i in range(0,2):
        if matrix_diag[i].count(b) == 3:
            print(f'{a} wins!')
            return True 
    return False    

def player_turn(player, sign):
    while True:
        try:
            chosen_by_player = input(f"{player}: Please put the '{sign}': ")
            playerXO = chosen_by_player.split('.')
            pool.remove(float(chosen_by_player))
             
            if matrix[int(playerXO[0])][int(playerXO[1])] !=' ':
                print('Wrong value! Try again!')
                chosen_by_player = input(f"This cell is occupied. Please try again to put the '{sign}' : ")
            matrix[int(playerXO[0])][int(playerXO[1])] = f"{sign}"
                
        except (ValueError, IndexError):
            print('Wrong value! Try again!')
        else:
            
            playerXO = chosen_by_player.split('.')
            matrix[int(playerXO[0])][int(playerXO[1])] = f"{sign}"   
            print(f'{matrix[0]}\n{matrix[1]}\n{matrix[2]}')
            if (matrix[0]+matrix[1]+matrix[2]).count(' ') == 0:
                print('The End. Draw!')
                return True
            elif (check_if_hor_win(player, sign) == True or check_if_vert_win(player, sign) == True or check_if_diag_win(player, sign) == True):
                print('The End')
                return True
            return False
            


while True:
    matrix_master = [['0.0','0.1','0.2'], ['1.0','1.1','1.2'], ['2.0','2.1','2.2']]
    winner = False
    pool = [0.0, 0.1, 0.2, 1.0, 1.1, 1.2, 2.0, 2.1, 2.2]  
    matrix = [[' ', ' ',' '], [' ', ' ', ' '], [' ', ' ', ' ']]  
    players_to_choose = input(f'Please choose the players:\n Human vs. Computer = 1\n Player1 vs. Player2 = 2\n\n\t')
    print(f'This is the matrix we will use to play.\n\n{matrix_master[0]}\n{matrix_master[1]}\n{matrix_master[2]}\n')
        
    if (players_to_choose == '1'):
        while winner == False:
                         
            if player_turn("Player1", "X") == True:
                break
            
            print(f"\nNow it's my turn\n")
            
            random_from_pool = random.choice(pool)
            pool.remove(float(random_from_pool))
            chosen_by_comp = str(random_from_pool).split('.')
            matrix[int(chosen_by_comp[0])][int(chosen_by_comp[1])] = 'O'
            print(f"{matrix[0]}\n{matrix[1]}\n{matrix[2]}\n")
            if (check_if_hor_win('Computer', 'O') == True or check_if_vert_win('Computer', 'O') == True or check_if_diag_win('Computer', 'O') == True):
                print('The End')
                break                                                
        
    else:
         while winner == False:
                                
            if player_turn("Player1", "X") == True:
                break
            
            elif player_turn("Player2", "O") == True:
                break
                                                                        
                
    question = input('Wanna play again? (y/n):  ').lower()
    if (question == 'y'):
        True
    else:
        print('Thank you!')
        break
     

