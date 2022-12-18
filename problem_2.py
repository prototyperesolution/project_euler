def solution():
    fibonacci = [0,1]
    total = 0
    curr = 0
    while curr < 4000000:
        new = sum(fibonacci)
        curr = new
        fibonacci.pop(0)
        fibonacci.append(new)
        if new%2 == 0:
            total += new

    return total

print(solution())