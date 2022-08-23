def factorial(n):
    if n == 1:
        return n
        # return 1
    else:
        # print("Step 1 ","N is",n)
        return n * factorial(n - 1)


n = input("Enter any number : ")
# if n > 0 :
#     print(factorial(n))
# elif n == 0 :
#     print("Factorial of zero is 1")
# else :
#     print("Factorial doesn't exist")

try:
    n = int(n)
    try:
        print(factorial(n))
    except RecursionError:
        print("Entry must be larger than 0")
except ValueError:
    print("Entry must be integer")
