def is_prime(n: int) -> bool:
    """Returns `True`, if and only if `n` is prime."""
    if n <= 1:
        
        return False
    if n == 2:
        
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
    raise NotImplementedError()
    
    
def next_prime(n: int) -> int:
    """Returns the next prime number that is bigger or equal to `n`."""
    if n <= 1:
        return 2
    prime = n
    while not is_prime(prime):
        prime += 1
    return prime
    raise NotImplementedError()
    
    
def main():
    
    print(is_prime(2))
    print(is_prime(20))
    print(is_prime(23))
    print(is_prime(47))
    print(next_prime(4))
    print(next_prime(23))
    print(next_prime(50000))


if __name__ == "__main__":
    main()