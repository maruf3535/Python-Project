import turtle as tr
# from turtle import *
import time



# speed("normal")
tr.pen(shown=False)
# time.sleep(2)
tr.fd(25)
tr.lt(90)
tr.fd(25)
tr.lt(90)
tr.fd(25)
tr.lt(90)
tr.fd(25)

tr.rt(90)
tr.fd(25)
tr.rt(90)
tr.fd(25)
tr.rt(90)
tr.fd(25)

tr.lt(180)
tr.fd(50)
tr.lt(90)
tr.fd(25)
tr.lt(90)
tr.fd(25)

tr.rt(180)
tr.fd(25)
tr.rt(90)
tr.fd(50)
tr.rt(90)
tr.fd(25)
tr.rt(90)
tr.fd(25)

tr.lt(180)
tr.fd(50)
tr.lt(90)
tr.fd(25)
tr.lt(90)
tr.fd(25)

tr.rt(180)
tr.fd(25)
tr.rt(90)
tr.fd(50)
tr.rt(90)
tr.fd(25)
tr.rt(90)
tr.fd(25)

tr.rt(180)
tr.fd(50)
tr.lt(90)
tr.fd(25)
tr.lt(90)
tr.fd(25)

tr.rt(180)
tr.fd(25)
tr.rt(90)
tr.fd(50)
tr.rt(90)
tr.fd(25)
tr.rt(90)
tr.fd(25)

tr.pen(shown=False, pendown=False)
tr.bk((25 / 2))
tr.lt(90)
tr.fd((25 / 2))

tr.pen(shown=False, pendown=True)
tr.dot(4, "blue")
tr.pen(shown=False, pendown=False)
tr.lt(90)
tr.fd(37.5)
tr.pen(shown=False, pendown=True)
tr.lt(90)
tr.circle(37.5)
tr.lt(90)
tr.fd(37.5)
tr.lt(90)
tr.fd(37.5)
tr.lt(180)
tr.pen(shown=False, pendown=False)
tr.fd(37.5)
tr.pen(shown=False, pendown=True)
tr.fd(37.5)
tr.lt(180)
tr.pen(shown=False, pendown=False)
tr.fd(37.5)
tr.pen(shown=False, pendown=True)
tr.rt(90)
tr.fd(37.5)

print("Success!")
tr.done()
