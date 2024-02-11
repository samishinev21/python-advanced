text = open("C:\\Projects\\python-advanced\\11-excercise-file-handling\\text.txt", "r")
file = open("C:\\Projects\\python-advanced\\11-excercise-file-handling\\file.txt", "x")

for line_i, line in enumerate(text):
    letters = 0
    marks = 0

    line = line.replace("\n", "")

    for char in line:
        if char == "-" or char == "," or char == "'" or char == "." or char == "?" or char == "!":
            marks += 1
        elif char == " ":
            pass
        else:
            letters += 1

    file.write(f"Line {line_i + 1}: {line} ({letters})({marks})\n")

file.close()