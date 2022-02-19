def custom_sort(lst):
    """
    Insertion sort is an improvement over bubble sort where
    we form two sub-array i.e. left-one is sorted and right-one is unsorted.
    An el (starts from second el because first single el is always sorted) is picked (first)
    from unsorted sub-array and inserted at its correct position in the sorted sub-array. In this way,
    sorted sub-array length increases while unsorted sub-array decreases till it becomes empty.
    So, it will sort from left-to-right manner.
    Time Complexity: O(n2)
    Space Complexity: O(1)
    :param lst: List to sort
    :return: Sorted List
    """
    n = len(lst)
    # outer loop will start from 1 because a single element is always sorted
    for i in range(1, n):
        # store the current element in a tmp var to insert it later at correct position in sorted sub-array
        tmp = lst[i]
        # inner loop will starts from the prev el of current el up to the 1st el (sorted sub-array)
        j = i-1
        while j >= 0 and lst[j] > tmp:
            # if el is greater than tmp el, then perform right shift
            lst[j + 1] = lst[j]
            j -= 1
        # end while
        # if el is not greater than tmp el, this will be the position to insert
        lst[j+1] = tmp
        print(f'Iteration #{i}:', sep=" ", end=" ")
        print(lst)
    # end for
    return lst
# end function


print(custom_sort([87, 200, 100, 150, 75, 99, 23, 65, 56, 77, 28, 67]))
