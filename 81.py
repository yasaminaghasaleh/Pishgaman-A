def hash(x):
    if len(str(x)) == 1:
        return x
    else:
        # figures = []
        # for i in str(x):
        #     figures.append(int(i))
        x = sum([ int(i) for i in str(x) ])
        return hash(x)


print(hash(int(input("Enter a number to hash : "))))
