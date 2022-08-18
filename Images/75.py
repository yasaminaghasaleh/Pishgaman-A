def prime_status(number):
    divs = [i for i in range(1, number + 1) if number % i == 0]

    # if len(divs) == 2:
    #     return True
    # else:
    #     return False

    print("Aval") if len(divs) == 2 else print("Morakab")
    return True if len(divs) == 2 else False


print(prime_status(int(input("Entry : "))))
