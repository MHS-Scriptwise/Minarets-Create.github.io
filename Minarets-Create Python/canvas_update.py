def color_click(x,y):
    tx = x - (x%ts)
    ty = y - (y%ts)+ts
    t.penup()
    t.setpos(tx,ty)
    t.pendown()
    t.color("red")
    draw_square(ts)
while True:
    wn.update()
    wn.onscreenclick(color_click)
    Canvas_Update()
    wn.mainloop()
