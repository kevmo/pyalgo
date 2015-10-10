# find the Nth fibonacci number

def fibonacci(n):
    if n < 1:
        raise

    if n <= 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def test_fibonacci():
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8

    print "All fibonacci tests passing."

    return 1


test_fibonacci()
