def compare(nums):
    negatives = []
    positives = []

    for num in nums:
        if num < 0:
            negatives.append(num)
        else:
            positives.append(num)

    print(sum(negatives))
    print(sum(positives))
            
    if abs(sum(negatives)) > sum(positives):
        print("The negatives are stronger than the positives")
    else:
        print("The positives are stronger than the negatives")

nums = list(map(int, input().split(" ")))

compare(nums)