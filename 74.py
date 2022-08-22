def calculator(n1, op, n2):
    def add():
        return n1 + n2

    def minus():
        return n1 - n2

    def multiply():
        return n1 * n2

    def divide():
        return n1 / n2

    def power():
        return n1 ** n2

    if op == "+":
        print(add())
    elif op == "-":
        print(minus())
    elif op == "/":
        print(divide())
    elif op == "*":
        print(multiply())
    elif op == "**":
        print(power())
    else :
        print("Invalid Output")


n1 = int(input("Enter number 1 : "))
op = input("Enter operator : ")
n2 = int(input("Enter number 2 : "))

calculator(n1, op, n2)
