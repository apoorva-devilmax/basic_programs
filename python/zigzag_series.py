from functools import reduce
import os, sys


def get_zigzag_series(in_str, num_rows):
    if num_rows == 1:
        return in_str
    # end if
    l = len(in_str)
    arr = ["" for x in range(l)]
    down = True
    row = 0
    for i in range(l):
        arr[row] += in_str[i]
        if row == num_rows - 1:
            down = False
        elif row == 0:
            down = True
        # end if
        if down:
            row += 1
        else:
            row -= 1
        # end if
    out_str = reduce(lambda x, y: x+y, arr)
    return out_str
# end function


print(get_zigzag_series("PAYPALISHIRING", 4))
