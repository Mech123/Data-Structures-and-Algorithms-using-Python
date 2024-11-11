"""
Solution for part 2.
# TODO
In Tree recursion, each call to the function may lead to 
multiple additional calls.
this creates a branching structure similar to a tree.
for Fibonacci, fin1(n) calls fib1(n-1) and fib1(n-2) 
and each of these calls further branches out. 
This can lead to an exponential increase in function calls.
"""
number_recursive_calls = 0
number_loop_iterations = 0


def fib1(n: int) -> int:
    """Calculates the `n`th fibonacci number recursively."""
    global number_recursive_calls
    number_recursive_calls += 1
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fib1(n - 1) + fib1(n - 2)
    raise NotImplementedError()  # TODO: Add implementation


def fib2(n: int) -> int:
    """Calculates the `n`th fibonacci number iteratively."""
    global number_loop_iterations
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        fib_number_1 = 0
        fib_number_2 = 1
        for i in range(1, n + 1):
            fib_n = fib_number_1 + fib_number_2
            fib_number_1 = fib_number_2
            fib_number_2 = fib_n
            number_loop_iterations += 1
        return fib_number_2
    raise NotImplementedError()  # TODO: Add implementation


if __name__ == "__main__":
    for i in range(1, 16):
        print(f"fibonaci number {i}: {fib1(i)}")
    for i in range(1, 6):
        print(f"fibonaci number {i}: {fib2(i)}") 

    print(f"Number of function call for fib1(15) {number_recursive_calls}")
        
    print(f"Number of function call for fib1(5) {number_loop_iterations}")
    fib1_result_23 = fib1(23)
    fib2_result_23 = fib2(23)
    print(fib1_result_23)
    print(fib2_result_23)
    print(f"Number of function calls for fib1(23) {number_recursive_calls}")
    print(f"Number of function calls for fib2(23) {number_loop_iterations}")    