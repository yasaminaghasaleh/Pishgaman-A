brands = ["mercedes", "toyota", "kia", "bmw", "saipa"]

# lengths = [ len(i) for i in brands ]
# print(lengths)

lengths = { x:len(x) for x in brands }
print(lengths)
