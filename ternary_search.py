from typing import List
from random import randint
import time


def binary_search(a: List[int], item: int) -> int | None:
    """Searches the list for item with binary search. Returns the position of item."""
    return binary_search_helper(a, item, 0, len(a) - 1)
    raise NotImplementedError()  # TODO: Add implementation


def binary_search_helper(a: List[int], item: int, low: int, high: int) -> int | None:
    if low > high:
        return None
    mid = (low + high) // 2
    
    if a[mid] == item:
        return mid
    elif a[mid] < item:
        return binary_search_helper(a, item, mid + 1, high)
    else:
        return binary_search_helper(a, item, low, mid - 1)
    raise NotImplementedError()  # TODO: Add implementation


def ternary_search_helper(a: List[int], item: int, low: int, high: int) -> int | None:
    
    split1 = low + (high - low) // 3
    split2 = high - (high - low) // 3
    
    if low > high:
        return None
    if a[split1] == item:
        return split1
    if a[split2] == item:
        return split2
    if item < a[split1]:
        return ternary_search_helper(a, item, low, split1 - 1)
    elif item > a[split2]:
        return ternary_search_helper(a, item, split2 + 1, high)
    else:
        return ternary_search_helper(a, item, split1 + 1, split2 - 1)    
    raise NotImplementedError()  # TODO: Add implementation
    
    
def ternary_search(a: List[int], item: int) -> int | None:
    """Searches the list for item with ternary search. Returns the position of item."""
    return ternary_search_helper(a, item, 0, len(a) - 1)
    raise NotImplementedError()  # TODO: Add implementation


def time_binary_search_in_s(arr: List[int], item: int) -> float:
    start = time.time()
    binary_search(arr, item)
    return time.time() - start


def time_ternary_search_in_s(arr: List[int], item: int) -> float:
    start = time.time()
    ternary_search(arr, item)
    return time.time() - start


if __name__ == "__main__":
    # TODO: Test your binary and ternary search implementation here...
    a = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    print("Ternary search results:")
    print(f"Searching for 7: Found at index {binary_search(a, 7)}")
    print(f"Searching for 15: Found at index {ternary_search(a, 15)}")
    print(f"Searching for 4 (not in list): {binary_search(a, 4)}")
    # These constants should be defined here, don't move them!
    MAX_VALUE = 50_000_000
    NUM_ITER = 100_000
    SEARCH_VALUES = [randint(0, MAX_VALUE - 1) for _ in range(NUM_ITER)]
    ARRAY = list(range(MAX_VALUE))
    print(f"Searching {NUM_ITER:_} random values in an array of size {MAX_VALUE:_}")

    time_binary = 0.
    for value in SEARCH_VALUES:
        time_binary += time_binary_search_in_s(ARRAY, value)

    time_ternary = 0.
    for value in SEARCH_VALUES:
        time_ternary += time_ternary_search_in_s(ARRAY, value)

    print(f"Total binary search time:    {time_binary:.9f} s")
    print(f"Total ternary search time:   {time_ternary:.9f} s")
    print(f"Average binary search time:  {time_binary / NUM_ITER:.9f} s")
    print(f"Average ternary search time: {time_ternary / NUM_ITER:.9f} s")


"""
TODO: Task 3, compare the algorithms
Binary Search:
 time complexity : O(log2(N)) where N is number of elements
 Mechanism: it divides the search range by half with each step.
 making it logarithmic in performanc.
 Ternary Search:
 time complexity: O(log3(N))
 Mechanism: 
 Ternary search divides the range into three parts using two middle points.
 it can reduce the search space faster in theory. but it also requires more comparsions per iteration.
 
"""