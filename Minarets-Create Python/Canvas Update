def color_click(x,y):
  tx = x - (x%ts)
  ty = -y + (y%ts)
  t.penup()
  setpos(tx,ty)
  t.pendown()
  t.color("red")
  t.forward(tt-1)
while True:
  wn.update()
  wn.oncsreenclick(color_click)
  Canvas_Update()
  wn.mainloop()
