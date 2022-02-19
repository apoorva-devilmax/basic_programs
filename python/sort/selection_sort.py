def custom_sort(lst):
    """
    Selection sort is like insertion sort except minimum el is picked
    instead of first el from unsorted sub-array. Here also we form two sub-array i.e.
    left-one is sorted and right-one is unsorted. Minimum el (starts from first el) is picked
    from unsorted sub-array and swap it from the current position in the sorted sub-array. In this way,
    sorted sub-array length increases while unsorted sub-array decreases till it becomes empty.
    So, it will sort from left-to-right manner.
    Time Complexity: O(n2)
    Space Complexity: O(1)
    :param lst: List to sort
    :return: Sorted List
    """
    n = len(lst)
    # start iteration
    for i in range(n-1):
        # set index of minimum value to i
        min_id = i
        # iterate to find minimum value from the rest of the value
        for j in range(i+1, n):
            if lst[min_id] > lst[j]:
                min_id = j
            # end if
        # end for
        # swap the current element with the minimum value (if not the same position)
        if min_id != i:
            lst[i], lst[min_id] = lst[min_id], lst[i]
        # end if
        print(f'Iteration #{i}:', sep=" ", end=" ")
        print(lst)
    # end for
    return lst
# end function


print(custom_sort([87, 200, 100, 150, 75, 99, 23, 65, 56, 77, 28, 67]))
