def find_prime(n):
    primes = [2]
    i = 2
    while len(primes) < n:
        is_prime = True
        for prime in primes:
            if i%prime == 0:
                is_prime = False
                continue
        if is_prime == True:
            primes.append(i)
        i += 1

    print(primes[-1])

find_prime(10001)