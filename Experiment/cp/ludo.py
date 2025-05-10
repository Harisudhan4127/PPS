import tkinter as tk
import random

COLORS = ["red", "green", "yellow", "blue"]
PLAYER_STARTS = {
    "red": (1, 6),
    "green": (6, 13),
    "yellow": (13, 8),
    "blue": (8, 1),
}

class LudoGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Ludo Game - 4 Players")

        self.canvas = tk.Canvas(root, width=600, height=600)
        self.canvas.pack()

        self.draw_board()
        self.players = {}
        for color in COLORS:
            pos = PLAYER_STARTS[color]
            x, y = self.coord(pos)
            self.players[color] = self.canvas.create_oval(x+5, y+5, x+35, y+35, fill=color)

        self.turn_index = 0
        self.dice_button = tk.Button(root, text="Roll Dice", command=self.roll_dice)
        self.dice_button.pack()
        self.status_label = tk.Label(root, text="Red's Turn")
        self.status_label.pack()

    def draw_board(self):
        size = 40
        # Draw grid (15x15)
        for i in range(15):
            for j in range(15):
                x1 = j * size
                y1 = i * size
                x2 = x1 + size
                y2 = y1 + size
                fill = "white"
                if i < 6 and j < 6:
                    fill = "red"
                elif i < 6 and j > 8:
                    fill = "green"
                elif i > 8 and j < 6:
                    fill = "yellow"
                elif i > 8 and j > 8:
                    fill = "blue"
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=fill, outline="black")

    def coord(self, grid_pos):
        size = 40
        i, j = grid_pos
        return j * size, i * size

    def roll_dice(self):
        color = COLORS[self.turn_index]
        roll = random.randint(1, 6)
        self.status_label.config(text=f"{color.capitalize()} rolled {roll}")
        
        # Move the token by shifting coordinates (basic placeholder logic)
        token = self.players[color]
        x0, y0, x1, y1 = self.canvas.coords(token)
        dx = 40 * roll
        self.canvas.move(token, dx, 0)

        # Next player's turn
        self.turn_index = (self.turn_index + 1) % 4
        next_color = COLORS[self]()
