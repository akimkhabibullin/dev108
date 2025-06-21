# by Akim Khabibullin
# 6/18/25
# this program gives the user 10 tries to break a 4 digit code and gives them hints along the way
import random

def generate_code():
    # generates a 4 digit secret code with unique digits from 1 to 6
    return random.sample(range(1, 7), 4)

def get_guess():
    # asks the user for a guess and validates it
    while True:
        guess_str = input("Enter your guess: ")
        if len(guess_str) != 4:
            print("Please enter exactly 4 digits.")
            continue
        if not guess_str.isdigit():
            print("Please enter digits only.")
            continue
        if any(d < '1' or d > '6' for d in guess_str):
            print("Each digit must be between 1 and 6.")
            continue
        if len(set(guess_str)) != 4:
            print("All digits must be unique.")
            continue
        return [int(d) for d in guess_str]

def analyze_guess(code, guess):
    # compares the guess against the code and returns the number of exact and partial matches
    exact = 0
    for i in range(4):
        if guess[i] == code[i]:
            exact += 1
    code_remaining = []
    guess_remaining = []
    for i in range(4):
        if guess[i] != code[i]:
            code_remaining.append(code[i])
            guess_remaining.append(guess[i])
    partial = 0
    for digit in guess_remaining:
        if digit in code_remaining:
            partial += 1
            code_remaining.remove(digit)
    return exact, partial

def main():
    # main function to run the Code Breaker game
    secret_code = generate_code()
    max_attempts = 10
    history = []
    
    print("Welcome to Code Breaker Program")
    print("You have 10 attempts to break the 4-digit code of digits 1-6.")
    print("Let's start:")
    
    for attempt in range(1, max_attempts + 1):
        user_guess = get_guess()
        exact_matches, partial_matches = analyze_guess(secret_code, user_guess)
        history.append((user_guess, exact_matches, partial_matches))
        
        print(f"Feedback {attempt}: {exact_matches} digits with exact match / {partial_matches} with partial match")
        
        if exact_matches == 4:
            print(f"Hurray! You cracked the code in {attempt} number of attempts")
            break
    else:
        print("Sorry, you exhausted number of guesses. Secret code was:")
        print(secret_code)
    
    print("Your attempt history:")
    for idx, (guess, exact, partial) in enumerate(history, start=1):
        print(f"{idx}: {guess} ({exact}, {partial})")
    
    print("Goodbye!")
# runs the main 
if __name__ == "__main__":
    main()
