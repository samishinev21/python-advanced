list = input().split(" ")
stack = []
result = []

for n in list:
    stack.append(n)
    
while len(stack) > 0:
    result.append(stack.pop())

print(" ".join(result))