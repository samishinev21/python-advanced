file = open("C:\\Projects\\python-advanced\\11-excercise-file-handling\\text.txt", "r")
result = ""

for i, line in enumerate(file):
    if i % 2 == 0:
        list = []
        for word in reversed(line.split(" ")):
            list.append(word.replace("\n", ""))

        result = " ".join(list)
        
        for sign in result:
            if sign == "-" or sign == "," or sign == "." or sign == "!" or sign == "?":
                result = result.replace(sign, "@")
        
        print(result)