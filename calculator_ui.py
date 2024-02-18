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
        self.text = tk.StringVar()
        self.default_font = font.nametofont('TkDefaultFont')
        self.default_font.configure(family='Arial TUR', size=16)
        self.create_display()
        self.create_buttons()

    def create_display(self):
        display = tk.Entry(self, justify='right', textvariable=self.text, state='disabled')
        display.pack()
        

    def create_buttons(self):
        top_row_keys = ['(',')','CLR']
        top_row_buttons = Keypad(self, keynames=top_row_keys, columns=3)
        keypad = Keypad(self, keynames=list('()789456123 0.'), columns=3)
        operators = Keypad(self, keynames=list('*/+-^='))
        top_row_buttons.pack(side=tk.LEFT, **self.PACKOPTION)
        keypad.pack(side=tk.LEFT, **self.PACKOPTION)
        operators.pack(side=tk.RIGHT, **self.PACKOPTION)
        

    def init_components(self):
        keypad = Keypad(self, keynames=list('()789456123 0.'), columns=3)
        operators = Keypad(self, keynames=list('*/+-^='))
        keypad.bind('<Button>', self.keypress_handler)
        operators.bind('<Button>', self.keypress_handler)
        output = tk.Label(self, bg='Black', fg='Yellow', anchor=tk.E, 
                          textvariable=self.text, font=('Times',30))
        output.pack(side=tk.TOP, **self.PACKOPTION)
        keypad.pack(side=tk.LEFT, **self.PACKOPTION)
        operators.pack(side=tk.RIGHT, **self.PACKOPTION)

    def run(self):
        """Start the app"""
        self.mainloop()
