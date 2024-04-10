from PIL import Image, ImageTk
import tkinter as tk

# img = Image.open("pic.png")
img = Image.open("PowerTwo.png")
new_size = 300

root = tk.Tk()
root.title("Canvas Item Example")
frame = tk.Frame()
frame.pack()
canvas = tk.Canvas(frame, width=new_size, height=new_size, background="gray75")
canvas.pack()

resized_image= img.resize((new_size, new_size))

imgtk = ImageTk.PhotoImage(resized_image)
canvas.create_image(0, 0, image=imgtk)

root.mainloop()