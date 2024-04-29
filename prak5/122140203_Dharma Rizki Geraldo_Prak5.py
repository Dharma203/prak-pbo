import tkinter
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (192, 192, 192)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

ROWS = 25
COLS = 25
CELL_SIZE = SCREEN_WIDTH // COLS

EMPTY = 0
BOMB_STATE = 1
NUMBER = 2

class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.rect = (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        self.state = EMPTY
        self.output = False
        self.flagged = False

    def draw(self, canvas):
        if not self.output:
            canvas.create_rectangle(self.rect, fill=GRAY)
            if self.flagged:
                canvas.create_text(self.rect[0] + CELL_SIZE // 2, self.rect[1] + CELL_SIZE // 2, text="F", fill="red")
        else:
            canvas.create_rectangle(self.rect, fill=WHITE)
            if self.state == BOMB_STATE:
                canvas.create_rectangle(self.rect, fill=RED)
            elif self.state == NUMBER:
                canvas.create_text(self.rect[0] + CELL_SIZE // 2, self.rect[1] + CELL_SIZE // 2, text=self.bombs_nearby, fill=BLUE)

class BombCell(Cell):
    def __init__(self, row, col):
        super().__init__(row, col)
        self.state = BOMB_STATE

class NumberCell(Cell):
    def __init__(self, row, col, bombs_nearby):
        super().__init__(row, col)
        self.state = NUMBER
        self.bombs_nearby = bombs_nearby

class Minesweeper:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("Mine Sweeper")
        self.canvas = tkinter.Canvas(self.window, width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.canvas.pack()
        self.running = True
        self.game_over = False
        self.grid = [[Cell(row, col) for col in range(COLS)] for row in range(ROWS)]
        self.place_bombs()
        self.calculate_numbers()
        self.canvas.bind("<Button-1>", self.control)  
        self.canvas.bind("<Button-3>", self.control)  

    def place_bombs(self):
        bomb_count = COLS * ROWS // 6
        for _ in range(bomb_count):
            row = random.randint(0, ROWS - 1)
            col = random.randint(0, COLS - 1)
            while isinstance(self.grid[row][col], BombCell):
                row = random.randint(0, ROWS - 1)
                col = random.randint(0, COLS - 1)
            self.grid[row][col] = BombCell(row, col)

    def calculate_numbers(self):
        for row in range(ROWS):
            for col in range(COLS):
                if not isinstance(self.grid[row][col], BombCell):
                    bombs_nearby = sum(1 for dr in (-1, 0, 1) for dc in (-1, 0, 1)
                                       if 0 <= row + dr < ROWS and 0 <= col + dc < COLS
                                       and isinstance(self.grid[row + dr][col + dc], BombCell))
                    if bombs_nearby > 0:
                        self.grid[row][col] = NumberCell(row, col, bombs_nearby)

    def reveal_cell(self, row, col):
        cell = self.grid[row][col]
        if not cell.output and not cell.flagged:
            cell.output = True
            if cell.state == EMPTY:
                for dr in (-1, 0, 1):
                    for dc in (-1, 0, 1):
                        if 0 <= row + dr < ROWS and 0 <= col + dc < COLS:
                            self.reveal_cell(row + dr, col + dc)

    def toggle_flag(self, row, col):
        cell = self.grid[row][col]
        if not cell.output:
            cell.flagged = not cell.flagged

    def check_win(self):
        for row in range(ROWS):
            for col in range(COLS):
                if not isinstance(self.grid[row][col], BombCell) and not self.grid[row][col].output:
                    return False
        return True

    def control(self, event):
        if not self.game_over:
            x = event.x // CELL_SIZE
            y = event.y // CELL_SIZE
            if event.num == 1:  
                self.reveal_cell(y, x)
            elif event.num == 3:  
                self.toggle_flag(y, x)
            if self.check_win():
                self.game_over = True
                print("You win!")
        else:
            print("Game over!")

    def draw(self):
        self.canvas.delete("all")
        for row in self.grid:
            for cell in row:
                cell.draw(self.canvas)
                if self.game_over and isinstance(cell, BombCell) and cell.state == BOMB_STATE:
                    self.canvas.create_rectangle(cell.rect, fill=RED)
        if self.game_over:
            self.canvas.create_text(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, text="Game Over", fill="black")
        self.window.after(100, self.draw) 

    def run(self):
        self.window.after(100, self.draw)
        self.window.mainloop()

def main():
    game = Minesweeper()
    game.run()

if __name__ == "__main__":
    main()