def findPayment(loan, r, m):
    """Assumes: loan and r are floats, m an int.
    Returns: The monthly payment for a mortgage of size
    loan at monthly rate of r for m months."""
    return loan * (r * (1+r)**m)/((1 + r)**m -1)

class Mortgage(object):
    """Abstract class for building different kinds of mortgages"""
    def __init__(self, loan, annRate, months):
        """Create a new mortgage"""
        self.loan = loan
        self.rate = annRate/12.0
        self.months = months
        self.paid = [0.0]
        self.owed = [loan]
        self.payment = findPayment(loan, self.rate, months)
        self.legend = None # description of mortgage
        self.findPayment = findPayment

    def make_payment(self):
        """Make a payment."""
        self.paid.append(self.payment)
        reduction = self.payment - self.owed[-1] * self.rate
        self.owed.append(self.owed[-1] - reduction)

    def get_total_paid(self):
        return sum(self.paid)

    def __str__(self):
        return self.legend
