entry = input("Entry : ")
numbers = []

try:
    number = float(entry)
    numbers.append(number)

except ValueError:
    print("Meghdar vorodi sahih nist")

finally:
    print(numbers)
