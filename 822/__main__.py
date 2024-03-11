from typing import List, Tuple

x = [(1, 3), (5, 8), (4, 10), (8, 12), (20, 25)]


def merge(input: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    result = []
    taken = []
    for index, item in enumerate(input):
        if index in taken:
            continue
        (current_min, current_max) = item
        for compare_index, compare in enumerate(input):
            # If comparing to the same value, skip
            if index == compare_index:
                continue
            (current_compare_min, current_compare_max) = compare
            # If no overlap, skip
            if current_compare_min > current_max:
                continue
            # If overlap, but current max isn't larger, skip
            if current_compare_max < current_max:
                continue
            current_max = current_compare_max
            if current_compare_min < current_min:
                current_min = current_compare_min
            taken.append(compare_index)
        result.append((current_min, current_max))
    return result


print(merge(x))
