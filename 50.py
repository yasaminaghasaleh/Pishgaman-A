number = int(input("Entry : "))
# divisors = []
#
# for i in range(1, n + 1):
#     if n % i == 0:
#         divisors.append(i)
#
# print("Divisors are :", divisors)

divisors = [i for i in range(1, number + 1) if number % i == 0]

# if len(divisors) == 2 :
if divisors == [1, number]:
    print("The number is Prime")
else:
    print("The Number is not Prime")
