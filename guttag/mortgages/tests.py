from types import Fixed, FixedWithPts, TwoRate

def compareMortgages(amt, years, fixedRate, pts, ptsRate,
                    varRate1, varRate2, varMonths):
    totMonths = years*12
    fixed1 = Fixed(amt, fixedRate, totMonths)
    fixed2 = FixedWithPts(amt, ptsRate, totMonths, pts)
    tworate = TwoRate(amt, varRate2, totMonths, varRate1, varMonths)
    morts = [fixed1, fixed2, tworate]

    for m in range(totMonths):
        for mort in morts:
            mort.make_payment()

    for m in morts:
        print m
        print "TOTAL: $", str(int(m.get_total_paid()))


compareMortgages(amt=200000, years=30, fixedRate=0.07,
                 pts=3.25, ptsRate=0.05, varRate1=.045,
                 varRate2=.095, varMonths=48)
