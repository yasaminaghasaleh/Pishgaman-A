entry = input("Type something : ")
output = f"<p>{entry}</p>"
open("Template.html", "w").write(output)
print("Done")
