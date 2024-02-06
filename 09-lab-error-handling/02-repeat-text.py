word = input()

try:
    number = int(input())
    print(word * number)
except ValueError:
    print("Variable times must be an integer")