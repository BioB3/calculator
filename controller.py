"""Controller for Calculator app"""
import tkinter as tk
from calculator_ui import CalculatorUI
from model import Model

class Controller:
    """Controller class for calculator"""
    def __init__(self, view:CalculatorUI, model:Model):
        self.view = view
        self.model = model
        self.bind_command()

    def update_display(self, event):
        """Update display's text"""
        pressed_text = event.widget['text']
        self.view.set_display_text(self.view.get_display_text()+pressed_text)

    def calculate(self, *args):
        """Calculate the expression on the display"""
        result = self.model.evaluate_expression(self.view.get_display_text())
        self.view.set_display_text(result)

    def bind_command(self):
        """bind commands to buttons based on thier text"""
        for component in self.view.winfo_children():
            if isinstance(component,tk.Frame):
                for button in component.winfo_children():
                    if isinstance(button, tk.Button):
                        if button['text'] == 'CLR':
                            button.bind('<Button>', lambda event, x='' :
                                self.view.set_display_text(x))
                        elif button['text'] == '=':
                            button.bind('<Button>', self.calculate, add='+')
                            button.bind('<Button>', lambda event, x=self.model.get_history():
                                self.view.set_history(x), add='+')
                        elif button['text'] not in ['=','CLR','DEL']:
                            button.bind('<Button>', self.update_display)

    def run(self):
        self.view.run()
