ages = {
    "ali": 24,
    "parsa": 14,
    "tina": 31,
    "pedram": 21,
    "siavash": 10,
    "maryam": 30
}

#lst = [i for i in ages.values()]
#print(max(lst))

print(max(*ages.values()))
