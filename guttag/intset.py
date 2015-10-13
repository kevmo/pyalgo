class IntSet(object):
    """An intSet is a set of integers""" # The abstraction
    # The implementation:
    # The value of the set is represented by a list of ints, self.vals.
    # Each int in the set occurs in self.vals exactly once.
    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, i):
        """Assumes i is an integer and inserts i into self.vals"""
        if i not in self.vals:
            self.vals.append(i)

        return self.vals

    def member(self, i):
        """If i is in self.vals, return True. Else, return false"""
        return i in self.vals

    def remove(self, i):
        """If i is in self.vals, raises ValueError if not"""
        try:
            self.vals.remove(i)
        except:
            raise ValueError(str(i) + ' not found')

    def getMembers(self):
        return self.vals[:] # copy, so you don't overwrite

    def __str__(self):
        self.vals.sort()
        result = ''
        for e in self.vals:
            result = result + str(e) + ','

        return '{' + result[:-1] + '}' # -1 omits trailing comma
