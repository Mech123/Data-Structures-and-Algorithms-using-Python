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
    
    
def is_prime2(n: int, known_primes: list[int]) -> bool:
    """Check if a number is prime using previously computed primes up to sqrt(n)."""
    if n < 2:
        return False
    for p in known_primes:
        if p * p > n:
            break
        if n % p == 0:
            return False
    return True
    
    
def prime_twins(n: int) -> list[tuple[int, int]]:
    """Returns the first n prime twins."""
    resultprimes: list[tuple[int, int]] = []
    prime = 3
    while len(resultprimes) < n:
        nextprime = prime + 2
        if is_prime(prime) and is_prime(nextprime):
            resultprimes.append((prime, nextprime))
        prime += 2
    return resultprimes
    raise NotImplementedError()  # TODO: Add implementation


def prime_triplets(n: int) -> list[tuple[int, int, int]]:
    """Returns the first n prime triplets."""
    tripletsresult: list[tuple[int, int, int]] = []
    primes = [2, 3]
    p = 5
    while len(tripletsresult) < n:
        if is_prime2(p, primes):
            primes.append(p)
            
            if (p >= 5 and is_prime2(p + 2, primes) and is_prime2(p + 6, primes)):
                tripletsresult.append((p, p + 2, p + 6))
            elif (p >= 5 and is_prime2(p + 4, primes) and is_prime2(p + 6, primes)):
                tripletsresult.append((p, p + 4, p + 6))
        p += 2
    return tripletsresult
    raise NotImplementedError()  # TODO: Add implementation


if __name__ == "__main__":
    assert prime_twins(2) == [(3, 5), (5, 7)]
    print(prime_triplets(20))
    # TODO: Add more test cases
