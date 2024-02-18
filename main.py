"""Main part to start Calculator app"""

from calculator_ui import CalculatorUI
from controller import Controller
from model import Model

view = CalculatorUI()
model = Model()
calculator = Controller(view, model)
calculator.run()