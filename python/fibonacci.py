def get_fibonacci_series(**kwargs):
    series = []
    max_limit = 1000
    count_limit = 100
    max_num_series = int(kwargs.get('max_num', max_limit))
    max_num_series = max_num_series if 1 < max_num_series < max_limit else max_limit
    count_series = min(kwargs.get('max_count', count_limit), count_limit)
    count_series = count_series if 1 < count_series < count_limit else count_limit
    first_num = 0
    second_num = 1
    third_num = 0
    series.append(first_num)
    series.append(second_num)
    if count_series > 2:
        for index in range(2, count_series):
            third_num = first_num + second_num
            if third_num > max_num_series:
                break
            # end if
            series.append(third_num)
            first_num = second_num
            second_num = third_num
        # end for
    # end if
    return series


print(get_fibonacci_series(max_count=15, max_num=100))
