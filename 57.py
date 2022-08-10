scores = {
    "hesaban": 13,
    "farsi": 14,
    "hendese": 17,
    "zaban": 20,
    "shimi": 8,
    "amar": 16
}

for k, v in scores.items():
    if v >= 10:
        print(k, ": passed")
    else:
        print(k, ": failed")

nomarat = [ i for i in scores.values() ]
moadel = sum(nomarat) / len(nomarat)
print("Moadel :",moadel)
