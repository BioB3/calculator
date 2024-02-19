"""Model to habdle calculator calculation and history"""

from math import *
import warnings
warnings.filterwarnings('ignore')

class Model:
    """Model class for calculator"""
    def evaluate_expression(self, expression:str):
        """Evalute expression and return the result"""
        modified = expression.replace('^', '**').replace('mod', '%')
        try:
            result = str(eval(modified))
        except Exception:
            result = 'error'
        return result
