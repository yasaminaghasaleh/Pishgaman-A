# def f1(text):
#     words = text.split()
#     lengths = [len(i) for i in words]
#     longest = max(lengths)
#
#     for i in words:
#         if len(i) == longest:
#             return i
#
#
# print(f1("python is a good programming language"))

# def f2(text):
#     words = text.split()
#     words.sort(key=len)
#     return words[-1]
#
#
# print(f2("python is a good programming language"))

def f3(text):
    words = text.split()
    return max(words, key=len)


print(f3("python is a good programming language"))
