import turtle
import tkinter as tk


def draw():
    for i in range(5):
        turtle.forward(150)
        turtle.right(144)


root = tk.Tk()
canvas = tk.Canvas(width=400, height=400, bg="black")
canvas.grid(column=0,row=0,columnspan=3)
turtle = turtle.RawTurtle(canvas)
turtle.pencolor("green")
turtle.width(3)
turtle.shape("turtle")
tk.Button(text="Draw", command=draw).grid(column=0,row=1)
tk.Button(text="Reset", command=turtle.reset).grid(column=1,row=1)
tk.Button(text="Quit", command=root.destroy).grid(column=2,row=1)


root.mainloop()
