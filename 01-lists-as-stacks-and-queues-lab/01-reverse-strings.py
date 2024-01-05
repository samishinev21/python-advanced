string = input()
stack = []
result = []

for letter in string:
    stack.append(letter)

for _ in range(len(stack)):
    result.append(stack.pop())

print("".join(result))
