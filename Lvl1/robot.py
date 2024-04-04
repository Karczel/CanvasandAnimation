import tkinter as tk
import time

root = tk.Tk()
root.title("Canvas Item Example")
frame = tk.Frame()
frame.pack()
canvas = tk.Canvas(frame, width=500, height=400, background="gray75")
canvas.pack()

face_id = canvas.create_rectangle(100, 100, 200, 200, width=2, fill="lightblue")
left_eye_id = canvas.create_oval(120, 120, 140, 150, width=3, fill="lightgray", outline="green")
right_eye_id = canvas.create_oval(160, 120, 180, 150, width=3, fill="lightgray", outline="green")
mouth_id = canvas.create_line(120, 175, 180, 175, width=10, fill="green")
text_id = canvas.create_text(150, 210, text="Hello, World!", anchor="n", fill="red",
                   font=("Arial", 30))

# canvas.itemconfigure(text_id, text="Goodbye"); time.sleep(5)
# canvas.itemconfigure("eyes", fill="red")

canvas.create_oval(120, 120, 140, 150,
width=3, fill="lightgray", outline="green",
tags=["eyes"])
canvas.create_oval(160, 120, 180, 150,
width=3, fill="lightgray", outline="green",
tags=["eyes"])
canvas.itemconfigure("eyes", fill="red")

root.mainloop()

