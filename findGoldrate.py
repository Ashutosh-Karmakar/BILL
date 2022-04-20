from tkinter import *

from baseInitialization import UiFields
from common import createCalender, visual_date_convert
from database import findGRDate


def findGoldRateOnDate(u: UiFields):
    root = Tk()
    root.configure(bg=u.background_color)
    root.title("Gold Rate")
    root.geometry("400x600")
    cal = createCalender(root)
    cal.pack(pady=20)

    def grad_date():
        u.grFindDate = visual_date_convert(cal.get_date())
        print(u.grFindDate)
        i = findGRDate(u)

        date.config(text="Selected Date is: " + u.grFindDate)
        goldRate.config(text=u.grRateOnDate)
        goldRate.config(font=("times new rommon", 11))

    Button(root, text="Get Date",
           command=grad_date).pack(pady=20)

    date = Label(root, text="")
    date.pack(pady=20)
    goldRate = Label(root, text="")
    goldRate.pack(pady=20)

    root.mainloop()
