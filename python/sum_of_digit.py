import sys
from functools import reduce


def get_sum(num):
    result = 0
    num = int(num)
    if num > 0:
        result = int(reduce(lambda x, y: x+y, map(int, str(num))))
    # end if/else
    return result
# end function


print(get_sum(sys.argv[1]))
