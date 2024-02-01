def operate(*args):
    def addition(nums):
        result = 0
        for num in nums:
            result += num
        return result
    
    def substraction(nums):
        result = nums[0]
        for i in range(1, len(nums)):
            result -= nums[i]
        return result

    def multiplication(nums):
        result = 1
        for num in nums:
            result *= num
        return result
    
    def devision(nums):
        result = nums[0]
        for i in range(1, len(nums)):
            result /= nums[i]
        return result
    
    operator = args[0]

    if operator == "+":
        return addition(args[1:])
    elif operator == "-":
        return substraction(args[1:])
    elif operator == "*":
        return multiplication(args[1:])
    elif operator == "/":
        return devision(args[1:])
    
print(int(operate("/", 10, 5, 2)))