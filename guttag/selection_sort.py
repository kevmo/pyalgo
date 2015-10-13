def selSort(L):
    """Assumes that L is a list of elements
    that can be compared using >.
    Sorts L in ascending order."""

    suffixStart = 0

    while suffixStart != len(L):
        # look at each element in suffix
        for i in range(suffixStart, len(L)):
            if L[i] < L[suffixStart]:
                # swap
                L[suffixStart], L[i] = L[i], L[suffixStart]

        suffixStart += 1

    return L

def test_selSort():
    assert selSort([5, 42, 9, 1, 69, 2, 14, 1]) == [1, 1, 2, 5, 9, 14, 42, 69]

    print "All test passing"

test_selSort()
