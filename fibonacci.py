def fibonacci(length):
    length = round(length)
    # if length < 0:
    #     return "Please input a positive whole number"
    iterations = 0
    n1 = 0
    n2 = 1
    fibo_list = []
    while iterations < length:
        fibo_list.append(n1)
        n_total = n1 + n2
        n1 = n2
        n2 = n_total
        iterations += 1
    return fibo_list, sum(fibo_list)


# Index of 0 to get the list of fibonacci numbers
# Index of 1 to get the sum of the list
print(fibonacci(4.8)[0])
