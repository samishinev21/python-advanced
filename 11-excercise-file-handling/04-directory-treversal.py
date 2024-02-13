import os

output_file = open("C:\\Projects\\python-advanced\\11-excercise-file-handling\\report.txt", "w", encoding="utf-8")

hash = {}

for file in os.listdir("C:\\Users\\Sammy\\Downloads\\"):
    tokens = file.split(".")
    extension = tokens[len(tokens) - 1]

    if extension in hash:
        hash[extension].append(file)
    else:
        hash[extension] = [file]

for extension, files in hash.items():
    output_file.write(f".{extension}\n")
    
    for file in files:
        output_file.write(f"- - - {file}\n")