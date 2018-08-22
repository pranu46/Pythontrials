# Calculate simple and compound interest for a given principal amount.

class InterestCalculator:
    def __init__(self, time, rate, principal):
        self.principal = principal
        self.rate = rate*0.01
        self.time = time
        self.finalVal = 0.0
        self.totalVal = 0.0

class SICalculator(InterestCalculator):
    def calcfinalval(self):
        self.finalVal = self.principal*(1 + (self.rate * self.time))
        self.totalVal = self.principal + self.finalVal

class CICalculator(InterestCalculator):
    def calcfinalval(self):
        self.finalVal = self.principal * (((1 + self.rate / 12))**(12 * self.time))
        self.totalVal = self.principal + self.finalVal


s = SICalculator(2,0.1,1000)
s.calcfinalval()
print('Simple Interest is :', "%.2f" % s.finalVal)
print('Total amount is : ',"%.2f" % s.totalVal)

c = CICalculator(2,0.1,1000)
c.calcfinalval()
print('Compound Interest is :', "%.2f" % c.finalVal)
print('Total amount is : ',"%.2f" % c.totalVal)
