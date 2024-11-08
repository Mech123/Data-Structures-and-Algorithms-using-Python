def interleave(a: list[int], b: list[int]) -> list[int]:
    """
    Returns a new array with elements consecutively taken from array `a` and
    `b`.
    """
    interleaved = []
    for i in range(len(a)):
        interleaved.append(a[i])
        interleaved.append(b[i])
    return interleaved
    raise NotImplementedError()  


def perfect_shuffle(a: list[int]) -> list[int]:
    """Returns a new array that is perfectly shuffled once."""
    # if len(a) % 2 != =:
    #   raise ValueError("The input array must have an even number of elements")
    midvalue = len(a) // 2
    first_half = a[:midvalue]
    second_half = a[midvalue:]
    shuffled_deck = interleave(first_half, second_half)
    return shuffled_deck
    raise NotImplementedError()  


def shuffle_number(a: int) -> int:
    """Returns the number of perfect shuffles needed to get to the same array."""
    original_deck = list(range(a))
    shuffled_deck = perfect_shuffle(original_deck)
    shuffle_count = 1
    
    while shuffled_deck != original_deck:
        shuffled_deck = perfect_shuffle(shuffled_deck)
        shuffle_count += 1
    return shuffle_count
    raise NotImplementedError() 


if __name__ == "__main__":
    pass
