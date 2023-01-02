import turtle as t

n = 3
t.shape('turtle')
t.color('orange')
t.begin_fill()
for i in range(n):
    t.forward(200)
    t.left(360 / n)
t.end_fill()

t.color('yellow')
t.left(60)
t.begin_fill()
for i in range(n):
    t.forward(200)
    t.left(360 / n)
t.end_fill()

t.color('green')
t.left(120)
t.begin_fill()
for i in range(n):
    t.forward(200)
    t.right(360 / n)
t.end_fill()

t.color('purple')
t.left(180)
t.begin_fill()
for i in range(n):
    t.forward(200)
    t.right(360 / n)
t.end_fill()

t.color('red')
t.left(240)
t.begin_fill()
for i in range(n):
    t.forward(200)
    t.left(360 / n)
t.end_fill()

t.color('blue')
t.left(300)
t.begin_fill()
for i in range(n):
    t.forward(200)
    t.left(120)
t.end_fill()

t.exitonclick()  # 클릭시 창을 닫아주는 명령어
