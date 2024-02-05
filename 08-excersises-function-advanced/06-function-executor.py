def sum_numbers(num1, num2):
    return num1 + num2

def multiply_numbers(num1, num2):
    return num1 * num2

def func_executor(*args):
    results = {}
    for function_name, params in args:
        results[function_name] = function_name(*params) # sum_numbers(1, 2)

    buffer = ""

    for function_name, result in results.items():
        buffer += f"{function_name.__name__} - {result}\n"
   
    return buffer


def make_upper(*strings):
    result = tuple(s.upper() for s in strings)
    return result

def make_lower(*strings):
    result = tuple(s.lower() for s in strings)
    return result

# print(func_executor(
#     (make_upper, ("Python", "softUni")),
#     (make_lower, ("PyThOn",))))

print(func_executor((lambda a, b: a * b, (2, 4))))

my_list = {"camember": 5, "blue cheese": 10, "bulgarian cheese": 2}

print(sorted(my_list.items(), key=lambda item: (item[1])))
