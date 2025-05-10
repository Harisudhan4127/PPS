import tkinter as tk
import random

# Snakes and ladders
snakes = {16: 6, 47: 26, 49: 11, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

class SnakeLadderGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake and Ladder")

        self.canvas = tk.Canvas(root, width=600, height=600)
        self.canvas.pack()

        # Load images
        self.snake_img = tk.PhotoImage(file="snake.png")
        self.ladder_img = tk.PhotoImage(file="ladder.png")

        self.draw_board()

        self.player_pos = 1
        self.player = self.canvas.create_oval(10, 550, 30, 570, fill='blue')

        self.roll_button = tk.Button(root, text="Roll Dice", command=self.roll_dice)
        self.roll_button.pack(pady=10)

        self.status_label = tk.Label(root, text="Click to roll the dice")
        self.status_label.pack()

    def draw_board(self):
        size = 60
        for i in range(10):
            for j in range(10):
                x = j * size
                y = i * size
                if i % 2 == 0:
                    num = 100 - (i * 10 + j)
                else:
                    num = 100 - (i * 10 + (9 - j))
                self.canvas.create_rectangle(x, y, x + size, y + size, fill="#FFFACD")
                self.canvas.create_text(x + 30, y + 30, text=str(num), font=('Arial', 10))

        # Place snakes and ladders
        for start, end in snakes.items():
            self.place_image(start, end, self.snake_img)

        for start, end in ladders.items():
            self.place_image(start, end, self.ladder_img)

    def get_coords(self, pos):
        row = (100 - pos) // 10
        col = (pos - 1) % 10 if row % 2 == 0 else 9 - ((pos - 1) % 10)
        x = col * 60 + 10
        y = row * 60 + 10
        return x, y

    def place_image(self, start, end, img):
        x1, y1 = self.get_coords(start)
        x2, y2 = self.get_coords(end)
        mid_x = (x1 + x2) // 2
        mid_y = (y1 + y2) // 2
        self.canvas.create_image(mid_x, mid_y, image=img)

    def roll_dice(self):
        if self.player_pos >= 100:
            return
        roll = random.randint(1, 6)
        self.status_label.config(text=f"Dice rolled: {roll}")
        next_pos = self.player_pos + roll
        if next_pos > 100:
            return

        self.move_player(next_pos)

        if next_pos in snakes:
            self.status_label.config(text=f"Oh no! Snake from {next_pos} to {snakes[next_pos]}")
            self.move_player(snakes[next_pos])
        elif next_pos in ladders:
            self.status_label.config(text=f"Yay! Ladder from {next_pos} to {ladders[next_pos]}")
            self.move_player(ladders[next_pos])

        if self.player_pos == 100:
            self.status_label.config(text="🎉 You won the game!")

    def move_player(self, pos):
        self.player_pos = pos
        x, y = self.get_coords(pos)
        self.canvas.coords(self.player, x, y, x + 20, y + 20)

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeLadderGame(root)
    root.mainloop()
    import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=600, height=600)
canvas.pack()

# Load the image
snake_image = tk.PhotoImage(file="snake.png")  # Replace with your image file

# Place the image at coordinates (x, y)
canvas.create_image(x, y, image=snake_image, anchor='nw')

root.mainloop()
