from math import gcd

class Fraction:
    def __init__(self, num, denum):
        if denum < 0:
            raise ValueError
        d = gcd(num, denum)
        self.num = num // d
        self.denum = denum // d

    def simplify(self, frac):
        d = gcd(frac.num, frac.denum)
        return Fraction(frac.num // d, frac.denum // d)

    def __str__(self):
        return str(self.num) + " / " + str(self.denum)

    def __eq__(self, frac):
        return (self.num / self.denum) == (frac.num / frac.denum)
    
    def __lt__(self, frac):
        return (self.num / self.denum) < (frac.num / frac.denum)
    
    def __add__(self, frac):
        return self.simplify(Fraction((self.num * frac.denum) + (frac.num * self.num), self.denum * frac.denum))

    def __mul__(self, frac):
        return self.simplify(Fraction(self.num * frac.num, self.denum * frac.denum))
