items = [4,5,6.5,"Farzad",7,"James",10]
reshteha = []

for item in items :
    # if type(item) == str :
    if type(item) in [str]:
        reshteha.append(item)

print(reshteha)
