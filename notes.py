import random

matrix_master = [['0.0','0.1','0.2'], ['1.0','1.1','1.2'], ['2.0','2.1','2.2']]
winner = False

def horizontal_win(a,b):
    for i in range(0,3):
        if (' ' in matrix[i]) == False and ('O' in matrix[i]) == False:
            print(f"{a} wins!")
            winner = True 
            return winner
        elif (' ' in matrix[i]) == False and ('X' in matrix[i]) == False:
            print(f"{b} wins!")
            winner = True 
            return winner
                                   
def vertical_win(a, b):
    matrix_vert = [[matrix[0][0], matrix[1][0], matrix[2][0]], [matrix[0][1], matrix[1][1], matrix[2][1]], [matrix[0][2], matrix[1][2], matrix[2][2]]]
    for i in range(0,3):
        if (' ' in matrix_vert[i]) == False and ('O' in matrix_vert[i]) == False:
            print(f"{a} wins!")
            winner = True 
            return winner
        elif (' ' in matrix_vert[i]) == False and ('X' in matrix_vert[i]) == False:
            print(f"{b} wins!")
            winner = True 
            return winner
                            
def diagonal_win(a, b):
    matrix_diag = [[matrix[0][0], matrix[1][1], matrix[2][2]], [matrix[0][2], matrix[1][1], matrix[2][0]]]
    for i in range(0,2):
        if (' ' in matrix_diag[i]) == False and ('O' in matrix_diag[i]) == False:
            print(f"{a} wins!")
            winner = True 
            return winner
        elif (' ' in matrix_diag[i]) == False and ('X' in matrix_diag[i]) == False:
            print(f"{b} wins!")
            winner = True 
            return winner

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
                    if (horizontal_win('Player', 'Computer') == True or vertical_win('Player', 'Computer') == True or diagonal_win('Player', 'Computer') == True):
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
                        if (horizontal_win('Player', 'Computer') == True or vertical_win('Player', 'Computer') == True or diagonal_win('Player', 'Computer') == True):
                            print("The End")
                            break
                        
            break
        
    else:
        while winner == False:
            
            while True:
                try:
                    chosen_by_player = input("Player 1: Please put the 'X': ")
                    player = chosen_by_player.split('.')
                    pool.remove(float(chosen_by_player))
                    matrix[int(player[0])][int(player[1])] = 'X'
                        
                except (IndexError, ValueError):
                        print("Wrong value! Try again!")
                    
                else:
                    print(f"{matrix[0]}\n{matrix[1]}\n{matrix[2]}")
                    if (horizontal_win('Player 1', 'Player 2') == True or vertical_win('Player 1', 'Player 2') == True or diagonal_win('Player 1', 'Player 2') == True):
                        print("The End")
                        break
                    elif len(pool)==0:
                        print("The End. Draw!")
                        break
                    else:                        
                        try:
                            chosen_by_player2 = input("Player 2: Please put the 'O': ")
                            player2 = chosen_by_player2.split('.')
                            pool.remove(float(chosen_by_player2))
                            matrix[int(player2[0])][int(player2[1])] = 'O'
                            
                        except (IndexError, ValueError):
                            print("Wrooooong value! Try again!")
                            
                        else:
                            print(f"{matrix[0]}\n{matrix[1]}\n{matrix[2]}\n")    
                            if (horizontal_win('Player 1', 'Player 2') == True or vertical_win('Player 1', 'Player 2') == True or diagonal_win('Player 1', 'Player 2') == True):
                                print("The End")
                                break                                
                        
                                                                                                                     
            break #ten brejk musi tu zostac
            

    question = input("Wanna play again? (y/n):  ").lower()
    if (question == 'y'): 
        True
    else:
        print("Thank you!")
        break                  
    
    
        
        
        
        
        import random

matrix_master = [['0.0','0.1','0.2'], ['1.0','1.1','1.2'], ['2.0','2.1','2.2']]
winner = False

def horizontal_win(a,b):
    for i in range(0,3):
        if (' ' in matrix[i]) == False and ('O' in matrix[i]) == False:
            print(f"{a} wins!")
            winner = True 
            return winner
        elif (' ' in matrix[i]) == False and ('X' in matrix[i]) == False:
            print(f"{b} wins!")
            winner = True 
            return winner
                                   
def vertical_win(a, b):
    matrix_vert = [[matrix[0][0], matrix[1][0], matrix[2][0]], [matrix[0][1], matrix[1][1], matrix[2][1]], [matrix[0][2], matrix[1][2], matrix[2][2]]]
    for i in range(0,3):
        if (' ' in matrix_vert[i]) == False and ('O' in matrix_vert[i]) == False:
            print(f"{a} wins!")
            winner = True 
            return winner
        elif (' ' in matrix_vert[i]) == False and ('X' in matrix_vert[i]) == False:
            print(f"{b} wins!")
            winner = True 
            return winner
                            
def diagonal_win(a, b):
    matrix_diag = [[matrix[0][0], matrix[1][1], matrix[2][2]], [matrix[0][2], matrix[1][1], matrix[2][0]]]
    for i in range(0,2):
        if (' ' in matrix_diag[i]) == False and ('O' in matrix_diag[i]) == False:
            print(f"{a} wins!")
            winner = True 
            return winner
        elif (' ' in matrix_diag[i]) == False and ('X' in matrix_diag[i]) == False:
            print(f"{b} wins!")
            winner = True 
            return winner

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
                    if (horizontal_win('Player', 'Computer') == True or vertical_win('Player', 'Computer') == True or diagonal_win('Player', 'Computer') == True):
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
                        if (horizontal_win('Player', 'Computer') == True or vertical_win('Player', 'Computer') == True or diagonal_win('Player', 'Computer') == True):
                            print("The End")
                            break
                        
            break
            
            # while True:
                
            #     try: 
            #         chosen_by_player = input("Please put the 'X': ")
            #         player = chosen_by_player.split('.')
            #         pool.remove(float(chosen_by_player))
            #         matrix[int(player[0])][int(player[1])] = 'X'
                    
            #     except (IndexError, ValueError):
            #         print("Wrong value! Try again!")
            #     # except ValueError:
            #     #     print("Please put the 'X' again: ")
            #     finally:
                    
            #         print(f"{matrix[0]}\n{matrix[1]}\n{matrix[2]}")
            #         if (horizontal_win('Player', 'Computer') == True or vertical_win('Player', 'Computer') == True or diagonal_win('Player', 'Computer') == True):
            #             print("The End")
            #             # break
            #         elif len(pool)==0:
            #             print("The End. Draw!")
            #             break
            #         break
                
                    
                
            
            # chosen_by_player = input("Please put the 'X': ")
            # player = chosen_by_player.split('.')
            
            
            
            # matrix[int(player[0])][int(player[1])] = 'X'
            # pool.remove(float(chosen_by_player))
            # print(f"{matrix[0]}\n{matrix[1]}\n{matrix[2]}")
            # if (horizontal_win('Player', 'Computer') == True or vertical_win('Player', 'Computer') == True or diagonal_win('Player', 'Computer') == True):
            #     print("The End")
            #     break
            # if len(pool)==0:
            #     print("The End. Draw!")
            #     break
                
            
            
            # print(f"\nNow it's my turn\n")
            # random_from_pool = random.choice(pool)
            # pool.remove(float(random_from_pool))
            # chosen_by_comp = str(random_from_pool).split('.')
            # matrix[int(chosen_by_comp[0])][int(chosen_by_comp[1])] = 'O'
            # print(f"{matrix[0]}\n{matrix[1]}\n{matrix[2]}\n")
            # if (horizontal_win('Player', 'Computer') == True or vertical_win('Player', 'Computer') == True or diagonal_win('Player', 'Computer') == True):
            #     print("The End")
            #     break
    else:
        while winner == False:
            
            while True:
                try:
                    chosen_by_player = input("Player 1: Please put the 'X': ")
                    player = chosen_by_player.split('.')
                    pool.remove(float(chosen_by_player))
                    matrix[int(player[0])][int(player[1])] = 'X'
                    
                except (IndexError, ValueError):
                    print("Wrong value! Try again!")
                
                else:
                    
                    print(f"{matrix[0]}\n{matrix[1]}\n{matrix[2]}")
                    if (horizontal_win('Player 1', 'Player 2') == True or vertical_win('Player 1', 'Player 2') == True or diagonal_win('Player 1', 'Player 2') == True):
                        print("The End")
                        break
                    elif len(pool)==0:
                        print("The End. Draw!")
                        break
                    
                    while True:
                        
                        try:
                            chosen_by_player2 = input("Player 2: Please put the 'O': ")
                            player2 = chosen_by_player2.split('.')
                            pool.remove(float(chosen_by_player2))
                            matrix[int(player2[0])][int(player2[1])] = 'O'
                        except:
                            print("dupa")
                        else:
                        
                            
                                
                    
                            print(f"{matrix[0]}\n{matrix[1]}\n{matrix[2]}\n")    
                            if (horizontal_win('Player 1', 'Player 2') == True or vertical_win('Player 1', 'Player 2') == True or diagonal_win('Player 1', 'Player 2') == True):
                                print("The End")
                                break    
                            break
                        
                
                # break                                
            break
        break             
        
            # chosen_by_player = input("Player 1: Please put the 'X': ")
            # player = chosen_by_player.split('.')
            # matrix[int(player[0])][int(player[1])] = 'X'
            # pool.remove(float(chosen_by_player))
            # print(f"{matrix[0]}\n{matrix[1]}\n{matrix[2]}")
            # if (horizontal_win('Player 1', 'Player 2') == True or vertical_win('Player 1', 'Player 2') == True or diagonal_win('Player 1', 'Player 2') == True):
            #     print("The End")
            #     break
            # if len(pool)==0:
            #     print("The End. Draw!")
            #     break
            
            # # while True:
            # #     try:
            # #         chosen_by_player2 = input("Player 2: Please put the 'O': ")
            # #         player2 = chosen_by_player2.split('.')
            # #         pool.remove(float(chosen_by_player2))
            # #         matrix[int(player2[0])][int(player2[1])] = 'O'
                    
            # #     except (IndexError, ValueError):
            # #         print("Wrong value! Try again!")
            # #     else:
                    
            # #         print(f"{matrix[0]}\n{matrix[1]}\n{matrix[2]}\n")
            # #         if (horizontal_win('Player 1', 'Player 2') == True or vertical_win('Player 1', 'Player 2') == True or diagonal_win('Player 1', 'Player 2') == True):
            # #             print("The End")
            # #             break
            # #         break
                 
            
             
                    
            # chosen_by_player2 = input("Player 2: Please put the 'O': ")
            # player2 = chosen_by_player2.split('.')
            # matrix[int(player2[0])][int(player2[1])] = 'O'
            # pool.remove(float(chosen_by_player2))
            # print(f"{matrix[0]}\n{matrix[1]}\n{matrix[2]}\n")
            # if (horizontal_win('Player 1', 'Player 2') == True or vertical_win('Player 1', 'Player 2') == True or diagonal_win('Player 1', 'Player 2') == True):
            #     print("The End")
            #     break
    
    question = input("Wanna play again? (y/n):  ").lower()
    if (question == 'y'):
        True
    else:
        print("Thank you!")
        break
        
        
        

    