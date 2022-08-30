lines = open("words.txt").readlines()
five_letters = [line for line in lines if len(line) is 6]

open("5-Letters.txt", "w").write(five_letters)
print("Done")
