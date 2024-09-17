import random
import math
import numpy as np   

def check_move(board, turn, index, push_from):
    n = int (math.sqrt(len(board)))
    outer_layer = []
    if board[index]!=0 and board[index] != turn: #check if selected piece is valid
        return False
    for i in range(n): #check if selected piece can push from top
        outer_layer.append(i)
        if index == i and push_from == 'T':
            return False
    for i in range((n-1)*n,n**2): #check if selected piece can push from bottom
        outer_layer.append(i)    
        if index == i and push_from == 'B':
            return False
    for i in range (0,(n*(n-1))+1,n): #check if selected piece can push from left
        outer_layer.append(i)    
        if index == i and push_from == 'L':
            return False 
    for i in range (n-1,n**2,n): #check if selected piece can push from right
        outer_layer.append(i)    
        if index == i and push_from == 'R':
            return False
    if index not in outer_layer:
        return False
    return True
              
def apply_move(board, turn, index, push_from):
    index_list = list(range(int(len(board))))
    n = int(math.sqrt(len(board)))
    chunks = [board[x:x+n] for x in range(0, len(board), n)] #split board into rows
    
    find_block_row = [index_list[x:x+n] for x in range(0, len(board), n)] #only consider row of chosen block
    for row in range(len(find_block_row)):
        if index in find_block_row[row]:
            index_in_row = find_block_row[row].index(index)
            break
    
    if push_from == 'R':
        chunks[row].pop(index_in_row)
        chunks[row].append(turn)
        temp_board = [item for sublist in chunks for item in sublist] #turn board back into a 1d array
        return temp_board
    
    if push_from == 'L':
        chunks[row].pop(index_in_row)
        chunks[row].insert(0, turn)
        temp_board = [item for sublist in chunks for item in sublist]
        return temp_board
    
    find_block_col = np.array(find_block_row).T.tolist() #flip the board 90 degrees
    chunks = np.array(chunks).T.tolist()
    for col in range(len(find_block_col)):
        if index in find_block_col[col]:
            index_in_col = find_block_col[col].index(index)
            break
        
    if push_from == 'B':
        chunks[col].pop(index_in_col)
        chunks[col].append(turn)
        chunks = np.array(chunks).T.tolist()
        temp_board = [item for sublist in chunks for item in sublist]
        return temp_board
    
    if push_from == 'T':
        chunks[col].pop(index_in_col)
        chunks[col].insert(0, turn)
        chunks = np.array(chunks).T.tolist()
        temp_board = [item for sublist in chunks for item in sublist]
        return temp_board

def check_victory(board, who_played):
    n = int(math.sqrt(len(board)))  
    player_1=0 
    player_2=0   
    count_5=0 
    count_6=0 
    count_7=0 
    count_8=0
    for y in range(n,0,-1): #check each column
        count_1 = 0
        count_2 = 0
        for i in range(n-y,len(board),n): 
                if board[i]==1: 
                    count_1+=1 
                    if count_1==n: 
                        player_1+=1 
                elif board[i]==2: 
                    count_2+=1 
                    if count_2==n: 
                        player_2+=1 
    for x in range(0,n**2,n): #check each row
        count_3 = 0
        count_4 = 0
        for i in range(x, x+n):
                if board[i]==1: 
                    count_3+=1 
                    if count_3==n: 
                        player_1+=1 
                elif board[i]==2: 
                    count_4+=1 
                    if count_4==n: 
                        player_2+=1     
    for i in board[0:n**2:n+1]: #check diagonal from left to right
        if i==1: 
            count_5+=1 
            if count_5==n: 
                return 1 
        elif i==2: 
            count_6+=1 
            if count_6==n: 
                return 2     
    for i in board[n-1:(n-1)*n+1:n-1]: #check diagonal from right to left  
         if i==1: 
             count_7+=1 
             if count_7==n: 
                 return 1 
         elif i==2: 
             count_8+=1 
             if count_8==n: 
                 return 2
    if player_1>=1 and player_2==0: 
        return 1 
    elif player_1==0 and player_2>=1: 
        return 2 
    elif player_1==0 and player_2==0: 
        return 0 
    elif player_1>=1 and player_2>=1: #check 2 players get full column/ row at same time
        if who_played==1: 
            return 2 
        elif who_played==2: 
            return 1
       
def computer_move(board, turn, level):  
    n = int (math.sqrt(len(board)))   
    outer_layer = []   
    for i in range(n): #index for first row 
        outer_layer.append(i)   
    for i in range((n-1)*n,n**2):  #index for last row 
        outer_layer.append(i)  
    for i in range (0,n*(n-1)+1,n):   #index for first column
        outer_layer.append(i)       
    for i in range (n-1,n**2,n):   #index for last column
        outer_layer.append(i) 
    outer_layer.remove(0) #so that the probability of each index in the outer layer being chosen is the same
    outer_layer.remove(n-1)
    outer_layer.remove((n-1)*n)
    outer_layer.remove((n**2)-1)
    
    if level == 1:  
        index_list = [i for i in outer_layer if board[i] ==0 or board[i]== turn]
        number = random.randrange(len(index_list))  
        index= index_list[number] 
        if index in range(1,n-1):  
            possible_moves = ['B', 'R', 'L']  
        elif index == 0:  
            possible_moves = ['B', 'R']  
        elif index == n-1:  
            possible_moves = ['B', 'L']  
        elif index in range(n, (n-2)*n +1, n):  
            possible_moves = ['B', 'R', 'T']  
        elif index in range((2*n)-1, (n-1)*n, n):  
            possible_moves = ['B', 'T', 'L']  
        elif index == (n-1)*n:  
            possible_moves = ['R', 'T']  
        elif index == n**2-1:
            possible_moves = ['T', 'L']
        elif index in range((n-1)*n +1, n**2 -1):  
            possible_moves = ['R', 'T', 'L']  
        move1 = random.randrange(len(possible_moves))  
        push_from = possible_moves[move1] 
        return(index,push_from)
        
    elif level == 2:   
        directions = ['B', 'L', 'R', 'T']   
        computer_valid_moves= []  
          
        for x in outer_layer: #move that leads to direct victory   
            for y in directions:   
                if check_move(board, turn, x, y) == True:   
                    if check_victory (apply_move(board, turn, x, y), turn) == turn:   
                        return (x,y)   
                              
        for x in outer_layer: #move that wont let the player win in the next move   
            for y in directions:  
                turn = 2 
                if check_move(board, turn, x, y) == True:   
                    computer_valid_moves.append((x,y))   
                    if check_victory(apply_move(board, turn, x, y), turn) == 1:  
                        computer_valid_moves.remove((x,y))  #remove the move that makes player the winner 
                    elif check_victory(apply_move(board, turn, x, y), turn) == 0:  
                        turn = 1                 
                        for v in outer_layer:  
                            for w in directions:  
                                if check_move(apply_move(board, 2, x, y),turn,v,w) == True: 
                                    if check_victory(apply_move(apply_move(board,2,x,y),turn,v,w),turn) == 1: #prevent player from winning by doing the move that allows them to win NEXT                                 
                                        computer_valid_moves.remove((x,y)) 
                                        break 
                            else: 
                                continue 
                            break 
                         
        if computer_valid_moves == []: #no moves can prevent player 1 from winning so just play a random valid move 
            for x in outer_layer: 
                for y in directions: 
                    if check_move(board,2,x,y) == True: 
                        computer_valid_moves.append((x,y)) 
                         
        move2 = random.randrange(len(computer_valid_moves)) #random valid move   
        random_move = computer_valid_moves[move2]   
        return(random_move)
def display_board(board):
    n = int(math.sqrt(len(board))) 
    chunks = [board[x:x+n] for x in range(0, len(board), n)] 
    for i in range(len(chunks)): 
           print(chunks[i])

def menu():
    while True: 
        print ('Welcome to Quixo!') 
        print('Enter quit below if you yould like to quit the game now.')
        print ('Would you like to play with another player or computer? ') 
        game_mode = input ('Enter player or computer: ') 
        while True: 
            if game_mode == 'quit':
                return None
            elif game_mode != 'player' and game_mode != 'Player' and game_mode != 'Computer' and game_mode != 'computer': 
                print('Error, choose between player or computer: ') 
                game_mode = input ('Enter player or computer: ') 
            elif game_mode == 'Player' or game_mode == 'player': 
                print ('Game mode =', game_mode)
                break
            elif game_mode =='Computer' or 'computer':
                print ('Game mode =', game_mode)
                break
                
        while True:
                try:
                    n = int(input("Enter size n of the board: "))
                    assert n>1 
                    print('n =',n)
                    break 
                except ValueError:
                    print("Error, choose a valid number!")
                except AssertionError:
                    print("Error, choose a valid number!")   
                    
        board = [] 
        for x in range(n): 
            for y in range(n): 
                board.append(0) 
        display_board(board)             
             
            
        if game_mode == 'Player' or game_mode == 'player':   
            who_played = 0
            checkvictory = check_victory(board,who_played)
            count = 0
            while checkvictory == 0:        
                count += 1
                if count%2 == 1: 
                    turn = 1
                    who_played = 1
                    print ("It is now player 1's turn.") 
                else: 
                    turn = 2
                    who_played = 2
                    print ("It is now player 2's turn.")
                    
                while True:  
                    try:  
                        i = int(input('Which row number would you like to pick with 0 being first row? ') )
                        assert 0<=i<n 
                        print('row number =',i)  
                        break   
                    except ValueError:  
                        print("Error, choose a valid number!")  
                    except AssertionError:  
                        print("Error, choose a valid number!") 
                      
                while True:  
                    try:  
                        j = int(input('Which column number would you like to pick with 0 being first column? ')) 
                        assert 0<=j<n   
                        print('column number =',j)  
                        break   
                    except ValueError:  
                        print("Error, choose a valid number!")  
                    except AssertionError:  
                        print("Error, choose a valid number!") 
             
                index = i*n + j 
                print('index =',index)  
                print ('Directions to push from:') 
                print ('B - push from bottom') 
                print ('T - push from top') 
                print ('L - push from left') 
                print ('R - push from right') 
                push_from = input ('Which direction do you want to push from? ')
                
                while True:  
                    if push_from == 'b' or push_from == 'l' or push_from == 'r' or push_from == 't': 
                        print('Error, key in directions to push from in capital letters!') 
                        push_from = input ('Which direction would you like to push from? ')  
                    elif push_from != 'B' and push_from != 'L' and push_from != 'R' and push_from != 'T': 
                        print('Error, choose from directions to push from!') 
                        push_from = input ('Which direction would you like to push from? ')
                    elif push_from == 'B' or push_from == 'L' or push_from == 'R' or push_from == 'T': 
                        print ('push from =', push_from) 
                        break
                    
                checkmove = check_move(board,turn,index,push_from)
                if checkmove == False:
                        print('Error, move is invalid!')
                        count -= 1
                        continue
                    
                applymove = apply_move(board,turn,index,push_from)
                display_board(applymove)
                board = applymove
                
                checkvictory = check_victory(board,who_played)
                if checkvictory == 1:
                    print("Congratulations! Player 1 wins!")
                    print('Would you like to start a new game?')
                    restart = input('Enter YES/NO: ')
                    if restart != 'YES' and restart !='NO':
                        print('Error, please choose between YES or NO!')
                    elif restart == 'YES':
                        menu()
                    elif restart == 'NO': 
                        return None
                    
                elif checkvictory == 2:
                    print("Congratulations! Player 2 wins!")
                    print('Would you like to start a new game?')
                    restart = input('Enter YES/NO: ')
                    if restart != 'YES' and restart !='NO':
                        print('Error, please choose between YES or NO!')
                    elif restart == 'YES':
                        menu()
                    elif restart == 'NO': 
                        return None
                
                while True:
                    print('Would you like to restart the game?')
                    end_game = input("Enter YES/NO: ")
                    if end_game != 'YES' and end_game != 'NO':
                        print('Error, please choose between YES or NO!')
                    elif end_game == 'YES':
                        menu()
                    else:
                        break 
                    
        elif game_mode == 'Computer' or game_mode == 'computer':
            while True: 
                try:
                    level= int(input("Which difficulty level would you like to play (1/2)? "))
                    if level != 1 and level != 2:
                        print('Error, please choose between 1 and 2!')
                    elif level == 1 or level == 2: 
                        print("You are playing with difficulty level",level)
                        break 
                except ValueError:  
                     print('Error, please choose between 1 and 2!')
            
            who_played = 0
            checkvictory = check_victory(board,who_played)
            count = 0
            while checkvictory == 0:  
                count += 1
                if count%2 == 1: 
                    turn = 1
                    who_played = 1
                    print ("It is now your turn.")
                    
                    while True:  
                        try:  
                            i = int(input('Which row number would you like to pick with 0 being first row? ') )
                            assert 0<=i<n 
                            print('row number =',i)  
                            break   
                        except ValueError:  
                            print("Error, choose a valid number!")  
                        except AssertionError:  
                            print("Error, choose a valid number!") 
                          
                    while True:  
                        try:  
                            j = int(input('Which column number would you like to pick with 0 being first column? ')) 
                            assert 0<=j<n   
                            print('column number =',j)  
                            break   
                        except ValueError:  
                            print("Error, choose a valid number!")  
                        except AssertionError:  
                            print("Error, choose a valid number!") 
                 
                    index = i*n + j 
                    print('index =',index)  
                    print ('Directions to push from:') 
                    print ('B - push from bottom') 
                    print ('T - push from top') 
                    print ('L - push from left') 
                    print ('R - push from right') 
                    push_from = input ('Which direction do you want to push from? ')
                    
                    while True:  
                        if push_from == 'b' or push_from == 'l' or push_from == 'r' or push_from == 't': 
                            print('Error, key in directions to push from in capital letters!') 
                            push_from = input ('Which direction would you like to push from? ')  
                        elif push_from != 'B' and push_from != 'L' and push_from != 'R' and push_from != 'T': 
                            print('Error, choose from directions to push from!') 
                            push_from = input ('Which direction would you like to push from? ')
                        elif push_from == 'B' or push_from == 'L' or push_from == 'R' or push_from == 'T': 
                            print ('push from =', push_from) 
                            break
                        
                    checkmove = check_move(board,turn,index,push_from)
                    if checkmove == False:
                            print('Error, move is invalid!')
                            count -= 1
                            continue
                        
                    applymove = apply_move(board,turn,index,push_from)
                    display_board(applymove)
                    board = applymove
                    checkvictory = check_victory(board,who_played)
                    
                    if checkvictory == 1:
                        print("Congratulations! You have won!")
                        print('Would you like to start a new game?')
                        restart = input('Enter YES/NO: ')
                        if restart != 'YES' and restart !='NO':
                            print('Error, please choose between YES or NO!')
                        elif restart == 'YES':
                            menu()
                        elif restart == 'NO': 
                            return None
                        
                    elif checkvictory == 2:
                        print("You have lost the game!")
                        print('Would you like to start a new game?')
                        restart = input('Enter YES/NO: ')
                        if restart != 'YES' and restart !='NO':
                            print('Error, please choose between YES or NO!')
                        elif restart == 'YES':
                            menu()
                        elif restart == 'NO': 
                            return None
                    
                    while True:
                        print('Would you like to restart the game?')
                        end_game = input("Enter YES/NO: ")
                        if end_game != 'YES' and end_game != 'NO':
                            print('Error, please choose between YES or NO!')
                        elif end_game == 'YES':
                            menu()
                        else:
                            break        
                else: 
                    turn = 2 
                    who_played = 2 
                    computermove = computer_move(board, turn, level)
                    print('index computer chose:', computermove[0], ', direction to push from:', computermove[1])
                    applymove = apply_move(board, turn, computermove[0], computermove[1])
                    display_board(applymove)
                    board = applymove
                    checkvictory = check_victory(board,who_played)
                    if checkvictory == 1:
                        print("Congratulations! You have won!")
                        print('Would you like to start a new game?')
                        restart = input('Enter YES/NO: ')
                        if restart != 'YES' and restart !='NO':
                            print('Error, please choose between YES or NO!')
                        elif restart == 'YES':
                            menu()
                        elif restart == 'NO': 
                            return None
                        
                    elif checkvictory == 2:
                        print("You have lost the game!")
                        print('Would you like to start a new game?')
                        restart = input('Enter YES/NO: ')
                        if restart != 'YES' and restart !='NO':
                            print('Error, please choose between YES or NO!')
                        elif restart == 'YES':
                            menu()
                        elif restart == 'NO': 
                            return None
    
if __name__ == "__main__":
    menu()
    