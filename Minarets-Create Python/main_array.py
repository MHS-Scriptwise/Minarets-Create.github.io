from PIL import Image
import tkinter
import turtle
import math
t = turtle.Turtle()
gsize = 100
ts = 10
wx = gsize*ts
wy = gsize*ts
wn = turtle.Screen()
t.hideturtle()
t.speed(0)
wn.colormode(255)
wn.setup(wx,wy)
img = Image.new('RGB', (wx,wy), "white")
Canvas_Array = []
print(gsize**2)
def draw_square(din):
    t.setheading(0)
    t.begin_fill()
    for i in range(4):
        t.forward(din)
        t.right(90)
    t.end_fill()
def Canvas_Update():
    for i in range((int(gsize**2/ts))):
        Canvas_Array.clear()
        color = img.getpixel((i%gsize+ts-1,math.floor(i/gsize)+ts-1))
        R = color[0]
        G = color[1]
        B = color[2]
        Canvas_Array.append([R,G,B])
        print([R,G,B])
