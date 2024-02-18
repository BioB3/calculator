"""Model to habdle calculator calculation and history"""

from math import *

class Model:
    def evaluate_expression(self, expression:str):
        """Evalute expression and return the result"""
        modified = expression.replace('^', '**').replace('mod', '%')
        try:
            result = str(eval(modified))
        except:
            result = 'error'
        return result
