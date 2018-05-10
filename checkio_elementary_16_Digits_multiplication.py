"""\
    Digits Multiplication

    You are given a positive integer. Your function should calculate the product
    of the digits excluding any zeroes.

    For example: The number given is 123405. The result will be 1*2*3*4*5=120
    (don't forget to exclude zeroes).

    Input: A positive integer.

    Output: The product of the digits as an integer.

    Example:
     checkio(123405) == 120
     checkio(999) == 729
     checkio(1000) == 1
     checkio(1111) == 1

    How it is used: This task can teach you how to solve a problem with simple
    data type conversion.

    Precondition:
     0 < number < 10^6
"""
def checkio(number: int) -> int:
    numberlist = list(str(number))
    product = 1
    for i in numberlist:
        if int(i) != 0:
            product = product * int(i)
    return product

print(checkio(123405))
print(checkio(999))
print(checkio(1000))
print(checkio(1111))

# szép, könnyen olvasható