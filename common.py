
from datetime import datetime
from tkcalendar import Calendar
from tkinter import *

def createCalender(root):
    cur_date = datetime.now()
    cal = Calendar(root, selectmode='day',
                   year=cur_date.year, month=cur_date.month,
                   day=cur_date.day)
    return cal


def date_to_string(date):
    if type(date) == str:
        return datetime.strptime(date, '%m/%d/%y')
    if type(date) == datetime:
        return date.strftime('%d-%m-%Y')


def visual_date_convert(date):
    datefind = ''
    result = date
    result = result.split('/')

    datefind = datefind + '20' + result[2] + '-'
    if len(result[0]) == 1:
        result[0] = '0' + result[0]
    datefind = datefind + result[0] + '-'

    if len(result[1]) == 1:
        result[1] = '0' + result[1]
    datefind = datefind + result[1]
    return datefind


def insert_into_disabled(widget, value):
    widget.config(state='normal')
    widget.delete(0, END)
    widget.insert(0, value)
    widget.config(state=DISABLED)