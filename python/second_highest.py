def get_second_highest(lst):
    f_highest = 0
    s_highest = 0
    for el in lst:
        if el > f_highest:
            s_highest = f_highest
            f_highest = el
        elif s_highest < el < f_highest:
            s_highest = el
        # end if/else
    # end for
    return {'first_highest': f_highest, 'second_highest': s_highest}
# end function


print(get_second_highest([87, 200, 100, 150, 75, 99, 23, 65, 56, 77, 28, 67]))
