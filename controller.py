"""Controller for Calculator app"""
from calculator_ui import CalculatorUI
from model import Model

class Controller:
    """Controller class for calculator"""
    def __init__(self, view:CalculatorUI, model:Model):
        self.view = view
        self.model = model
        self.bind_command()

    def update_display(self, event):
        pressed_text = event.widget['text']
        self.view.set_display_text(self.view.get_display_text+pressed_text)

    def bind_command(self):
        """bind commands to buttons based on thier text"""
        for frame in self.view.winfo_children():
            for component in frame:
                component.bind('<Button>', self.update_display)
