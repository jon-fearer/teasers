from typing import List, Tuple, Union

x = [-9, -2, 0, 2, 3]


def square_sort(input: List[int]) -> List[int]:
    squared = []
    for item in input:
        squared.append(item**2)
    squared.sort()
    return squared


print(square_sort(x))
