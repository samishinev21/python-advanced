try:
    open("C:\\Projects\\python-advanced\\10-lab-file-handling\\text.txt")
    print("File found")
except FileNotFoundError:
    print("File not found")