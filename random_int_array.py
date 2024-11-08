import random


def create_random(n: int) -> list[int]:
    """Creates an array with `n` random integers in the range `[5, 99]`"""
    # if n>95:
    #    raise ValueError("n should be 99 or less to maintain unique numbers in the range[5,99]")
    return [random.randint(5, 99) for n in range(n)]
    raise NotImplementedError()  # TODO: Add implementation


def to_string(a: list[int]) -> str:
    """Creates a string from an array."""
    string = "["
    for i, number in enumerate(a):
        string += str(number)
        if i < len(a) - 1:
            string += ", "
    string += "]"
    return string
    raise NotImplementedError()  # TODO: Add implementation


def pos_min(a: list[int]) -> int:
    """
    Returns the position of the smallest element in `a`. If it is not unique, it
    returns the position of the first one.
    """
    # if not a:
    #    raise ValueError("The list is empty")
    min_index = 0
    for i in range(1, len(a)):
        if a[i] < a[min_index]:
            min_index = i
    return min_index    
    raise NotImplementedError()  # TODO: Add implementation


def swap(a: list[int]) -> None:
    """Swaps the first and last element in `a`."""
    if len(a) > 1:
        temp = a[0]
        a[0] = a[-1]
        a[-1] = temp
    # raise NotImplementedError()  # TODO: Add implementation


if __name__ == "__main__":
    pass
