def isIn(s1, s2):
    """
    Input: 2 strings

    Output: True if one str occurs inside the other
    """
    result = False

    k
    def match_string(str1, str2):
        result = len(str1.split(str2)) > 1
        return result

    if match_string(s1, s2):
        result = True
    elif match_string(s2, s1):
        result = True

    return result


def test_isIn():
    assert isIn("moocow", "moo") == True
    assert isIn("moo", "moo") == True
    assert isIn("adslhfoaihf", "moo") == False
    assert isIn("bra", "abracadabra") == True
    assert isIn("182", "blink") == False

    print "All tests passing."


test_isIn()
