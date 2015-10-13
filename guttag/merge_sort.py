def merge(left, right, compare):
    """Assumes left and right are sorted lists and
     compare defines an ordering on the elements.

     Returns a new sorted (by compare) list, containing
     the same elements as (left + right) would contain."""

    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):

        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j +=1
    while (i < len(left)):
        result.append(left[i])

    while (j < len(right)):
        result.append(right[j])

    return result


import operator

def mergeSort(L, compare=operator.lt):
    """Assumed L is a list, compare defines
    an order on elements of L."""

    if len(L) < 2:
        return L[:]

    else:
        middle = len(L) //2
        left = mergeSort(L[:middle], compare)
        right = mergeSort(L[middle:], compare)

        return merge(left, right, compare)


def lastNameFirstName(name1, name2):
    import string
    name1 = string.split(name1, " ")
    name2 = string.split(name2, " ")

    if name1[1] != name2[1]:
        return name1[1] < name2[1]

    else:
        return name1[0] < name2[0]

def firstNameLastName(name1, name2):
    import string
    name1 = string.split(name1, " ")
    name2 = string.split(name2, " ")

    if name1[0] != name2[0]:
        return name1[0] < name2[0]

    else:
        return name1[1] < name2[1]

L = ["Christ Almighty", "Asshat Trump", "Tom Brady", "Kevin Moore"]

print "Sorted by last name:", mergeSort(L, lastNameFirstName)
print "Sorted by first name:", mergeSort(L, firstNameLastName)
