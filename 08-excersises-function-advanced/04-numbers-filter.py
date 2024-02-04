def even_odd_filter(**args):
    result = {}

    if "odd" in args:
        odd_list = args["odd"]
        result["odd"] = []
    else:
        odd_list = []

    if "even" in args:
        even_list = args["even"]
        result["even"] = []
    else:
        even_list = []

    for num in odd_list:
        if num % 2 != 0:
            result["odd"].append(num)

    for num in even_list:
        if num % 2 == 0:
            result["even"].append(num)

    return result

print(even_odd_filter(odd=[1, 2, 3, 4, 10, 5]))