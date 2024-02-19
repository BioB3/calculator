"""User interface for calculator"""
import tkinter as tk
from tkinter import font, ttk
from keypad import Keypad

class CalculatorUI(tk.Tk):
    """UI for calculator
    The UI display numbers and operation in buttons"""
    
    PACKOPTION = {'padx': 2, 'pady': 2, 'expand': True, 'fill': tk.BOTH}

    def __init__(self):
        super().__init__()
        self.title('Calculator')
        self.display_text = tk.StringVar()
        self.selected_func = tk.StringVar()
        self.default_font = font.nametofont('TkDefaultFont')
        self.default_font.configure(family='Arial TUR', size=16)
        self.create_history()
        self.create_display()
        self.create_func_box()
        self.create_buttons()

    def create_display(self):
        display = tk.Entry(self, textvariable=self.display_text, state='readonly',
                           readonlybackground='Black')
        display.config(justify='right', fg='Yellow', font=('Times',30))
        display.pack(fill='x')

    def create_buttons(self):
        top_row_keys = ['(',')','CLR','DEL']
        numbers_keys = ['7','8','9','4','5','6','1','2','3','','0','.']
        operators_keys = ['mod','^','/','*','-','+','=']
        top_row_buttons = Keypad(self, keynames=top_row_keys, columns=4)
        top_row_buttons.configure(height=2)
        keypad = Keypad(self, keynames=numbers_keys, columns=3)
        operators = Keypad(self, keynames=operators_keys)
        top_row_buttons.pack(padx=2, pady=2, fill='x')
        keypad.pack(side=tk.LEFT, **self.PACKOPTION)
        operators.pack(side=tk.RIGHT, **self.PACKOPTION)

    def create_func_box(self):
        func_box = ttk.Combobox(self, font=self.default_font, textvariable=self.selected_func)
        func_box['values'] = ['exp','ln','log10','log2','sqrt','sin','cos','tan']
        self.option_add("*TCombobox*Listbox*Font", self.default_font)
        func_box.set('Mathematical functions')
        func_box.pack(padx=2, pady=2, fill='x')

    def set_display_text(self, text):
        self.display_text.set(text)

    def get_display_text(self):
        return self.display_text.get()

    def create_history(self):
        history_box = tk.Listbox(self, selectmode=tk.SINGLE, font=('Times',20))
        scrollbar = tk.Scrollbar(history_box, orient=tk.VERTICAL)
        history_box.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=history_box.yview)
        history_box.pack(side=tk.TOP, expand=True, fill='both')
        scrollbar.pack(side=tk.RIGHT, fill='y')

    def set_history(self, history: list):
        self.children['!listbox'].delete(0,tk.END)
        while len(history) > 10:
            history.pop(0)
        for i in range(len(history)):
            self.children['!listbox'].insert(i+1, f'{history[i][0]}  =  {history[i][1]}')

    def run(self):
        """Start the app"""
        self.mainloop()
