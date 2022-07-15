def factorial(n):
    try:
        if n < 0:
            return "n must be greater or equal to 0"
        if n == 0:
            return 1
        if n == 1:
            return n
        return n * factorial(n-1)
    except TypeError:
        return "n must be whole number"

print(factorial(20))
