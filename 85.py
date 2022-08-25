# def is_pangram(word):
#     new_word = set(word)
#
#     if len(word) == len(new_word):
#         return True
#     else:
#         return False

pangram = lambda word : True if len(word) == len(set(word)) else False
print(pangram("mohammad"))
