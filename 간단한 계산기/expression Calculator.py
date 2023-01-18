import tkinter as tk


def Cal():
    label.configure(text="결과 값 = " + str(eval(entry.get())))


window = tk.Tk()  # 윈도우 창 생성

window.title("계산기")  # 윈도우 창 제목 설정
window.geometry("300x200+100+100")  # 창 너비와 높이, 초기 화면의 위치 설정
window.resizable(False, False)  # 상하 좌우로 창 크기 조절 가능 여부

entry = tk.Entry(window)  # 텍스트를 입력받거나 출력하기 위한 창 생성
entry.pack()

button = tk.Button(window, text="계산", command=Cal)  # cal함수를 실행할 버튼 생성
button.pack()

label = tk.Label(window)  # label 위젯 설정
label.pack()  # 위젯 배치

window.mainloop()  # 윈도우 창이 종료될 때 까지 실행
