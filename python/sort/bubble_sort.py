def custom_sort(lst):
    """
    Bubble sort is the most basic sorting technique where
    two adjacent (like bubbles) el (starts from first el) is compared and swapped only if
    left el is greater than right el. In this way, the max el will be shifted
    into the last position (right-most) after the first pass. After second pass,
    second max el will be available at second-last position and so on. So it will sort
    from right-to-left manner.
    Time Complexity: O(n2)
    Space Complexity: O(1)
    :param lst: List to sort
    :return: Sorted List
    """
    n = len(lst)
    for i in range(n-1):
        # last i elements are sorted already because after one iteration of swapping
        # max element will be shifted to rightmost position
        swapped = False
        for j in range(n-i-1):
            if lst[j] > lst[j+1]:
                swapped = True
                lst[j], lst[j+1] = lst[j+1], lst[j]
            # end if
        # end for
        print(f'Iteration #{i}:', sep=" ", end=" ")
        print(lst)
        # it is an improvement: if no el is swapped, then no need to check further
        if swapped is False:
            break
        # end if
    # end for
    return lst
# end function


print(custom_sort([87, 200, 100, 150, 75, 99, 23, 65, 56, 77, 28, 67]))
