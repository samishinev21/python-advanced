expression = input()
stack = []

for i, sign in enumerate(expression):
    if sign == "(":
        stack.append(i)

    elif sign == ")":
        opening_position = stack.pop()
        print(expression[opening_position:i + 1])
