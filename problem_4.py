def larget_palindrome():
    max = 0
    for i in range(100,1000):
        for j in range(100,1000):
           max = i*j if (str(i*j) == str(i*j)[::-1] and i*j > max) else max
    return max

print(larget_palindrome())