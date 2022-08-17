def f(x):
    del x[3]
    del x[-2]
    print(x)


f([10, 20, 30, 40, 50, 60, 70])
