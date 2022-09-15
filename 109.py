import random

def generate1():
    password = []

    for i in range(6):
        x = str(random.choice(range(10)))
        password.append(x)

    return "".join(password)


def generate2():
    password = ""

    for i in range(6):
        x = str(random.choice(range(10)))
        password += x

    return password

print(generate2())
