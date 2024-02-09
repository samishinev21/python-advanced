import os
try:
    os.remove('my_fist_file.txt')
except FileNotFoundError:
    print("File already deleted!")