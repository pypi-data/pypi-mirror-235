# main.py
import tkinter as tk

# twt components
import twt.button as btn

# other Examples Import
from twt.input import TwEntry
from twt.label import TwLabel

root = tk.Tk()
 
class Example:
    # example function
    def login():
       print("You have been logged in")

    # App
   
    root.geometry("700x400")
    root.title("Wind.tk")
 
# Window Icon
    icon = tk.PhotoImage(file="C:\\Users\\runo\\Desktop\\twt\\assets\\wind.png")
    root.iconphoto(False, icon)


# start app Function
    def start():
       root.mainloop()

# example button
    loginButton = btn.TwButton(root, text="Login", cls="bg-red-500 text-red-100 w-5 h-[1] active:bg-red-400 border-none active:text-blue-500", command=login)
    loginButton.pack()

# example label
    label = TwLabel(root, text="Email", cls="text-white bg-blue-500 px-20 py-1 border-none")
    label.pack()

# example Input
    entry = TwEntry(root, cls="w-[30]  bg-white border text-black border-w-[1]")
    entry.pack()

# start app
    start()

