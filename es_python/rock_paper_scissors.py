import random

user_wins = 0
ai_wins = 0
ties = 0

options = ["rock", "paper", "scissors"]

wins_against = {
    "rock" : "scissors",
    "paper" : "rock",
    "scissors" : "paper"
}

while True:
    user_input = input("Type Rock / Paper / Scissors or Q to quit --> ").lower()
    
    if user_input == "q":
        break
    elif user_input not in options:
        print("Input not valid! :( ")
        print()
        continue
    else:
        ai_move = options[random.randint(0,2)]
        print(f"AI picked {ai_move}.")
        if wins_against[user_input] == ai_move:
            print("YOU WON!")
            print()
            user_wins += 1
        elif user_input == ai_move:
            print("IT'S A TIE !!")
            print()
            ties += 1
        else:
            print("YOU LOST !! :(")
            print()
            ai_wins += 1

if ai_wins > 0 or user_wins > 0 or ties > 0:
    print(f"AI WINS --> {ai_wins}")
    print(f"USER WINS --> {user_wins}")
    print(f"TIES --> {ties}")

else:
    print("GOODBYE !")