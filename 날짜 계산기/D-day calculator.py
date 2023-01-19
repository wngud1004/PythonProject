from tkinter import *
from datetime import *


def get_today():
    today = datetime.today()
    return today.year, today.month, today.day


def str_to_date(s):
    try:
        y = int(s[:4])
        m = int(s[4:6])
        d = int(s[6:])
    except:
        print("날짜 입력 오류")
        return -1
    else:
        return datetime(y, m, d)


def calc_days(date):
    days = hours = 0
    if str_to_date(date) != -1:
        result = str_to_date(date) - datetime.today()
        days = result.days
        hours = result.seconds // 3600

    return days, hours


def f_click():
    days, hours = calc_days(enDday.get())
    lbResult.config(text="D- {0}일 {1}시간".format(days, hours))


w = Tk()
w.title('D-Day 계산기')

yy, mm, dd = get_today()
Label(w, text="오늘 날짜", width=20).grid(row=0, column=0, pady=5)
lbToday = Label(w, text="{0}년 {1}월 {2}일".format(yy, mm, dd))
lbToday.grid(row=0, column=1)

Label(w, text="D-Day (예)20230129").grid(row=1, column=0, pady=5)
enDday = Entry(w)
enDday.grid(row=1, column=1)

btCalc = Button(w, text="계산하기", width=20, command=f_click)
btCalc.grid(row=2, column=0, columnspan=2, pady=5)

lbResult = Label(w, text="D-", font=("arial", 15), fg="red")
lbResult.grid(row=3, column=0, columnspan=2, pady=5)

w.mainloop()
