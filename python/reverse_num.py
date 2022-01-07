import sys


def get_reverse(num):
    result = 0
    num = int(num)
    if num > 0:
        result = int(str(num)[::-1])
    # end if/else
    return result
# end function


print(get_reverse(sys.argv[1]))
