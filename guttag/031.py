# INSTRUCTIONS
# input: integer
# output: root and power such that 0 < pwr < 6 and
# root**pwr = integer

from sys import argv


user_number = int(argv[1])

def find_root_and_power(num):
    """
    Input: num

    Returns a root, power such that power is 2 and 5,
    inclusive, and root**power = num.
    """
    root = 0
    for pwr in range(2, 6):

        while root**pwr < num:
            root += 1

        if root**pwr == num:
            return root, pwr
        else:
            root = 0

    print "There is no root, power pair for {}.".format(num)
    return None

print find_root_and_power(user_number)
