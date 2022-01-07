from functools import reduce


def check_armstrong(num):
    is_armstrong = False
    num = int(num)
    if num > 0:
        cube_sum = int(reduce(lambda x, y: x+y, map(lambda x: int(x)**3, str(num))))
        if cube_sum == num:
            is_armstrong = True
        # end if
    elif num == 0:
        is_armstrong = True
    # end if/else
    return is_armstrong
# end function


def get_armstrong_num(max_count=10):
    series = []
    max_count = max_count if 1 < max_count <= 100 else 10
    index_count = 0
    start_num = 0
    while index_count < max_count:
        if check_armstrong(start_num):
            series.append(start_num)
            index_count += 1
        # end if
        start_num += 1
    # end for
    return series
# end function


print(get_armstrong_num(6))
