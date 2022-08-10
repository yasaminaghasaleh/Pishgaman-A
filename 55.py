info = {
    "name": "sony",
    "nationality": "japan",
    "founder": "akio morita",
    "field": "tech company"
}

key = input("Key to search : ")

if key in info.keys():
    print("Founded :", info[key])
else:
    print("Not Found")
