lst1 = [10, 1, 2, 4, 6]
lst2 = [4, 11, 3, 2, 7]
lst3 = []

for i in lst1 :
    if i in lst2 :
        lst3.append(i)

print(lst3)
