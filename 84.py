# def factorial(n):
#     if n == 1:
#         return n
#         # return 1
#     else:
#         # print("Step 1 ","N is",n)
#         return n * factorial(n - 1)

factorial = lambda n: n if n == 1 else n * factorial(n - 1)
print(factorial(5))
