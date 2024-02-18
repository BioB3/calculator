"""User interface for calculator"""
import tkinter as tk
from tkinter import font
from keypad import Keypad

class CalculatorUI(tk.Tk):
    """UI for calculator
    The UI display numbers and operation in buttons"""
    def __init__(self):
        super().__init__()
        self.title('Calculator')
        self.text = tk.StringVar()
        self.init_components()

    def make_keypad(self) -> tk.Frame:
        """Create a keypad frame and return it"""
        keypad = tk.Frame(self)
        grid_options = {'sticky': tk.NSEW, 'padx': 2, 'pady': 2}
        key_texts = ['7','8','9','4','5','6','1','2','3','','0','.']
        for key in key_texts:
            row = key_texts.index(key) // 3
            col = key_texts.index(key) % 3
            button = tk.Button(keypad, text=key)
            button.bind('<Button>', self.keypress_handler)
            button.grid(row=row, column=col, **grid_options)
            keypad.rowconfigure(row, weight=1)
            keypad.columnconfigure(col, weight=1)
        return keypad

    def make_operator_pad(self) -> tk.Frame:
        """Create an operator pad frame and return it"""
        operator_pad = tk.Frame(self)
        grid_options = {'sticky': tk.NSEW, 'padx': 2, 'pady': 2}
        operators_text = ['*','/','+','-','^','=']
        for operator in operators_text:
            row = operators_text.index(operator)
            button = tk.Button(operator_pad, text=operator)
            button.bind('<Button>', self.keypress_handler)
            button.grid(row=row, column=0, **grid_options)
            operator_pad.rowconfigure(row, weight=1)
        operator_pad.columnconfigure(0, weight=1)
        return operator_pad

    def init_components(self):
        pack_options = {'padx': 2, 'pady': 2, 'expand': True, 'fill': tk.BOTH}
        self.default_font = font.nametofont('TkDefaultFont')
        self.default_font.configure(family='Arial TUR', size=16)
        keypad = Keypad(self, keynames=list('789456123 0.'), columns=3)
        operators = Keypad(self, keynames=list('*/+-^='))
        keypad.bind('<Button>', self.keypress_handler)
        operators.bind('<Button>', self.keypress_handler)
        output = tk.Label(self, bg='Black', fg='Yellow', anchor=tk.E, 
                          textvariable=self.text, font=('Times',30))
        output.pack(side=tk.TOP, **pack_options)
        keypad.pack(side=tk.LEFT, **pack_options)
        operators.pack(side=tk.RIGHT, **pack_options)

    def keypress_handler(self, event):
        pressed_text = event.widget['text']
        self.text.set(self.text.get() + pressed_text)

    def run(self):
        """Start the app"""
        self.mainloop()
