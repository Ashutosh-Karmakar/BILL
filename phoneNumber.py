from database import getPhNumber
from tkinter import *


def findPhone():
    root = Tk()
    h = Scrollbar(root, orient='horizontal')
    h.pack(side=BOTTOM, fill=X)
    v = Scrollbar(root)
    v.pack(side=RIGHT, fill=Y)

    t = Text(root, width=50, height=30, wrap=NONE,
             xscrollcommand=h.set,
             yscrollcommand=v.set)
    result = getPhNumber()
    for i in range(len(result)):
        t.insert(END, result[i][0] + '\t\t' + result[i][1] + '\t\t' + result[i][2].strftime('%d-%m-%Y') + '\n')
        t.config(font=('times new rommon', 10))
    t.pack(side=TOP, fill=X)
    t.config(state=DISABLED)

    h.config(command=t.xview)
    v.config(command=t.yview)

    root.mainloop()



