def my_func(user_input, current):
    epsilon = 0.001
    print("x0 = {}".format(current))
    counter = 1
    while True:
        next_iteration = (current + (user_input / current)) / 2
        print("x{} = {}".format(counter, next_iteration))
        counter = counter + 1
        error_check = abs(next_iteration - current)
        current = next_iteration
        if error_check < epsilon:
            return
