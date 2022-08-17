def f(items):
    numbers = []

    for i in items:
        if type(i) in [int, float]:
            numbers.append(i)

    return numbers


entries = ["apple", 1, 4.5, "sony", "toyota", False, {}, 12]

print(f(entries))
