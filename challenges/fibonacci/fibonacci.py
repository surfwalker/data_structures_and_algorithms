def fib_finder(k):
    if k < 2:
        return k

    return fib_finder(k - 1) + fib_finder(k - 2)