# coding:utf-8
import turtle as t

t.screensize(400, 300,"black")
t.pensize(2)
t.colormode(255)
t.color((255,255,255),"black")
t.setup(800,600)
t.speed(100)


t.pu()
t.goto(130,40)
t.seth(45)
t.begin_fill()
t.pd()

a = 1.2
for i in range(17):
	t.rt(1)
	t.fd(a)

t.seth(160)
for i in range(32):
	t.rt(1)
	t.fd(a)

t.seth(55)
t.fd(7)
t.seth(120)
t.fd(27)
t.seth(190)
t.fd(10)
t.seth(145)
t.fd(25)
t.seth(-88)
t.fd(14)
t.seth(145)
t.fd(27)
t.seth(-88)
t.fd(10)
t.seth(145)
t.fd(25)
t.seth(-90)
t.fd(5)

t.seth(155)
b = 1
for i in range(58):
	t.lt(0.4)
	t.fd(b)
#155,58,0.4,1

c = 1
for i in range(95):
	t.rt(1)
	t.fd(c)


t.seth(160)
d = 1
for i in range(260):
	t.lt(0.1)
	t.fd(d)

t.seth(2)
e = 1
for i in range(248):
	t.rt(0.1)
	t.fd(e)

t.seth(-75)
f = 1
for i in range(65):
	t.lt(0.2)
	t.fd(f)

g = 1.2
t.seth(-170)
for i in range(160):
	t.lt(1)
	t.fd(g)

h = 1
t.seth(-5)
for i in range(210):
	t.rt(0.4)
	t.fd(h)

j = 1
t.seth(85)
for i in range(160):
	t.lt(0.4)
	t.fd(j)

k = 1
t.seth(0)
for i in range(140):
	t.rt(0.6)
	t.fd(k)

l = 1
t.seth(87)
for i in range(150):
	t.lt(0.6)
	t.fd(l)

m = 1
t.seth(175)
for i in range(50):
	t.rt(0.2)
	t.fd(m)

n = 1
t.seth(170)
for i in range(190):
	t.rt(1)
	t.fd(n)

t.seth(-10)
for i in range(105):
	t.rt(0.2)
	t.fd(1)

t.seth(-80)
t.fd(10)
t.goto(130,40)
t.end_fill()


# wing 2
t.pu()
t.goto(-92,174)
t.pd()

t.seth(170)
d = 1
for i in range(270):
	t.lt(0.09)
	t.fd(d)

t.seth(6)
e = 1
for i in range(270):
	t.rt(0.05)
	t.fd(e)

t.seth(105)
e = 1
for i in range(12):
	t.rt(0.1)
	t.fd(e)

# wing 3
t.pu()
t.goto(-90,150)
t.pd()

t.seth(180)
d = 1
for i in range(265):
	t.lt(0.08)
	t.fd(d)

t.seth(15)
e = 1
for i in range(265):
	t.rt(0.05)
	t.fd(e)

t.seth(105)
e = 1
for i in range(12):
	t.rt(0.1)
	t.fd(e)

#eye
t.pu()
t.goto(110,80)
t.pencolor("red")
t.pensize(5)
t.pd()
t.seth(120)
t.fd(12)

t.pu()
t.goto(200,200)

t.done()