import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=500, borderwidth=0, highlightthickness=0,
                   bg="grey")
canvas.grid()


class Position:
    def __init__(self, x, y, r, color):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.draw_dot()

    def draw_dot(self):
        center = [self.x, self.y]
        canvas.create_oval(center[0] - self.r, center[1] - self.r, center[0] + self.r, center[1] + self.r, fill=self.color)


root.title("Circles and Arcs")
root.mainloop()
