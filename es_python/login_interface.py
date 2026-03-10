from datetime import datetime

def login(): 
    now = datetime.now()
    print(now.strftime("%d/%m/%Y"))
    print(now.strftime("%H:%M:%S"))       
    print(now.strftime("%d %B %Y"))

    print("=================================")
    print("            WELCOME              ")
    print("=================================")

    MAX_ATTEMPTS = 3
    attempts = 0

    with open("secret.txt", "r") as file:
        saved_user = file.readline().strip()
        saved_password = file.readline().strip()

    while attempts < MAX_ATTEMPTS:
        input_user = input("Insert your username --> ")
        input_pw = input("Insert your password --> ")

        if input_user == saved_user and input_pw == saved_password:
            print("Login successful!")
            return True  
        else:
            attempts += 1
            remaining = MAX_ATTEMPTS - attempts
            if remaining > 0:
                print(f"Wrong username or password! {remaining} attempts remaining")
            
    print("Too many failed attempts. Goodbye!")
    return False

def deposit() :
    print("Deposit selected!")

def whitdraw() :
    print("Withdraw selected!")

def check_balance() :
    print("balance selected")

menu = {
    "1" : ("Deposit", deposit),
    "2" : ("Whitdraw", whitdraw),
    "3" : ("Check Balance", check_balance),
    "4" : ("Exit", None)
}

def print_menu() :
    print("\n--- MENU ---")
    for key, (label, _) in menu.items():
        print(f"{key}. {label}")
    

# MAIN 

login()
while True:
        print_menu()
        choice = input("Choose an option: ")

        if choice not in menu:
            print("Invalid option, try again!")
            continue

        label, action = menu[choice]

        if action is None:  # Exit
            print("Goodbye!")
            break
        
        action()