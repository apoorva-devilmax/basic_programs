def process_partition(lst, l, h):
    pivot_pos = l
    pivot = lst[pivot_pos]
    i = l
    j = h
    while i < j:
        while lst[i] <= pivot and i <= h-1:
            i += 1
        # end while
        while lst[j] > pivot and j >= l:
            j -= 1
        # end while
        if i < j:
            lst[i], lst[j] = lst[j], lst[i]
        # end if
    # end while
    lst[j], lst[pivot_pos] = lst[pivot_pos], lst[j]
    return j
# end function


def quick_sort(lst, l, h, i=1):
    if l < h:
        pivot = process_partition(lst, l, h)
        print(f'Iteration #{i}:', sep=" ", end=" ")
        print(lst)
        quick_sort(lst, l, pivot - 1, i+1)
        quick_sort(lst, pivot + 1, h, i+1)
    # end if
    return lst
# end function


def custom_sort(lst):
    """
    Quick sort is very efficient sorting algorithm where we pick an el (first|mid|random),
    say Pivot, and compare all the el with this Pivot value. The el greater than this, will
    move to the left side and smaller el will move to the right side. Now, the array can
    be divided into two parts (partitioning) using the Pivot el. Both the parts will again
    be sorted using the earlier approach recursively.
    Real-World Example: Assembly Line of school days where students have to be in line
    according to their heights.
    Time Complexity: O(n2)|O(n log n)
    Space Complexity: O(n)
    :param lst: List to sort
    :return: Sorted List
    """
    n = len(lst)
    quick_sort(lst, 0, n-1)
    return lst
# end function


print(custom_sort([87, 200, 100, 150, 75, 99, 23, 65, 56, 77, 28, 67]))
