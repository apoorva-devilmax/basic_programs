"""
https://www.geeksforgeeks.org/leaders-in-an-array/
"""
from typing import List


def leader_array(array: List[int]) -> List[int]:
    n = len(array)
    leader_el = array[n-1]
    leader = [leader_el]
    for i in range(n-2, -1, -1):
        if array[i] > leader_el:
            leader_el = array[i]
            leader = [leader_el] + leader  # if same order needed
            # leader.append(leader_el)  # if order does not matter
        # if
    # for
    return leader
# def


print("input===", [16, 17, 4, 3, 5, 2])
print(leader_array([16, 17, 4, 3, 5, 2]))
