# lines = open("words.txt", "r").readlines()
#
# lst = [line[:-1] for line in lines]
#
# output = "".join(lst)
#
# open("One-Line.txt", "w").write(output)

with open("words.txt", "r") as lines:
    lst = [line[:-1] for line in lines]
    output = "".join(lst)
    open("One-Line.txt", "w").write(output)

print("Done")
