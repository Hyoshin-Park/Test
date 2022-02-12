def factorial(n):
    num = 1

    if n > 0:
        num = n * factorial(n - 1)
    return num

n = int(input())
print(factorial(n))
