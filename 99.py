# end = False

def signup(user, pw):
    open("DB-USERS.txt", "a+").write(user + "\n")
    open("DB-PASSWORD.txt", "a+").write(pw + "\n")
    print("Account created")


def login(user, pw):
    db_usernames = open("DB-USERS.txt", "r").readlines()
    db_passwords = open("DB-PASSWORD.txt", "r").readlines()
    usernames = [user[:-1] for user in db_usernames]
    passwords = [password[:-1] for password in db_passwords]

    accounts = dict(zip(usernames, passwords))

    if user in accounts:
        if pw == accounts[user]:
            print("Login completed")
            # end = True
        else:
            print("Password was incorrect")
    else:
        print("Account not found")


while True:
    user = input("Enter a username : ")
    pw = input("Enter a password : ")
    login(user, pw)
