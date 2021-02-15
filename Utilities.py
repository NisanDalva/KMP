class Array(list):
    """
    make a list start from index 1 instead of 0
    >>> arr = Array([1, 2, 3])
    >>> arr[1]
    1
    >>> arr[2] = 7
    >>> arr
    Array([1, 7, 3])
    """
    def __init__(self, items: list) -> None:
        self.items = items

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.items})'

    def __len__(self) -> int:
        return len(self.items)

    def __getitem__(self, key: int) -> any:
        return self.items[key - 1]

    def __setitem__(self, key: int, value: any) -> None:
        self.items[key - 1] = value


class String(str):
    """
    make a simple string start from index 1 instead of 0
    >>> my_string = String('Some String')
    >>> my_string[1]
    S
    >>> my_string[4]
    e
    >>> my_string[len(my_string)]
    g
    """
    def __init__(self, string: str) -> None:
        self.string = string

    def __repr__(self) -> str:
        return self.string

    def __len__(self) -> int:
        return len(self.string)

    def __getitem__(self, key: int) -> str:
        return self.string[key - 1]
