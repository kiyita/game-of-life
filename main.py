"""
Conway's Game of Life
Pyhton 3.11.0

à faire :
- créer tableau ok
- créer jolie grid ok
- afficher tableau dans jolie grid ok
- changer couleur cases ok
- fonction prend état en cours et calcul le suivant ok
- bouton pour cette fonction et afficher nouvel état ok
- cliquer sur case pour la remplir ok
- étendre les limites ? voir comment étendre la grille à l'infini peut etre abandonné le tableau et juste jouer avec les caese et coordonées
- bouton pause et start ok
- bouton vitesse ok (si trop grande vitesse bug my bad)
- bouton changer règles
"""
import tkinter as tk
from tkinter import ttk
import random

N = 10
CELL_SIZE = 25
DELAY = 1000
ONGOING_STATE = 0
INIT_SPEED = 500
SPEED = INIT_SPEED
INIT_OVERPOP = 3
INIT_UNDERPOP = 2
INIT_BIRTH = 3
OVERPOP = INIT_OVERPOP
UNDERPOP = INIT_UNDERPOP
BIRTH = INIT_BIRTH #à changer pour rendre possible le fait d'avoir plusieurs nombre de naissance

##Subfunction

def click_button():
    game_update()

def put_cell_clicked(x, y):
    x, y = x//CELL_SIZE, y//CELL_SIZE
    if grid[y][x] == 0 :
        grid[y][x] = 1
    else:
        grid[y][x] = 0
    update_grid_on_canvas()

def get_click_coordinates(event):
    x = event.x
    y = event.y
    put_cell_clicked(x, y)

def start_stop():
    global ONGOING_STATE
    ONGOING_STATE = 1 if ONGOING_STATE == 0 else 0
    if ONGOING_STATE:
        ongoing()

def ongoing():
    if ONGOING_STATE:
        game_update()
        window.after(int(SPEED), ongoing)

def action(event):
    global SPEED
    factor = listeCombo.get()
    print(factor)
    SPEED = INIT_SPEED // float(factor)

def change_underpop():
    global UNDERPOP
    UNDERPOP = int(underpop_input.get())
    print(UNDERPOP)

def change_overpop():
    global OVERPOP
    OVERPOP = int(overpop_input.get())
    print(OVERPOP)

def change_birth():
    global BIRTH
    BIRTH = int(birth_input.get())
    print(BIRTH)

def reset_settings():
    global UNDERPOP
    global OVERPOP
    global BIRTH
    UNDERPOP = INIT_UNDERPOP
    OVERPOP = INIT_OVERPOP
    BIRTH = INIT_BIRTH


##Main functions (minimal change)

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
    global ONGOING_STATE
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
                if UNDERPOP <= temp <= OVERPOP:
                    new_game_grid[row][column] = 1
            else:
                if temp == BIRTH:
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
    window.canvas.bind("<Button-1>", get_click_coordinates)
    window.mainloop()


##Working method for window, buttons and inputs
# Create the main window
window = tk.Tk()
window.title("Conway's Game of Life")

# Create buttons for start/stop and next step
button_next = tk.Button(window, text="Next step", command=click_button)
button_next.pack()

button_start_stop = tk.Button(window, text="Play/Stop", command=start_stop)
button_start_stop.pack()

button_reset = tk.Button(window, text="reset settings", command=reset_settings)
button_reset.pack()

#Create checklist for speed
labelSpeed = tk.Label(window, text = "Choisissez une vitesse")
labelSpeed.pack()

listeSpeed=[1, 2, 3, 0.5]

listeCombo = ttk.Combobox(window, values=listeSpeed)

listeCombo.current(0)

listeCombo.pack()
listeCombo.bind("<<ComboboxSelected>>", action)

#Create input user
underpop = tk.IntVar()
underpop_input = tk.Entry(window, textvariable=underpop)
underpop_input.pack()

button_underpop = tk.Button(window, text="change underpop", command=change_underpop)
button_underpop.pack()


overpop = tk.IntVar()
overpop_input = tk.Entry(window, textvariable=overpop)
overpop_input.pack()

button_overpop = tk.Button(window, text="change overpop", command=change_overpop)
button_overpop.pack()


birth = tk.IntVar()
birth_input = tk.Entry(window, textvariable=birth)
birth_input.pack()

button_birth = tk.Button(window, text="change birth", command=change_birth)
button_birth.pack()



if __name__ == "__main__":
    main()




















