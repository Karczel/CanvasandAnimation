import tkinter as tk
import matplotlib
matplotlib.use("TkAgg") #anti-grain geometry
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np




def plot1(canvas, axes):
    axes.clear()
    x = np.arange(100)
    axes.plot(x, x**2)
    canvas.draw()




def plot2(canvas, axes):
    axes.clear()
    x = np.arange(0,2*np.pi,0.1)
    axes.plot(x, np.sin(x))
    canvas.draw()




root = tk.Tk()
root.title("Matplotlib Integration")


# create Matplotlib figure and plotting axes
fig = Figure()
ax = fig.add_subplot() #ax for axis


# make some grid's columns and row fill extra space
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.rowconfigure(0, weight=1)


# create a canvas to host the figure and place it into the root window
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.grid(column=0, row=0, columnspan=3, sticky="news")


# create a few action buttons
tk.Button(text="Plot1", command=lambda: plot1(canvas, ax)).grid(column=0, row=1)
tk.Button(text="Plot2", command=lambda: plot2(canvas, ax)).grid(column=1, row=1)
tk.Button(text="Quit", command=root.destroy).grid(column=2, row=1)


root.mainloop()

