"""
author:         Akim Khabibullin
date:           6/2/2025
class:          DEV 108
description:    plays a game of rock paper sciccors with the user and computer and displays results of all games combined at the end.
"""
import random

def printWelcome():
    # prints the welcome message and the rules of the Rock-Paper-Scissors game.
    print("Welcome to Rock/Paper/Scissors game")
    print("\nRules of the game:")
    print("   You and the computer will each pick (r)ock, (p)aper or (s)cissors.")
    print("   The winner will be decided using following policy:")
    print("   Rock wins over Scissors but loses to Paper.")
    print("   Scissors wins over Paper but loses to Rock.")
    print("   Paper wins over Rock but loses to Scissors.")
    print("\n   Let the game begin!! Enter 'q' to quit.\n")

def getUserPick():
    # prompts the user to pick (r)ock, (p)aper, (s)cissors, or 'q' to quit.
    # returns the users pick as a string.
    valid_choices = ['r', 'p', 's', 'q']
    while True:
        user_input = input("Your turn. Pick (r)ock, (p)aper, (s)cissors or (q)to quit: ").lower()
        if user_input in valid_choices:
            return user_input
        print("Invalid choice. Please enter 'r', 'p', 's', or 'q'.")

def pickRPS():
    # randomly selects and returns the computer's pick rock, paper, or scissors
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def getResult(user, computer):
    # determines the winner based on the users and computers choices and alsoreturns tie, user, or computer
    user = user.lower()
    # truns the users response into a string and the full word so r->rock so on
    if user == 'r':
        user_full = 'rock'
    elif user == 'p':
        user_full = 'paper'
    elif user == 's':
        user_full = 'scissors'
    # decides who is the winner by the rules
    if user_full == computer:
        return 'tie'
    elif (user_full == 'rock' and computer == 'scissors')or(user_full == 'scissors' and computer == 'paper')or(user_full == 'paper' and computer == 'rock'):
        return 'user'
    else:
        return 'computer'

def main():
    # the main that basically runs the Rock Paper Scissors game
    printWelcome()
    countUserWins = 0
    countComputerWins = 0
    countTies = 0
    countTotal = 0
    user_pick = getUserPick()
    #while user doesnt quit or type q it continues playing a game wiht the user
    while user_pick != 'q':
        computer_pick = pickRPS()
        winner = getResult(user_pick, computer_pick)
        user_full = ""
        if user_pick == 'r':
            user_full = 'rock'
        elif user_pick == 'p':
            user_full = 'paper'
        elif user_pick == 's':
            user_full = 'scissors'
        
        print(f"You picked {user_pick} Computer picked {computer_pick}")
        # displays the result fo the game and saves the data for later
        if winner == 'tie':
            print("Its a tie!")
            countTies += 1
        elif winner == 'user':
            print("You win")
            countUserWins += 1
        else:
            print("Computer wins")
            countComputerWins += 1
        
        countTotal += 1
        
        user_pick = getUserPick()
    # shows the data for the games all together
    print(f"Number of rounds: {countTotal}")
    print(f"Number of times you won {countUserWins}")
    print(f"Number of times Computer won {countComputerWins}")
    print(f"Number of ties : {countTies}")
    print("Bye")
    
# calls the main
main()
