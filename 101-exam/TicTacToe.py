import random

matrix_master = [['0.0','0.1','0.2'], ['1.0','1.1','1.2'], ['2.0','2.1','2.2']]
winner = False

def horizontal_win(a, b):
    for i in range(0,3):
        if matrix[i].count(b) == 3:
            print(f"{a} wins!")
            return True 
    return False             
                                   
def vertical_win(a, b):
    matrix_vert = [[matrix[0][0], matrix[1][0], matrix[2][0]], [matrix[0][1], matrix[1][1], matrix[2][1]], [matrix[0][2], matrix[1][2], matrix[2][2]]]
    for i in range(0,3):
        if matrix_vert[i].count(b) == 3:
            print(f"{a} wins!")
            return True 
    return False           
                            
def diagonal_win(a, b):
    matrix_diag = [[matrix[0][0], matrix[1][1], matrix[2][2]], [matrix[0][2], matrix[1][1], matrix[2][0]]]
    for i in range(0,2):
        if matrix_diag[i].count(b) == 3:
            print(f"{a} wins!")
            return True 
    return False     
        
while True:
    
    pool = [0.0, 0.1, 0.2, 1.0, 1.1, 1.2, 2.0, 2.1, 2.2]  
    matrix = [[' ', ' ',' '], [' ', ' ', ' '], [' ', ' ', ' ']]  
    players_to_choose = input(f"Please choose the players:\n Human vs. Computer = 1\n Player1 vs. Player2 = 2\n\n\t")
    print(f"This is the matrix we will use to play.\n\n{matrix_master[0]}\n{matrix_master[1]}\n{matrix_master[2]}\n")    
    
    if (players_to_choose == '1'):
        
        while winner == False:
            
            while True:
                try: 
                    chosen_by_player = input("Please put the 'X': ")
                    player = chosen_by_player.split('.')
                    pool.remove(float(chosen_by_player))
                    matrix[int(player[0])][int(player[1])] = 'X'
                    
                except (IndexError, ValueError):
                    print("Wrong value! Try again!")
               
                else:
                    print(f"{matrix[0]}\n{matrix[1]}\n{matrix[2]}")
                    if (horizontal_win('Player', 'X') == True or vertical_win('Player', 'X') == True or diagonal_win('Player', 'X') == True):
                        print("The End")
                        break
                    elif len(pool)==0:
                        print("The End. Draw!")
                        break
                    else:
                        print(f"\nNow it's my turn\n")
                        random_from_pool = random.choice(pool)
                        pool.remove(float(random_from_pool))
                        chosen_by_comp = str(random_from_pool).split('.')
                        matrix[int(chosen_by_comp[0])][int(chosen_by_comp[1])] = 'O'
                        print(f"{matrix[0]}\n{matrix[1]}\n{matrix[2]}\n")
                        if (horizontal_win('Computer', 'O') == True or vertical_win('Computer', 'O') == True or diagonal_win('Computer', 'O') == True):
                            print("The End")
                            break
                        
            break
        
    else:
        while winner == False:
            while True:
            
                try:
                    chosen_by_player = input("Player 1: Please put the 'X': ")
                    player1 = chosen_by_player.split('.')
                    # pool.remove(float(chosen_by_player))
                    # matrix[int(player[0])][int(player[1])] = 'X'
                    if matrix[int(player1[0])][int(player1[1])] !=' ':
                        print('Wrong value! Try again!')
                        continue
                    
                    matrix[int(player1[0])][int(player1[1])] = 'X'
                        
                except (IndexError, ValueError):
                        print("Wrong value! Try again!")
                    
                else:
                    print(f"{matrix[0]}\n{matrix[1]}\n{matrix[2]}")
                    if (horizontal_win('Player 1', 'X') == True or vertical_win('Player 1', 'X') == True or diagonal_win('Player 1', 'X') == True):
                        print("The End")
                        break
                    # elif len(pool)==0:
                    elif (matrix[0]+matrix[1]+matrix[2]).count(' ') == 0:
                        print("The End. Draw!")
                        break
                    while True:
                        try:
                            chosen_by_player2 = input("Player 2: Please put the 'O': ")
                            player2 = chosen_by_player2.split('.')
                            
                            # pool.remove(float(chosen_by_player2))
                            
                            if matrix[int(player2[0])][int(player2[1])] !=' ':
                                print('Wrong value! Try again!')
                                continue
                            matrix[int(player2[0])][int(player2[1])] = 'O'
                                                                                    
                        except (IndexError, ValueError):
                            print("Wrooooong value! Try again!")
                            
                        else:
                            print(f"{matrix[0]}\n{matrix[1]}\n{matrix[2]}\n")    
                            if (horizontal_win('Player 2', 'O') == True or vertical_win('Player 2', 'O') == True or diagonal_win('Player 2', 'O') == True):
                                print("The End")
                                break
                           
                            break
                    
                            
            break      

    question = input("Wanna play again? (y/n):  ").lower()
    if (question == 'y'): 
        True
    else:
        print("Thank you!")
        break                  
    
    
        