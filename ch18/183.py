# Write function that takes variable number of text files
# Concatenates them as one file
n = open(*kwargs, mode = "r", encoding = "utf-8")
f = open("data/flatland.txt", mode = "r", encoding = "utf-8")
g = open("data/flatland01.txt", mode = "r")
new_file = open("data/new_file", mode = "w", encoding = "utf-8")

new_file.write(f.read() + n.read() + g.read())

new_file.close()
g.close()
f.close()
n.close()

print(new_file)