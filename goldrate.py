import tkinter as tk
from tkinter import simpledialog
from tkinter import *
from tkinter import messagebox
from baseInitialization import UiFields
from database import saveGoldRate
from backend import startOverGOLDRATE
from common import insert_into_disabled

def calc(u: UiFields, i):
    try:
        wt = float(u.wt_txt[i].get())
        amt = float(u.net_txt[i].get())
        gr = u.gold_rate
        print(gr)
        cost = amt * (100 / 103)
        if cost < amt:
            cgst = amt - cost
        else:
            cgst = 0
        mc = (cost / wt) - gr
        mc = round(mc, 2)
        cgst = round(cgst / 2, 2)
        gstamt = cgst * 2

        if mc < 0:
            startOverGOLDRATE(u)
            print("There is a error in calculation mc")
            messagebox.showerror("Error", 'GOLD RATE IS TOO HIGH')
            return 1

        insert_into_disabled(u.cgst_txt[i], cgst)
        insert_into_disabled(u.sgst_txt[i], cgst)
        insert_into_disabled(u.gstAmt_txt[i], gstamt)
        insert_into_disabled(u.mc_txt[i], mc)

        u.gstAmt_txt[i].focus_set()
    except Exception as e:
        print("There is a error in cal in goldrate : {0}".format(e))
        messagebox.showerror("Error", "There is a error in cal in goldrate : {0}".format(e))


def changeGoldRate(u: UiFields):
    gr = tk.Tk()
    gr.withdraw()
    gold_rate = simpledialog.askstring(title="Gold Rate", prompt="Gold Rate?:")
    if not gold_rate.isnumeric():
        messagebox.showerror("Error", "Gold Rate can only be number")
        return
    if len(gold_rate) > 4:
        tens = 10 ** (len(gold_rate) - 4)
        u.gold_rate = int(gold_rate) // tens
    else:
        u.gold_rate = int(gold_rate)
    saveGoldRate(u)
    for i in range(0, 9):
        insert_into_disabled(u.unit_txt[i], u.gold_rate)

    u.old_gold_rate = u.gold_rate - 100

    for i in range(0, 3):
        insert_into_disabled(u.oldunit_txt[i], u.old_gold_rate)

    if u.mobile_txt.get() == '':
        u.mobile_txt.focus()
        u.entryCount = 0
        return
    l = 0
    for l in range(0, 10):
        if u.des_txt[l].get() == '':
            u.des_txt[l].focus()
            u.entryCount = 4 + l * 3
            break
        if u.wt_txt[l].get() == '':
            u.wt_txt[l].focus()
            u.entryCount = 5 + l * 3
            break
        if u.net_txt[l].get() == '':
            u.net_txt[l].focus()
            u.entryCount = 6 + l * 3
            break
        mm = calc(u, l)
        if mm == 1:
            break
    if l == 10:
        u.oldwe_txt[0].focus()
