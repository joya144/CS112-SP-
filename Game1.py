#File:CS112_A1_T2_Game1_20230110
#Purpose:the player who reaches to number 100 first is the winner
#Author:Joy alaa fathy sadkey
#ID:20230110


import sys

#welcome message and display status
print ("Welcome to 100 game")
print ("the winner is whoever reaches number 100 first")

#Set numbers
num = 0
the_rest = 100

#Game playing
#player 1's turn
while num < 100:
    try:
        move =int(input("player 1: please add 1-10 numbers"))
        #check if the input is within the valid range
        while move < 1 or move > 10:
             print("please select valid number")
             move =int(input("player 1: please add 1-10 numbers"))
    except ValueError:
        print ("please select a valid choose")
        continue
    
    #the sum of the number they have
    num += move
    #the remaining number until they reach 100
    the_rest -= move
    print (f'Now we have {num}')

    #check if player 1 has won
    if num == 100:
        print ("player 1 is the winner")
        break

    #check if player 1 exceeded 100
    while num >= 100 :
        print ("please choose another number, you must stop at 100")
        the_rest += move
        num -= move
        print (f'Now we have {num}')
        move =int(input("player 1: please enter number less than or equal the rest number until 100"))
        
        if move > the_rest:
            the_rest -= move
            num += move
            continue
        
        elif move < the_rest:
            num += move
            the_rest -= move
            print (f'Now we have {num}')
            continue
        
        else :
            print ("player 1 is the winner")
            #call the function
            sys.exit()
            
    #player 2's turn
    while True:
        try:
            move =int(input("player 2: please add 1-10 numbers"))
            #check if the input is within the valid range
            while move < 1 or move > 10:
                 print("please select valid number")
                 move =int(input("player 2: please add 1-10 numbers"))
        except ValueError:
            print ("please select a valid choose")
            continue
        break
    
    #the sum of the number they have
    num += move
    #the remaining number until they reach 100
    the_rest -= move
    print (f'Now we have {num}')

    # check if player 2 has won
    if num == 100 :
        print("player 2 is the winner")
        break

    #check if player 1 exceeded 100
    while num >= 100 :
        print ("please choose another number, you must stop at 100")
        the_rest += move
        num -= move
        print (f'Now we have {num}')
        move =int(input("player 2: please enter number less than or equal the rest number until 100"))
        
        if move > the_rest:
            the_rest -= move
            num += move
            continue
        
        elif move < the_rest:
            num += move
            the_rest -= move
            print (f'Now we have {num}')
            continue
        
        else :
            print ("player 2 is the winner")
            #call the function
            sys.exit()
   
