import time
import tkinter as tk




class Ball:


    def __init__(self, canvas, start_pos, size, color, speed):
        self.__canvas = canvas
        self.__size = size
        self.__id = canvas.create_oval(0, 0, size, size, fill=color)
        self.__speed = speed
        self.__start_pos = start_pos
        self.__x = start_pos
        self.__y = start_pos
        self.reset()
        self.render()
        self.__state = self.state_move_right


    def reset(self):
        x, y = self.__start_pos
        self.move_to(x, y)
        self.__state = self.state_move_right

    def state_move_right(self):
        self.move_to(self.x + self.speed, self.y)
        if self.x > self.__canvas.winfo_width(): # hit the right border
            self.__state = self.state_move_left
        # order affects speed of animation,
        # if put if in front the output will be slower

    def state_move_left(self):
        self.move_to(self.x - self.speed, self.y)
        if self.x < 0: #hit the left border
            self.__state = self.state_move_right

    @property
    def x(self):
        return self.__x


    @property
    def y(self):
        return self.__y


    @property
    def speed(self):
        return self.__speed


    @property
    def size(self):
        return self.__size


    def move_to(self, x, y):
        self.__x = x
        self.__y = y


    def render(self):
        #incomplete
        self.__canvas.moveto(self.__id,
                             self.x - self.size / 2,
                             self.y - self.size / 2,)
        # self.__canvas.coords(self.__id,
        #                      self.x-self.size/2,
        #                      self.y-self.size/2,
        #                      self.x + self.size,
        #                      self.y + self.size
        #                      )


    def update(self):
        # move the ball by 'speed' pixels to the right every time it is updated
        # self.move_to(self.x + self.speed, self.y)
        self.__state() #call as a function


class App(tk.Frame):


    def __init__(self, parent):
        super().__init__(parent)
        parent.rowconfigure(0, weight=1)
        parent.columnconfigure(0, weight=1)
        self.grid(row=0, column=0, sticky="news")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.create_widgets()
        self.is_animating = False
        self.balls = [
            Ball(self.canvas, (0, 50), 10, "blue", 3),
            Ball(self.canvas, (0, 50), 14, "green", 2),
            Ball(self.canvas, (0, 50), 18, "red", 1),
        ]


    def create_widgets(self):
        self.canvas = tk.Canvas(self,
                                borderwidth=0,
                                highlightthickness=0, bg="yellow")
        self.canvas.grid(row=0, column=0, columnspan=3,
                         sticky="news", padx=10, pady=10)
        self.btn_start = tk.Button(self, text="Start",
                                    command=self.toggle_animation)
        self.btn_reset = tk.Button(self, text="Reset",
                                    command=self.reset_animation)
        self.btn_quit = tk.Button(self, text="Quit",
                                   command=root.destroy)
        self.btn_start.grid(row=1, column=0, pady=10)
        self.btn_reset.grid(row=1, column=1, pady=10)
        self.btn_quit.grid(row=1, column=2, pady=10)


    def toggle_animation(self):
        self.is_animating = not self.is_animating
        if self.is_animating:
            self.btn_start.config(text="Stop")
            self.animate()
        else:
            self.btn_start.config(text="Start")


    def reset_animation(self):
        for ball in self.balls:
            ball.reset()
            ball.render()

    def animate(self):
        for ball in self.balls:
            ball.update()
            ball.render()
        if self.is_animating:
            self.after(10, self.animate) #recursively call
            # make it bounce off walls
        pass




if __name__ == "__main__":
    root = tk.Tk()
    root.title("Basic Animation")
    root.geometry("300x300")
    app = App(root)
    root.mainloop()

#ambition:
# physics bounce
# - follow curve path
# ้ัhyperbola -> use speed as state
# y increase speed
#acceleration

# roll ball, stuck at border
# - roll match move
#

# roll based on tilting of canvas/container
# - gravity
# - earlier features
# collision check tangent , vector, trigonometer


# screen pet + chatbox, stop and stand(change gif)
# animating balls (2 walking png) + actions png poses
# - how to replace ball with object
#   that can change gif(transparent bg)
#   and move and change actions based on
#   time.sleep()/time.now()
# - make that object create chatbox after set time
#chat -> polygon in canvas /
# add text and show location like gif # order infront

# get those with state machine probably


# idea: ai chat character + screen pet (double click to go to chat page)
#can connect chat with ai
#maybe add clicking to link to pet <button> or <app>

# curious
# can canvas display mp4?
# how to change from canvas pet to screen pet?

# from teacher
#