"""
https://www.geeksforgeeks.org/array-rotation/
"""
from typing import List


def array_rotate(array: List[int], rotation_size: int) -> List[int]:
    tmp_arr = array[:rotation_size]
    n = len(array)
    diff = n - rotation_size
    for index in range(n):
        if index < diff:
            array[index] = array[index + rotation_size]
        else:
            array[index] = tmp_arr[index - diff]
        # if/else
    # for
    return array
# def


print("input===", [1, 2, 3, 4, 5, 6, 7])
print(array_rotate([1, 2, 3, 4, 5, 6, 7], 4))
