# numbers = []
#
# for i in range(5):
#     x = float(input("Entry : "))
#     numbers.append(x)
#
# numbers.sort()
# print(numbers)

# ---------------------------------------------

# numbers = list()
#
# for i in range(5):
#     x = float(input("Entry : "))
#     numbers.append(x)

# maximum = 0
#
# for n in numbers:
#     if n > maximum:
#         maximum = n
#
# print("Max is :", maximum)

#------------------------

numbers = list()

for i in range(5):
    x = float(input("Entry : "))
    numbers.append(x)

print(max(numbers))
