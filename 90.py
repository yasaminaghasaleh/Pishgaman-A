# lines = open("words.txt").readlines()
# five_letters = []
#
# for line in lines :
#     if len(line) is 6 :
#         five_letters.append(line)
#
# print(five_letters)

lines = open("words.txt").readlines()
five_letters = [line for line in lines if len(line) is 6]
print(*five_letters)
