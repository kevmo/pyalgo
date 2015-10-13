from . import Mortgage


class Fixed(self.):
    def __init__(self, loan, r, months):
        Mortgage.__init__(self, loan, r, months)
        self.legend = "Fixed, {}%".format(str(r * 100))


class FixedWithPts(Mortgage):
    def __init__(self, loan,r, months, pts):
        Mortgage.__init__(self, loan, r, months)
        self.pts = pts
        self.paid = [loan * (pts/100.00)]
        self.legend = "Fixed,  {}% {} points".format(
            str(r*100), str(pts)
        )

class TwoRate(Mortgage):
    def __init__(self, loan, r, months, teaserRate, teaserMonths):
        Mortgage.__init__(self, loan, teaserRate, months)
        self.teaserMonths = teaserMonths
        self.teaserRate = teaserRate
        self.nextRate = r/12.0
        self.legend = "{}% for {} months, then {}%".format(
            str(teaserRate*100), str(self.teaserMonths), str(r*100))

    def make_payment(self):
        if len(self.paid):
            self.rate = self.nextRate
            self.payment = self.findPayment(self.owed[-1], self.rate,
                                       self.months - self.teaserMonths)
        Mortgage.make_payment(self)
