import vader as v
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("VADER Sentiment Analyzer")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

sentence = StringVar()
si = ttk.Entry(mainframe, width=7, textvariable=sentence)
si.grid(column=2, row=1, sticky=(W, E))

analyze = StringVar()
ttk.label()