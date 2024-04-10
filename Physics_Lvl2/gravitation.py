import tkinter as tk
import math

class SoftBodySimulation:
    def __init__(self, master, width, height):
        self.master = master
        self.canvas = tk.Canvas(master, width=width, height=height, bg="white")
        self.canvas.pack()
        self.points = []
        self.springs = []
        self.create_soft_body()
        self.create_springs()
        self.simulate()

    def create_soft_body(self):
        num_points = 10
        radius = 20
        center_x = 150
        center_y = 150
        for i in range(num_points):
            angle = (2 * math.pi / num_points) * i
            x = center_x + radius * math.cos(angle)
            y = center_y + radius * math.sin(angle)
            point = self.canvas.create_oval(x-5, y-5, x+5, y+5, fill="blue")
            self.points.append(point)

    def create_springs(self):
        for i in range(len(self.points)):
            for j in range(i+1, len(self.points)):
                spring = Spring(self.canvas, self.points[i], self.points[j])
                self.springs.append(spring)

    def simulate(self):
        for spring in self.springs:
            spring.update()

        self.master.after(10, self.simulate)

class Spring:
    def __init__(self, canvas, point1, point2):
        self.canvas = canvas
        self.point1 = point1
        self.point2 = point2
        self.rest_length = math.sqrt(sum((a - b) ** 2 for a, b in zip(self.canvas.coords(self.point1), self.canvas.coords(self.point2))))

    def update(self):
        x1, y1, _, _ = self.canvas.coords(self.point1)
        x2, y2, _, _ = self.canvas.coords(self.point2)
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        displacement = self.rest_length - distance
        angle = math.atan2(y2 - y1, x2 - x1)
        dx = math.cos(angle) * displacement * 0.1
        dy = math.sin(angle) * displacement * 0.1
        self.canvas.move(self.point1, dx, dy)
        self.canvas.move(self.point2, -dx, -dy)

def main():
    root = tk.Tk()
    root.title("Soft Body Collision Simulation")
    simulation = SoftBodySimulation(root, 400, 400)
    root.mainloop()

if __name__ == "__main__":
    main()
