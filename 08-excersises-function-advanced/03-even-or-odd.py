def even_odd(*args):
    even_nums = []
    odd_nums = []

    for num in args[:len(args) - 1]:
        if num % 2 == 0:
            even_nums.append(num)
        else:
            odd_nums.append(num)

    if args[len(args) - 1] == "even":
        return even_nums
    elif args[len(args) - 1] == "odd":
        return odd_nums
    
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))