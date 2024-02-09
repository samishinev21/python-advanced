numbers = open("C:\\Projects\\python-advanced\\10-lab-file-handling\\numbers.txt")
sum = 0

for line in numbers:
    sum += int(line)

print(sum)