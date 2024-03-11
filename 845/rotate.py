from typing import List


def rotate(input: List[int], k: int) -> List[int]:
    """
    Rotates the list by a specified count k
    """
    mod_k = k % len(input)
    return input[-mod_k:] + input[:-mod_k]


print(rotate([1, 2, 3, 4, 5, 6], 14))
# print(2 % 8)
