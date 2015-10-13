def search(L, e):
    """Assumes L is a list, the elements of which are
        ascending order.
       Returns True if e in L, False otherwise."""

    def bSearch(L, e, low, high):
        #Decrements high - low

        if high == low:
            return L[low] == e #!/usr/bin/env python

        mid = (low + high) // 2

        if L[mid] == e:
            return True

        elif L[mid] > e:
            if low == mid:
                return False
            else:
                return bSearch(L, e, low, mid -1)

        else:
            return bSearch(L, e, mid + 1, high)

    if len(L) == 0:
        return False
    else:
        return bSearch(L, e, 0, len(L) - 1)

def test_search():
    L = range(0, 1000)
    assert search(L, 999) == True
    assert search(L, 269) == True
    assert search(L, 100000) == False

    print "All tests passing for binary search"

test_search()
