'''
Addition and subtraction of quadratic expressions by using operator overloading.
Check the equality of the quadratic expressions.
Check the co-efficients of the quadratic expressions to put  +  or  - in return string
'''

class Quadratic:

    def __init__(self, Q1, Q2, Q3):
       self.Q1 = Q1
       self.Q2 = Q2
       self.Q3 = Q3

    def __str__(self):
        if self.Q1 < 0:
            self.Q1 = '-x^2'
        elif self.Q1 == 1:
            self.Q1 = 'x^2'
        else:
            self.Q1 = '%sx^2' % self.Q1

        if self.Q2 < 0:
            self.Q2 = ' - %sx' % (self.Q2 * -1)
        elif self.Q2 == 0:
            self.Q2 = ''
        elif self.Q2 == 1:
            self.Q2 = ' + x'
        else:
            self.Q2 = ' + %sx' % self.Q2

        if self.Q3 < 0:
            self.Q3 = ' - %s' % (self.Q3 * -1)
        elif self.Q3 == 0:
            self.Q3 = ''
        else:
            self.Q3 = ' + %s' % self.Q3

        return self.Q1 + self.Q2 + self.Q3


    def __add__(self, other):
        return Quadratic(self.Q1 + other.Q1, self.Q2 + other.Q2, self.Q3 + other.Q3)

    def __sub__(self, other):
        return Quadratic(self.Q1 - other.Q1, self.Q2 - other.Q2, self.Q3 - other.Q3)

    def __eq__(self,other):
        if self.Q1 == other.Q1 and self.Q2 == other.Q2 and self.Q3 == other.Q3:
            return True
        else:
            return False


Q1 = Quadratic(3, 8, -5)
Q2 = Quadratic(2, 3, 7)
print('Sum of 2 quadratic expressions:', Q1 + Q2)
print('Difference between 2 quadratic expressions:', Q1 - Q2)
print('Is the 2 given quadratic expressions are same ?', Q1 == Q2)

