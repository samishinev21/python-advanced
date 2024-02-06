class ValueCannotBeNegative(Exception):
    """value_cannot_be_negative"""
    pass

for i in range(5):
    try:
        number = int(input())
        if number < 0:
            raise ValueCannotBeNegative
    except ValueCannotBeNegative as error:
        print(error)
