length = int(input("How many numbers do yo want : "))
numbers = []


for i in range(length):
    x = float(input("Entry : "))
    numbers.append(x)

print(max(numbers))


#-------------------------------------------------

# end = False
# lst = []
#
# while end == False :
#     entry = input("Entry : ")
#     if entry == "exit" :
#         end = True
#     else :
#         lst.append(int(entry))
#
# print(lst)
