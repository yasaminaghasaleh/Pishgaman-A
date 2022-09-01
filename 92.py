lines = open("words.txt").readlines()
# lines.sort(key=len)
# print(lines[-1])

# maximum = max(lines,key=len)
# print(len(maximum))
#-----------------------------------------------

# lines.sort(key=len)
# print(lines[0])

minimum = min(lines,key=len)
print(len(minimum))
