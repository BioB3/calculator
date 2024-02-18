"""Model to habdle calculator calculation and history"""

from math import *

class Model:
    def evaluate_expression(self, expression):
        """Evalute expression and return the result"""
        try:
            result = str(eval(expression))
        except:
            result = 'error'
        return result
