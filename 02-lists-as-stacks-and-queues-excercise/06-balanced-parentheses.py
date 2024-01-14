parentheses = input()
stack = []

def rotate_sign(sign):
    if sign == ")":
        return "("
    elif sign == "]":
        return "["
    elif sign == "}":
        return "{"
    
error = False

for sign in parentheses:
    if sign == "(" or sign == "[" or sign == "{":
        stack.append(sign)
    elif sign == ")" or sign == "]" or sign == "}":
        if len(stack) > 0:
            if stack[len(stack) - 1] == rotate_sign(sign):
                stack.pop()
                continue
            else:
                break
        else:
            error = True

if not error and len(stack) == 0:
    print("YES")
else:
    print("NO")