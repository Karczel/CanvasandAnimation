import tkinter as tk
import math

class SoftBodySimulation:
    def __init__(self, master, width, height):
        self.master = master
        self.canvas = tk.Canvas(master, width=width, height=height, bg="white")
        self.canvas.pack()
        self.points = []
        self.create_soft_body()
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

    def simulate(self):
        for i, point1 in enumerate(self.points):
            x1, y1, _, _ = self.canvas.coords(point1)
            for point2 in self.points[i+1:]:
                x2, y2, _, _ = self.canvas.coords(point2)
                distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
                if distance < 50:  # Soft body collision threshold
                    self.canvas.move(point1, 1, 1)
                    self.canvas.move(point2, -1, -1)
        self.master.after(10, self.simulate)

def main():
    root = tk.Tk()
    root.title("Soft Body Collision Simulation")
    simulation = SoftBodySimulation(root, 400, 400)
    root.mainloop()

if __name__ == "__main__":
    main()
