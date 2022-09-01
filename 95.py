lines = open("words.txt","r").readlines()
items = [ i[0:-1] for i in lines ]
# print(lines[:100])
print(items[:100])
