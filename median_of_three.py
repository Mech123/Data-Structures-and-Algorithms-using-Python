def median(a: int, b: int, c: int) -> int:
    return sorted([a, b, c])[1]
    raise NotImplementedError()  # TODO: Add implementation
    
    
def median2(a: int, b: int, c: int) -> int:
    if (a <= b <= c) or (c <= b <= a):
        return b
    elif (b <= a <= c) or (c <= a <= b):
        return a
    else:
        return c
    raise NotImplementedError()  # TODO: Add implementation


if __name__ == "__main__":
    print(median(0, 0, 0))
    print(median(11, 25, 2))
    print(median(1, 53, 2))
    print(median(9, 3, 23))
    print(median2(10, 3, 23))
    print(median2(9, 89, 1))
    print(median2(11, 3, 1000))
    print(median2(345, 67, 23))
