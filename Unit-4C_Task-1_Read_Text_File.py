# program that reads sample.txt and displays its content
filename = "sample.txt"
with open(filename, "r") as file:
    content = file.read()
print(content)