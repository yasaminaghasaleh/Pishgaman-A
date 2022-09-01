# lines = open("words.txt").readlines()
# output = ""
#
# for i in lines :
#     if len(i) == 6 :
#         output += i
#
# new_file = open("5letter.txt","w")
# new_file.write(output)
# print("done")
#-------------------------------------------------

lines = open("words.txt").readlines()
five_letters = [ i for i in lines if len(i) == 8 ]

output = "".join(five_letters)
print(output)
open("7letter.txt","w").write(output)
print("done")

#-------------------------------------------------

# lines = open("words.txt").readlines()
# five_letters = [line for line in lines if len(line) is 6]
#
# for line in five_letters :
#     open("5letter.txt","a+").write(line)
#
# print("done")
