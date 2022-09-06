lines = open("words.txt").readlines()
rev = [line[::-1] for line in lines]
open("Rev.txt", "w").write("".join(rev))


# lines = open("words.txt").readlines()
# open("Rev.txt", "w").write("".join(lines[::-1]))
