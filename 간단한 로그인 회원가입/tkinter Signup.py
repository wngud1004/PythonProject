from tkinter import *


def bt_click():
    name = nameEn.get()  # 이름을 가져와 name에 저장
    pwd = pwdEn.get()  # 비밀번호를 가져와 pwd에 저장
    print(name, ":", pwd)  # 이름과 비밀번호를 쉘에 출력


w = Tk()
w.title("회원 가입")

Label(w, text="이    름", width=15).grid(row=0, column=0)
nameEn = Entry(w)
nameEn.grid(row=0, column=1)

Label(w, text="비밀번호", width=15).grid(row=1, column=0)
pwdEn = Entry(w)
pwdEn.grid(row=1, column=1)

bt = Button(w, text="확인", fg="blue", command=bt_click)  # 이벤트 처리 함수 연결
bt.grid(row=2, column=0, columnspan=2)

w.mainloop()
