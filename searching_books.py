def search_linear(a: list[str], item: str) -> int | None:
    """Searches the list for item linearly. Returns the position of item."""
    for number, book in enumerate(a):
        if book == item:
            return number
    return None
    raise NotImplementedError()  # TODO: Add implementation


def search_binary(a: list[str], item: str) -> int | None:
    """Searches the list for item binary. Returns the position of item."""
    low, high = 0, len(a) - 1
    while low <= high:
        midvalue = (low + high) // 2
        if a[midvalue] == item:
            return midvalue
        elif a[midvalue] < item:
            low = midvalue + 1
        else:
            high = midvalue - 1
    return None
    raise NotImplementedError()  # TODO: Add implementation


def search_linear_cmp_count(a: list[str], item: str) -> int:
    """Searches the list for item linearly. Returns the number of comparisions needed."""
    comparisons = 0
    for number, book in enumerate(a):
        comparisons += 1
        if book == item:
            return comparisons
    return comparisons 
    raise NotImplementedError()  # TODO: Add implementation


def search_binary_cmp_count(a: list[str], item: str) -> int:
    """Searches the list for item linearly. Returns the number of comparisions needed."""
    low, high = 0, len(a) - 1
    comparisons = 0
    while low <= high:
        midvalue = (low + high) // 2
        comparisons += 1
        if a[midvalue] == item:
            return comparisons
        elif a[midvalue] < item:
            low = midvalue + 1
        else:
            high = midvalue - 1
    return comparisons    
    raise NotImplementedError()  # TODO: Add implementation


if __name__ == "__main__":
    a = ["Design Patterns", "The Pragmatic Programmer", "The mythical man-month", "Clean Code"]
    b = ["The Pragmatic Programmer", "The mythical man-month", "Clean Code", "Design Patterns", "Machine Leanring"]
    b = sorted(b)
    print(f"Linear search for Clean Code: {search_linear_cmp_count(a, 'Clean Code')} comparisons")
    print(f"Binary search for Clean Code: {search_binary_cmp_count(a, 'Clean Code')} comparisons")
    print(f"Linear search for Clean Code: {search_linear_cmp_count(b, 'Clean Code')} comparisons")
    print(f"Binary search for Clean Code: {search_binary_cmp_count(b, 'Clean Code')} comparisons")
