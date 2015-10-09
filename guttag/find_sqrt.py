def find_sqrt(num):
    epsilon = .01
    ans = 1.0
    step = epsilon**2

    while abs(num - ans**2) >= epsilon and ans <= num:
        ans = ans + step

    return ans


def test_find_sqrt():
    print find_sqrt(4)
    print find_sqrt(9)
    print find_sqrt(16)
    print find_sqrt(25)


test_find_sqrt()
