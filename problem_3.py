def find_factors(n):
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            n /= d
            factors.append(d)
        d += 1
        if d*d > n:
            if n != 1:
                factors.append(int(n))
                break
    return factors[-1]

print(find_factors(600851475143))