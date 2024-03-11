import copy
from typing import List


def substr_in_available_words(current_word: str, available_words: List[str]) -> int:
    """
    Returns the index of the matching word when it is a substring of current_word.
    For example, if current_word is 'defabc' and available_words is ['abc', 'ghi'], then
    the return value would be 3. If current_word is 'defabc' and available_words is ['ghi'], then
    the return value would be -1.
    """
    for word in available_words:
        try:
            match_index = current_word.index(word)
            return match_index
        except ValueError:
            continue
    return -1


# print(substr_in_available_words('defabc', ['abc']))


def find_words(s: str, words: List[str]) -> List[int]:
    word_indices = []
    available_words = copy.copy(words)
    # print(f'available_words: {available_words}')
    current_word = ''
    current_word_index = 0
    for index, char in enumerate(s):
        current_word += char
        # print(f'current_word: {current_word}')
        match_index = substr_in_available_words(current_word, available_words)
        if match_index >= 0:
            matching_word = current_word[match_index:]
            available_words.remove(matching_word)
            current_word = ''
            if len(available_words) == 0:
                word_indices.append(current_word_index + match_index)
                current_word_index = index + 1
                available_words = copy.copy(words)
        if current_word in words and current_word not in available_words:
            current_word_index = copy.copy(index)
            available_words = copy.copy(words)
            available_words.remove(current_word)
        # print(f'available_words: {available_words}')
    return word_indices


result = find_words('dogcatcatcodecatdog', ['cat', 'dog'])
print(f'result: {result}')
result2 = find_words('barfoobazbitbyte', ['dog', 'cat'])
print(f'result2: {result2}')
