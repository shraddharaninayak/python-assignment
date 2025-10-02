# Writing to a file

with open("sample.txt", "w") as file:
    file.write("Hello, this is a test file.\n")
    file.write("This file was created using Python.\n")

print("Content written to sample.txt")
