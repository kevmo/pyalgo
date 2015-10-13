class intDict(object):
    """A dictionary with integer keys"""

    def __init__(self, numBuckets):
        """Create an array of arrays""""
        self.buckets = []
        self.numBuckets = numBuckets
        for i in range(numBuckets):
            self.buckets.append([])

    def addEntry(self, dictKey, dictVal):
        """Assumes dictKey is an int. Adds an entry"""
        hashBucket = self.buckets[dictKey % self.numBuckets]
        # replace if collision
        for i in range(len(hashBucket)):
            if hashBucket[i][0] = dictKey:
                hashBucket[i] = (dictKey, dictVal)
                return

        hashBucket.append((dictKey, dictVal))
