def add_string(s):
    """
    Input: string like '33.1, 44.1, 69.69'

    Output: Sum of numbers.
    """
    # initialize accumulator
    accumulator = 0
    tmp = ""
    # break up string, using tmp var
    for i in s:
        ## build tmp
        if i == ',':
            accumulator = accumulator + float(tmp)
            tmp = ""
        else:
            tmp = tmp + i

    # adding tmp a final time to catch last number
    return accumulator + float(tmp)


def test_add_string():
    assert add_string("13.1, 62.4, 55.4") == 130.9
    assert add_string("12.1") == 12.1

    return "All tests passing."

print test_add_string()
