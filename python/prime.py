def check_prime(num):
    is_prime = True
    if 2 < num < 1000:
        for i in range(2, (int(num/2)+1)):
            if num % i == 0:
                is_prime = False
                break
            # end if
        # end for
        return is_prime
    elif num == 2:
        return is_prime
    # end if/else
    return False
# end function


def get_prime_num(max_count=10):
    series = []
    max_count = max_count if 1 < max_count <= 100 else 10
    index_count = 0
    start_num = 2
    while index_count < max_count:
        if check_prime(start_num):
            series.append(start_num)
            index_count += 1
        # end if
        start_num += 1
    # end for
    return series
# end function


print(get_prime_num())
