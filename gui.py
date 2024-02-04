from pip import main
import vader as v
from tkinter import *
from tkinter import ttk

def valuereturn():
    obj = v.Vader(sentence.get())
    obj.analyze()
    pos.set(obj.positive*100)
    neg.set(obj.negative*100)
    neu.set(obj.neutral*100)

root = Tk()
root.title("VADER Sentiment Analyzer")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

sentence = StringVar()
ttk.Label(mainframe, text="How are you?").grid(column=1, row=1, sticky=(W, E))
sentenceentry = ttk.Entry(mainframe, width=7, textvariable=sentence)
sentenceentry.grid(column=2, row=1, sticky=(W, E))
ttk.Button(mainframe, text="Calculate", command=valuereturn).grid(column=2, row=2, sticky=(W))

pos = StringVar()
neg = StringVar()
neu = StringVar()
most = StringVar()
ttk.Label(mainframe, text="How you're feeling:").grid(column=1, row=3, sticky=(W, E))
ttk.Label(mainframe, text="Positive: ").grid(column=1, row=4, sticky=(W, E))
ttk.Label(mainframe, text="Neutral: ").grid(column=1, row=5, sticky=(W, E))
ttk.Label(mainframe, text="Negative: ").grid(column=1, row=6, sticky=(W, E))
ttk.Label(mainframe, textvariable=pos).grid(column=2, row=4, sticky=(W, E))
ttk.Label(mainframe, textvariable=neu).grid(column=2, row=5, sticky=(W, E))
ttk.Label(mainframe, textvariable=neg).grid(column=2, row=6, sticky=(W, E))
ttk.Label(mainframe, text="%").grid(column=3, row=4, sticky=(W, E))
ttk.Label(mainframe, text="%").grid(column=3, row=5, sticky=(W, E))
ttk.Label(mainframe, text="%").grid(column=3, row=6, sticky=(W, E))
ttk.Label(mainframe, text="You're feeling mostly: ").grid(column=1, row=7, sticky=(W,E))
ttk.Label(mainframe, textvariable=most).grid(column=3, row=7, sticky=(W,E))

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

sentenceentry.focus()
root.bind("<Return>", valuereturn)

root.mainloop()
