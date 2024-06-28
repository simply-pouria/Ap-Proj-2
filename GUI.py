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
        canvas.create_oval(center[0] - self.r, center[1] - self.r, center[0] + self.r, center[1] + self.r,
                           fill=self.color)

    def change_color(self, new_color):
        del self
        return Position(self.x, self.y, self.r, new_color)
# These dictionaries are used to label each circle with a specific color
white_circles_dicts = {}
red_circles_dicts = {}
blue_circles_dicts = {}

white_circles_positions = [
    (350, 210) , (320, 210) , (290, 210) , (260, 210) , (230, 210) ,(230, 240),
    (230, 270) , (230, 300) , (230, 330) , (200, 330) , (170, 330) , (170, 300) ,
    (170, 270) , (170, 240) , (170, 210) , (140, 210) , (110, 210) , (80, 210) ,
    (50, 210) , (50, 180) ,(50, 150) , (80, 150) , (110, 150) , (140, 150) ,
    (170, 150) , (170, 120) , (170, 90) , (170, 60) , (170, 30) , (200, 30),
    (230, 30) , (230, 60) , (230, 90) , (230, 120) , (230, 150) , (260, 150),
    (290, 150) , (320, 150) , (350, 150) , (350, 180)
]

red_circles_positions = [
    (320, 180), (290, 180), (260, 180), (230, 180)
]

blue_circles_positions = [
    (80, 180), (110, 180), (140, 180), (170, 180)
]

for position in white_circles_positions :
    x = position[0]
    y = position[1]
    r = 10
    color = 'white'
    circle_position = Position(x, y, r, color)
    white_circles_dicts[white_circles_positions.index(position) + 1] = circle_position

for position in red_circles_positions :
    x = position[0]
    y = position[1]
    r = 10
    color = 'red'
    circle_position = Position(x, y, r, color)
    red_circles_dicts[red_circles_positions.index(position) + 1] = circle_position

for position in blue_circles_positions :
    x = position[0]
    y = position[1]
    r = 10
    color = 'blue'
    circle_position = Position(x, y, r, color)
    blue_circles_dicts[blue_circles_positions.index(position) + 1] = circle_position

root.title("Mensch")
root.mainloop()
