def make_times_tables():
    """Make some motherfucking times tables."""
    for i in range(1, 13):
        for j in range(1,13):
            print "{} x {} = {}".format(i, j, i*j)
        print "--------------------------------"

if __name__ == "__main__":
    make_times_tables()
