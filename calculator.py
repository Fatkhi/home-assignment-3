import math
from decimal import Decimal

class Calculator:
    def add(self, x, y):
        try:
            return float(Decimal(str(x)) + Decimal(str(y)))
        except:
            return 'error'

    def subtract(self, x, y):
        try:
            return float(Decimal(str(x)) - Decimal(str(y)))
        except:
            return 'error'

    def divide(self, x, y):
        if y == 0:
            raise ValueError
        try:
            return float(Decimal(str(x)) / Decimal(str(y)))
        except:
            return 'error'

    def multiply(self, x, y):
        try:
            return float(Decimal(str(x)) * Decimal(str(y)))
        except:
            return 'error'

    def cos(self, x):
        try:
            return math.cos(Decimal(str(x)))
        except:
            return 'error'