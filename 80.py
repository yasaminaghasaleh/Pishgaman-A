def tavan(x, y):
    if y == 1:
        return x
    else:
        return x * tavan(x, y - 1)


print(tavan(2, 4))
