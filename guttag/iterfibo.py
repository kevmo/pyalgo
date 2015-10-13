def inter_fibo(n):
    """Find the nth fibonacci number."""
    if n <=2:
        return 1

    fib = [1, 1]

    while len(fib) <= n:
        fib.append(fib[-1]) + fib[-2])

    return fib.pop()
