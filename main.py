"""
Conway's Game of Life
Pyhton 3.11.0

à faire :
- créer tableau ok
- créer jolie grid ok
- afficher tableau dans jolie grid ok
- changer couleur cases ok
- fonction prend état en cours et calcul le suivant ok
- bouton pour cette fonction et afficher nouvel état
- cliquer sur case pour la remplir
- bouton pause et start
- bouton vitesse
- bouton changer règles
"""
import tkinter as tk
import random

N = 10
CELL_SIZE = 25
DELAY = 1000
LISTE = []

#TEST
def click_button():
    print("Bouton cliqué !")
    game_update()

def get_cell_clicked(x, y):
    x, y = x//CELL_SIZE, y//CELL_SIZE
    if grid[x][y] == 0 :
        grid[x][y] = 1
    else:
        grid[x][y] = 0
    update_grid_on_canvas()

def get_click_coordinates(event):
    x = event.x
    y = event.y
    get_cell_clicked(x, y)

#TEST fin


def new_grid():
    """Create a grid of size N x N filled with zeros"""
    return [[0 for _ in range(N)] for _ in range(N)]

def show_grid(grid):
    """Display the grid on the Tkinter canvas"""
    window.canvas = tk.Canvas(window, width=N*CELL_SIZE, height=N*CELL_SIZE, borderwidth=0, highlightthickness=0)
    window.canvas.pack(side="top", fill="both", expand="true")
    window.cellwidth = CELL_SIZE
    window.cellheight = CELL_SIZE

    window.rect = {}
    for column in range(N):
        for row in range(N):
            x1 = column * window.cellwidth
            y1 = row * window.cellheight
            x2 = x1 + window.cellwidth
            y2 = y1 + window.cellheight

            color = "pink" if grid[row][column] == 1 else "white"
            window.rect[row, column] = window.canvas.create_rectangle(x1, y1, x2, y2, fill=color, tags="rect")

def game_update():
    """Update the game grid according to Conway's rules"""
    global grid
    new_game_grid = new_grid()
    for row in range(N):
        for column in range(N):
            temp = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if (i != 0 or j != 0) and 0 <= row + i < N and 0 <= column + j < N:
                        if grid[row + i][column + j] == 1:
                            temp += 1
            if grid[row][column] == 1:
                if temp in [2, 3]:
                    new_game_grid[row][column] = 1
            else:
                if temp == 3:
                    new_game_grid[row][column] = 1

    grid = new_game_grid
    update_grid_on_canvas()

def update_grid_on_canvas():
    """Update the canvas to reflect the updated grid"""
    for column in range(N):
        for row in range(N):
            color = "pink" if grid[row][column] == 1 else "white"
            window.canvas.itemconfig(window.rect[row, column], fill=color)

def main():
    global grid
    grid = new_grid()
    grid[2][2] = 1
    grid[1][2] = 1
    grid[3][2] = 1
    show_grid(grid)
    window.bind("<Button-1>", get_click_coordinates)
    window.mainloop()

# Create the main window
window = tk.Tk()
window.title("Conway's Game of Life")

# Création du bouton
bouton = tk.Button(window, text="Next step", command=click_button)
bouton.pack()

if __name__ == "__main__":
    main()




















