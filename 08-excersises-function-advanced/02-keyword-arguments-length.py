dictionary = {'name': 'Peter', 'age': 25}

def kwargs_length(**args):
    return len(args)

print(kwargs_length(dictionary))