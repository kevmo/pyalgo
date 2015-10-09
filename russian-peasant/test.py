import time

from src import russian_multiply, bit_russian

def test_russian_multiply():
    start_time = time.time()
    assert russian_multiply(6, 12) == 72
    assert russian_multiply(120, 10) == 1200
    assert russian_multiply(9, 5) == 45
    assert russian_multiply(0, 222) == 0
    assert russian_multiply(99, 2) == 198
    end_time = time.time()

    return "All tests passing in {} secs for russian_multiply".format(end_time - start_time)

def test_bit_russian():
    start = time.time()
    assert bit_russian(12, 6) == 72
    assert bit_russian(10, 120) == 1200
    assert bit_russian(0, 5) == 0
    assert bit_russian(99, 1) == 99
    assert bit_russian(5, 5) == 25
    end = time.time()

    return "All tests passing in {} secs for bit_russian".format(end - start)

print test_russian_multiply()
print test_bit_russian()
