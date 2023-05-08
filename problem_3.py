def find_factors(n):
    d = 2
    while n > 1:
        while n % d == 0:
            n /= d
        d += 1
        if d*d > n:
            if n != 1:
                return int(n)
                break

print(find_factors(600851475143))