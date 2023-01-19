from tkinter import *
from tkinter import colorchooser

color = 'black'  # 색상 초기화
bold = False  # 펜 두께 초기화(False:가늘게, True:두껍게)


def get_xy(x, y, b):  # 펜 두께(bold)에 따라 타원의 크기 결정
    if b:
        return x - 4, y - 4, x + 4, y + 4  # 타원의 좌표를 넓게 = 두껍게
    else:
        return x - 2, y - 2, x + 2, y + 2  # 타원의 좌표를 좁게 = 가늘게


def draw(event):
    x1, y1, x2, y2 = get_xy(event.x, event.y, bold)  # 좌표 계산 함수 호출
    canvas.create_oval(x1, y1, x2, y2, fill=color, outline=color)


def clear_canvas():
    canvas.delete("all")


def change_color():
    global color
    color = colorchooser.askcolor()
    color = color[1]  # 색상 선택 함수 호출


def change_bold():
    global bold
    bold = not bold  # 버튼을 누를 때마다 '두껍게 ↔ 가늘게' 가 전환


w = Tk()
w.title("그림판")
canvas = Canvas(w, width=500, height=400)
canvas.pack()
canvas.bind("<B1-Motion>", draw)  # 마우스 왼쪽 클릭에 함수 draw()를 연결

frame = Frame(w)
frame.pack()
bColor = Button(frame, text="색상 선택", font="Tahoma", command=change_color)
bBold = Button(frame, text="두껍게/가늘게", font="Tahoma", command=change_bold)
bClear = Button(frame, text="지우기", font="Tahoma", command=clear_canvas)
bExit = Button(frame, text="나가기", font="Tahoma", command=w.destroy)
bColor.grid(row=0, column=0)
bBold.grid(row=0, column=1)
bClear.grid(row=0, column=2)
bExit.grid(row=0, column=3)

w.mainloop()
