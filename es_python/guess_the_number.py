import random

attempts = 0
rand = random.randint(1,100)
flag = False
print("Welcome to the game !!\nYou have 7 tries to guess the secret number!")

while not flag and attempts <= 7:
    guess = int(input("Guess the Number --> "))
    if guess < rand :
        print("Higher!")
    elif guess > rand :
        print("Lower!")
    else :  
        flag = True
    attempts += 1
    
if flag == True :
    print("Congratulations")
else :
    print("You have failed!")