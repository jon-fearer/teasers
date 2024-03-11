from typing import Union


class SmartDictionary:
    __min = None
    __min_key = None
    __max = None
    __max_key = None
    __store = {}

    def __init__(self) -> None:
        self.__min = None

    def plus(self, key: Union[int, str]) -> None:
        new_value = self.__store.get(key, 0) + 1
        self.__store[key] = new_value
        if self.__max is None or new_value > self.__max:
            self.__max = new_value
            self.__max_key = key
        if self.__min is None:
            self.__min = new_value
            self.__min_key = key

    def minus(self, key: Union[int, str]) -> None:
        value = self.__store.get(key, 0)
        if value == 0:
            return
        if value == 1:
            del self.__store[key]
            return
        self.__store[key] = value - 1

    def get_max(self) -> int:
        return self.__max

    def get_min(self) -> int:
        return self.__min


smart_dictionary = SmartDictionary()
print(smart_dictionary.get_max())
print(smart_dictionary.get_min())
smart_dictionary.plus('a')
smart_dictionary.plus('a')
print(smart_dictionary.get_max())
print(smart_dictionary.get_min())
