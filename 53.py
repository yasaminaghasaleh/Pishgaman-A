numbers = []

for i in range(3):
    entry = input("Entry : ")

    try:
        n = float(entry)
        if str(n)[-2:] == ".0":
            numbers.append(int(n))
        else :
            numbers.append(n)
    except ValueError:
        print("Noue vorodi sahih nist")
        # raise Exception("Moshkel pish amade kasagam")


print(numbers)
for i in numbers :
    print(type(i))
