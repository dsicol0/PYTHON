menu = {"pizza" : 5.0,
        "fries" : 3.5, 
        "nuggets" : 3.0,
        "hamburger" : 4.5,
        "cheescake" : 3,
        "toast" : 2.5,
        "coca cola" : 1.5,
        "water" : 1.0}

cart = []
total = 0

print("------  MENU  ------")
for key, value in menu.items():
    print(f"{key:10} : {value:.2f}€")
print("--------------------")

while True:
    food = input("Select an item (q to quit) --> ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

for food in cart:
    total += menu.get(food)
    print(food, end = "")
    print()

print()
print(f"Total is : {total:.2f}€")
print("--------------------")

print("GOODBYE !! :)")