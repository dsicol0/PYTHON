def view_passwords():
    with open('password.txt','r') as f:
        for line in f.readlines():
            print(line.rstrip())


def add_password():
    application_or_website = input("Application / Website name --> ")
    username_or_email = input("Account name --> ")
    pwd = input("Password --> ")

    with open('password.txt','a') as f:
        f.write(application_or_website + " --> " + username_or_email + " | " + pwd + "\n")


options = {
    "add" : add_password,
    "view" : view_passwords,
    "q" : quit
}


while True:
    print()
    print("Would you like to add a new password or view the existing ones? ")
    print(" < add > for adding a new password")
    print(" < view > for viewing all the password")
    print(" < q > to quit")
    choice = input("Enter your choice --> ")

    options[choice]()