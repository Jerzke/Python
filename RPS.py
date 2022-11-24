import random 
import sys

playerCount = input("Would you like to play against the computer or another player? ")
playerCheck = ["Player"]
computerCheck = ["Computer"] 
possible_actions = ["Rock", "Paper", "Scissors"]
user_actions = input("Player 1 choose one! (Rock, Paper or scissors)") 
user1_win = '''
-------------------------
You win, congratulations
-------------------------
'''
user2_win = '''
-------------------------
Player 2 wins, nice!
-------------------------
'''
computer_win = '''
-------------------------
Computer wins, very sad!
-------------------------
'''
computer_actions = random.choice(possible_actions)
    

while playerCount == "Player":
    user2_actions = input("Player 2 choose one! (Rock, Paper or scissors) ")
    print(f"You chose: {user_actions}\nPlayer 2 chose: {user2_actions}")
    if user_actions == user2_actions:  
        print(f"Both players selected {user_actions}. It's a tie!")
    elif user_actions =="Rock":
        if user2_actions == "Scissors":
            print(user1_win)
        else: 
         print(user2_win)
    elif user_actions == "Paper":
        if user2_actions == "Rock":
            print(user1_win)
        else: 
            print(user2_win)
    elif user_actions == "Scissors":
        if user2_actions == "Paper":
            print(user1_win)
        else: 
            print(user2_win)
    break

while playerCount == "Computer":
    print(f"You chose: {user_actions}\nComputer chose: {computer_actions}")
    if user_actions == computer_actions:  
        print(f"Both players selected {user_actions}. It's a tie!")
    elif user_actions =="Rock":
        if computer_actions == "Scissors":
            print(user1_win)
        else: 
         print(computer_win)
    elif user_actions == "Paper":
        if computer_actions == "Rock":
            print(user1_win)
        else: 
            print(computer_win)
    elif user_actions == "Scissors":
        if computer_actions== "Paper":
            print(user1_win)
        else: 
            print(computer_win)
    break
    


    
