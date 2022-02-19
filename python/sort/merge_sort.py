import os, sys


def process_merge(lst, l, mid, r):
    n1 = mid - l + 1
    n2 = r - mid
    # create temp arrays
    left_list = [0] * n1
    right_list = [0] * n2
    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        left_list[i] = lst[l + i]
    # end for
    for j in range(0, n2):
        right_list[j] = lst[mid + 1 + j]
    # end for
    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:
        if left_list[i] <= right_list[j]:
            lst[k] = left_list[i]
            i += 1
        else:
            lst[k] = right_list[j]
            j += 1
        # end if/else
        k += 1
    # end while
    while i < n1:
        lst[k] = left_list[i]
        k += 1
        i += 1
    # end while
    while j < n2:
        lst[k] = right_list[j]
        k += 1
        j += 1
    # end while
# end function


def merge_sort(lst, l, r, i=1):
    if l < r:
        mid = int((l+r)/2)
        # print(f'my mid: {mid}')
        merge_sort(lst, l, mid, i+1)
        merge_sort(lst, mid + 1, r, i+1)
        process_merge(lst, l, mid, r)
        print(f'Iteration #{i}:', sep=" ", end=" ")
        print(lst)
    # end if
    return lst
# end function


def custom_sort(lst):
    """
    Merge sort is also very fast and efficient sorting algorithm based on
    divide and conquer approach. In this, we pick the mid el and divide the array
    into two sub-array and then again do the same recursively to both the array.
    After this all the returned sorted arrays are merged in sorted manner.
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    :param lst: List to sort
    :return: Sorted List
    """
    n = len(lst)
    merge_sort(lst, 0, n-1)
    return lst
# end function


print(custom_sort([87, 200, 100, 150, 75, 99, 23, 65, 56, 77, 28, 67]))
