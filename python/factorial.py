import sys


def get_factorial(num):
    num = int(num)
    result = 1
    if num > 1:
        while num > 1:
            result *= num
            num -= 1
        # end while
        return result
    elif num == 1:
        return 1
    # end if
    return 0
# end function


def get_factorial_rec(num):
    num = int(num)
    if num > 1:
        return num * get_factorial_rec(num-1)
    elif num == 1:
        return 1
    # end if
    return 0
# end function


print(get_factorial_rec(sys.argv[1]))
print(get_factorial(sys.argv[1]))
