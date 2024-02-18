"""User interface for calculator"""
import tkinter as tk
from tkinter import font
from keypad import Keypad

class CalculatorUI(tk.Tk):
    """UI for calculator
    The UI display numbers and operation in buttons"""
    
    PACKOPTION = {'padx': 2, 'pady': 2, 'expand': True, 'fill': tk.BOTH}

    def __init__(self):
        super().__init__()
        self.title('Calculator')
        self.display_text = tk.StringVar()
        self.default_font = font.nametofont('TkDefaultFont')
        self.default_font.configure(family='Arial TUR', size=16)
        self.create_display()
        self.create_buttons()

    def create_display(self):
        display = tk.Entry(self, justify='right', textvariable=self.display_text, state='readonly')
        display.config(bg='Black', fg='Yellow', font=('Times',30))
        display.pack()

    def create_buttons(self):
        top_row_keys = [' ( ',' ) ','CLR','DEL']
        numbers_keys = list('789456123 0.')
        operators_keys = ['^','/','*','-','+','=']
        top_row_buttons = Keypad(self, keynames=top_row_keys, columns=4)
        keypad = Keypad(self, keynames=numbers_keys, columns=3)
        operators = Keypad(self, keynames=operators_keys)
        top_row_buttons.pack(anchor=tk.N, **self.PACKOPTION)
        keypad.pack(side=tk.LEFT, **self.PACKOPTION)
        operators.pack(side=tk.RIGHT, **self.PACKOPTION)

    def set_display_text(self, text):
        self.display_text.set(text)

    def get_display_text(self):
        return self.display_text.get()

    def run(self):
        """Start the app"""
        self.mainloop()
