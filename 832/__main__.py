from typing import List


def find_longest_subarray(input: List[int]) -> int:
    unique_numbers = []
    current_length = 0
    longest = 0
    for number in input:
        if number not in unique_numbers:
            unique_numbers.append(number)
            current_length += 1
            if current_length > longest:
                longest = current_length
        else:
            unique_numbers = [number]
            current_length = 1
        print(f'unique_numbers: {unique_numbers}')
        print(f'current_length: {current_length}')
        print(f'longest: {longest}')
    return longest


print(find_longest_subarray([5, 1, 3, 5, 2, 3, 4, 1]))
