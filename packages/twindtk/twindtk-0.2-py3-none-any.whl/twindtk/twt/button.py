import tkinter as tk
from cls.tw import Tw

# Twt Example Button Code
class TwButton(tk.Button):
    def __init__(self, master=None, cls=None, **kwargs):
        super().__init__(master, **kwargs)
        self.tw = Tw(master)
        if cls:
            self.tw.apply_classes(self, cls)