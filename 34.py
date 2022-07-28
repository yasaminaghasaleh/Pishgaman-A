numbers = [1, 2, 3, 4, 5]

for i in range(4):
    n = int(input("Entry : "))
    if 5 < n < 10 :
        numbers.append(n)

numbers.sort()
print(numbers)
