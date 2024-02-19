"""Controller for Calculator app"""
import tkinter as tk
from tkinter import ttk
from calculator_ui import CalculatorUI
from model import Model
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

class Controller:
    """Controller class for calculator"""
    def __init__(self, view:CalculatorUI, model:Model):
        self.view = view
        self.model = model
        self.bind_command()
        pygame.init()

    def update_display(self, event):
        """Update display's text"""
        pressed_text = event.widget['text']
        self.view.set_display_text(self.view.get_display_text()+pressed_text)

    def update_display_func(self, *args):
        """Update display's text for functions combobox"""
        current_input = self.view.get_display_text()
        if current_input.endswith(('(','mod','^','/','*','-','+')):
            to_be_add = self.view.get_display_text()+self.view.selected_func.get()+'('
        else:
            to_be_add = self.view.selected_func.get()+'('+\
                self.view.get_display_text()+')'
        self.view.set_display_text(to_be_add)

    def del_display(self, event):
        """handle DEL button by deleting last input"""
        current_input = self.view.get_display_text()
        if current_input.endswith((' exp ',' ln  ','log10',' log2',' sqrt',' sin ',' cos ',' tan ')):
            new_text = current_input[:-5]
        else:
            new_text = current_input[:-1]
        self.view.set_display_text(new_text)

    def recall_history(self, event, index):
        selection_index = event.widget.curselection()
        selection_text = event.widget.get(selection_index[0])
        self.view.set_display_text(selection_text.split()[index])

    def calculate(self, *args):
        """Calculate the expression on the display"""
        result = self.model.evaluate_expression(self.view.get_display_text())
        if result == 'error':
            self.view.children['!entry'].configure(fg='red')
            my_sound = pygame.mixer.Sound('beep-03.wav')
            my_sound.play()
        else:
            self.view.children['!entry'].configure(fg='yellow')
            self.view.set_display_text(result)

    def bind_command(self):
        """bind commands to component based on thier type and text"""
        for component in self.view.winfo_children():
            if isinstance(component,tk.Frame):
                for button in component.winfo_children():
                    if button['text'] == 'CLR':
                        button.bind('<Button>', lambda event, x='' :
                            self.view.set_display_text(x))
                    elif button['text'] == '=':
                        button.bind('<Button>', self.calculate, add='+')
                        button.bind('<Button>', lambda event, x=self.model.history:
                            self.view.set_history(x), add='+')
                    elif button['text'] == 'DEL':
                        button.bind('<Button>', self.del_display)
                    else:
                        button.bind('<Button>', self.update_display)
            elif isinstance(component, tk.Listbox):
                component.bind('<Button-1>', lambda event:
                    self.recall_history(event,0), add='+')
                component.bind('<Button-3>', lambda event:
                    self.recall_history(event,2), add='+')
            elif isinstance(component, ttk.Combobox):
                component.bind('<<ComboboxSelected>>', self.update_display_func)

    def run(self):
        self.view.run()
