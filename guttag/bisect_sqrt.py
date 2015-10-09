def bisect_sqrt(num, ans=None, lowest=0, highest=None):

    # guess the middle
    # if num too low guess middle of lowest and prev middle
    # if too high, guess higher
    epsilon = .05
    if not highest:
        highest = num
    if not ans:
        ans = (lowest + highest)/2.0

    # // might need more here
    if abs(num - ans**2) >= epsilon:
        if ans**2 > num:
            highest = ans
        else:
            lowest = ans

        answer = (highest + lowest)/2.0
        return bisect_sqrt(num, ans=answer, lowest=lowest, highest=highest)
    else:
        return ans


def test_bisect_sqrt():
    # print bisect_sqrt(1)
    print bisect_sqrt(4)
    print bisect_sqrt(9)
    print bisect_sqrt(16)
    print bisect_sqrt(25)
    print bisect_sqrt(48659865)

test_bisect_sqrt()
