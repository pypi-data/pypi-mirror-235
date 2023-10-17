import tkinter as tk
from cls.tw  import Tw

# Twt Example Label Code
class TwLabel(tk.Label):
    def __init__(self, master=None, cls="", **kwargs):
        super().__init__(master, **kwargs)
        self.tw = Tw(master)
        self.tw.apply_classes(self,cls)