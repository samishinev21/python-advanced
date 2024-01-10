n = int(input())
stack = []

for i in range(n):
    command = input()

    tokens = command.split(" ")

    if tokens[0] == "1":
        stack.append(int(tokens[1]))
    elif tokens[0] == "2":
        if len(stack) > 0:
            stack.pop()
        else:
            continue
    elif tokens[0] == "3":
        print(max(stack))
    elif tokens[0] == "4":
        print(min(stack))

def reverse(a):
    result = []

    while len(a) > 0:
        result.append(a.pop())
        
    return result

result = reverse(stack)
print(", ".join(map(str, result)))