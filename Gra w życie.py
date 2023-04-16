import tkinter as tk
import random as rnd


class Game:
    def __init__(self, size, num_alive, rules="23/3"):
        self.size = size
        self.rules = rules
        self.cells = [[False for x in range(size)] for y in range(size)]

        # Uzupełnienie tablicy komórek początkowo "żywymi" komórkami
        for z in rnd.sample(range(size * size), num_alive):
            self.cells[z % size][z // size] = True

    def update(self):
        # Aktualizacja stanu gry zgodnie z regułami gry "Gra w Życie"
        new_cells = [[False for x in range(self.size)] for y in range(self.size)]

        for x in range(self.size):
            for y in range(self.size):
                # Obliczenie liczby żywych sąsiadów
                num_alive_neighbors = 0
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if dx == 0 and dy == 0:
                            continue
                        if self.cells[(x + dx) % self.size][(y + dy) % self.size]:
                            num_alive_neighbors += 1

                # Aktualizacja stanu komórki na podstawie reguł gry
                if self.cells[x][y]:
                    # Reguły dla żywej komórki
                    rules_string = self.rules.split("/")[0]
                    if str(num_alive_neighbors) in rules_string:
                        new_cells[x][y] = True
                else:
                    # Reguły dla martwej komórki
                    rules_string = self.rules.split("/")[1]
                    if str(num_alive_neighbors) in rules_string:
                        new_cells[x][y] = True

        self.cells = new_cells


class GameView:
    def __init__(self, window, game, cell_size):
        self.window = window
        self.game = game
        self.cell_size = cell_size
        self.window.title("Gra w Życie")

        self.canvas = tk.Canvas(self.window, width=game.size * cell_size, height=game.size * cell_size)
        self.canvas.pack()

        self.rectangles = [[self.canvas.create_rectangle(x * cell_size, y * cell_size, cell_size * (x + 1),
                                                         cell_size * (y + 1), fill="white") for x in range(game.size)]
                           for y in range(game.size)]

    def draw(self):
        # Rysowanie komórek na ekranie
        for x in range(self.game.size):
            for y in range(self.game.size):
                if self.game.cells[x][y]:
                    self.canvas.itemconfig(self.rectangles[x][y], fill="black")
                else:
                    self.canvas.itemconfig(self.rectangles[x][y], fill="white")


class GameController:
    def __init__(self, game, view):
        self.game = game
        self.view = view

        self.window = view.window
        self.window.bind("<Key>", self.on_key_press)

        self.paused = False  # Dodanie atrybutu self.paused

    def run(self):
        # Pętla aktualizacji stanu gry i wyświetlania na ekranie
        while True:
            if not self.paused:  # Sprawdzenie, czy gra jest zatrzymana
                self.game.update()
                self.view.draw()
            else:  # Jeśli gra jest zatrzymana, wznów ją po jednej sekundzie
                self.window.after(1000, self.restart_game)
            self.window.update()

    def restart_game(self):
        # Wznowienie gry
        self.paused = False

    def on_key_press(self, event):
        # Obsługa naciśnięcia klawisza przez użytkownika
        if event.keysym == "space":
            # Zatrzymanie/wznowienie gry
            self.paused = not self.paused

def main():
    game = Game(size=50, num_alive=500)
    view = GameView(tk.Tk(), game, cell_size=15)
    controller = GameController(game, view)
    controller.run()



if '__main__' == __name__:
    main()
