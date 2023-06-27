from tkinter import *
from tkinter import ttk
from functools import partial
import sympy
    
root = Tk()
root.title("Handheld Calculator")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

statement = ""
number_view = ttk.Label(mainframe, text=statement)
number_view.grid(row=0,stick=N)

def add_symbol(character):
    global number_view, statement
    statement = "".join((statement, character))
    number_view["text"] = statement

def all_clear():
    global number_view, statement
    statement = ""
    number_view["text"] = statement

def eval_exp():
    global number_view, statement
    statement = str(sympy.simplify(statement))
    number_view["text"] = statement
    

one_button = ttk.Button(mainframe, text="1", command=partial(add_symbol, "1")).grid(column=0, row=4, stick=S)
two_button = ttk.Button(mainframe, text="2", command=partial(add_symbol, "2")).grid(column=1, row=4, stick=S)
three_button = ttk.Button(mainframe, text="3", command=partial(add_symbol, "3")).grid(column=2, row=4, stick=S)
four_button = ttk.Button(mainframe, text="4", command=partial(add_symbol, "4")).grid(column=0, row=3, stick=S)
five_button = ttk.Button(mainframe, text="5", command=partial(add_symbol, "5")).grid(column=1, row=3, stick=S)
six_button = ttk.Button(mainframe, text="6", command=partial(add_symbol, "6")).grid(column=2, row=3, stick=S)
seven_button = ttk.Button(mainframe, text="7", command=partial(add_symbol, "7")).grid(column=0, row=2, stick=S)
eight_button = ttk.Button(mainframe, text="8", command=partial(add_symbol, "8")).grid(column=1, row=2, stick=S)
nine_button = ttk.Button(mainframe, text="9", command=partial(add_symbol, "9")).grid(column=2, row=2, stick=S)
zero_button = ttk.Button(mainframe, text="0", command=partial(add_symbol, "0")).grid(column=0, row=5, stick=S)

decimal_button = ttk.Button(mainframe, text=".", command=partial(add_symbol, ".")).grid(column=1, row=5, stick=S)
eval_button = ttk.Button(mainframe, text="=", command=eval_exp).grid(column=2, row=5, stick=S)

add_button = ttk.Button(mainframe, text="+", command=partial(add_symbol, "+")).grid(column=3,row=5, stick=S)
subtract_button = ttk.Button(mainframe, text="-", command=partial(add_symbol, "-")).grid(column=3,row=4, stick=S)
mult_button = ttk.Button(mainframe, text="x", command=partial(add_symbol, "*")).grid(column=3,row=3, stick=S)
div_button = ttk.Button(mainframe, text="/", command=partial(add_symbol, "/")).grid(column=3,row=2, stick=S)
pStart_button = ttk.Button(mainframe, text="(", command=partial(add_symbol, "(")).grid(column=0,row=1, stick=S)
pEnd_button = ttk.Button(mainframe, text=")", command=partial(add_symbol, ")")).grid(column=1,row=1, stick=S)
AC_button = ttk.Button(mainframe, text="AC", command=all_clear).grid(column=3, row=1, stick=S)





root.mainloop()