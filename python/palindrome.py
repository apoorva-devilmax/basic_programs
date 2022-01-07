def check_palindrome(num):
    is_palindrome = False
    num = int(num)
    if num > 0:
        if str(num)[::-1] == str(num):
            is_palindrome = True
        # end if
    elif num == 0:
        is_palindrome = True
    # end if/else
    return is_palindrome
# end function


def get_palindrome_num(max_count=10):
    series = []
    max_count = max_count if 1 < max_count <= 100 else 10
    index_count = 0
    start_num = 0
    while index_count < max_count:
        if check_palindrome(start_num):
            series.append(start_num)
            index_count += 1
        # end if
        start_num += 1
    # end for
    return series
# end function


print(get_palindrome_num(30))
