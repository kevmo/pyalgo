import datetime

class Person(object):

    def __init__(self, name):
        """Create a person"""
        self.name = name
        self.birthday = None

        try:
            lastBlank = name.rindex(' ')
            self.lastName = name[lastBlank + 1:]
        except:
            self.lastName = name

    def getName(self):
        """Return's full name"""
        return self.name

    def getLastName(self):
        return self.lastName

    def setBirthday(self, bday):
        """Assumed birthdte is of type datetime.datetime
        Sets self's birthday to birthdate"""
        self.birthday = bday

    def getAge(self):
        """Returns age in days"""
        if self.birthday == None:
            raise ValueError("Ain't no birthday here!")
        return (datetime.date.today() - self.birthday).days

    def __lt__(self, other):
        """Returns True if self's name is lexicographically
        less than the other's name, and False otherwise"""
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

    def __str__(self):
        return self.name
