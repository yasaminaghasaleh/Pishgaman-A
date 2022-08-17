def is_pangram(word):
    new_word = set(word)

    if len(word) == len(new_word):
        return True
    else:
        return False


# print(is_pangram("james"))

if is_pangram("dad") == True:
    print("You are allowed")
else:
    print("You are not allowed")
