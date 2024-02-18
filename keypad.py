"""Module for Keypad composite class"""
import tkinter as tk

class Keypad(tk.Frame):
    """Composite class of Frame, behave similar to a button"""

    def __init__(self, parent, keynames=[], columns=1, **kwargs):
        super().__init__(parent, **kwargs)
        self.keynames = keynames
        self.init_components(columns)

    def init_components(self, columns) -> None:
        """Create a keypad of keys using the keynames list.
        The first keyname is at the top left of the keypad and
        fills the available columns left-to-right, adding as many
        rows as needed.
        :param columns: number of columns to use
        """
        grid_options = {'sticky': tk.NSEW, 'padx': 2, 'pady': 2}
        for key in self.keynames:
            row = self.keynames.index(key) // columns
            col = self.keynames.index(key) % columns
            button = tk.Button(self, text=key)
            button.grid(row=row, column=col, **grid_options)
            self.rowconfigure(row, weight=1)
            self.columnconfigure(col, weight=1)

    def bind(self, sequence=None, func=None, add=None):
        """Bind an event handler to an event sequence."""
        for component in self.children.values():
            component.bind(sequence, func, add)

    def __setitem__(self, key, value) -> None:
        """Overrides __setitem__ to allow configuration of all buttons
        using dictionary syntax.

        Example: keypad['foreground'] = 'red'
        sets the font color on all buttons to red.
        """
        for component in self.children.values():
            component[key] = value

    def __getitem__(self, key):
        """Overrides __getitem__ to allow reading of configuration values
        from buttons.
        Example: keypad['foreground'] would return 'red' if the button
        foreground color is 'red'.
        """
        return self.children['!button'][key]

    def configure(self, cnf=None, **kwargs):
        """Apply configuration settings to all buttons.

        To configure properties of the frame that contains the buttons,
        use `keypad.frame.configure()`.
        """
        for component in self.children.values():
            component.configure(cnf, **kwargs)

    @property
    def frame(self):
        """Return a reference to the superclass"""
        return super()


if __name__ == '__main__':
    keys = list('789456123 0.')  # = ['7','8','9',...]
    def lamo(event):
        """Print the button's text with aghhhhhhhh"""
        print(f'{event.widget["text"]} aghhhhhhhh')
    root = tk.Tk()
    root.title("Keypad Demo")
    keypad = Keypad(root, keynames=keys, columns=3)
    keypad.bind('<Button>', lamo)
    keypad.configure(fg='blue')
    keypad.frame.configure(bg='red')
    keypad.pack(expand=True, fill=tk.BOTH)
    root.mainloop()
