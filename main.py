"""
Conway's Game of Life
Pyhton 3.11.0
By Kiyita
Started on 27/06/24
"""


import tkinter as tk
from tkinter import ttk
import random


##Global variables

GRID_SIZE = 10
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
    return [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

def show_grid(grid):
    """Display the grid on the Tkinter canvas"""
    window.canvas = tk.Canvas(window, width=GRID_SIZE*CELL_SIZE, height=GRID_SIZE*CELL_SIZE, borderwidth=0, highlightthickness=0)
    window.canvas.pack(side="top", fill="both", expand="true")
    window.cellwidth = CELL_SIZE
    window.cellheight = CELL_SIZE

    window.rect = {}
    for column in range(GRID_SIZE):
        for row in range(GRID_SIZE):
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
    for row in range(GRID_SIZE):
        for column in range(GRID_SIZE):
            temp = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if (i != 0 or j != 0) and 0 <= row + i < GRID_SIZE and 0 <= column + j < GRID_SIZE:
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
    for column in range(GRID_SIZE):
        for row in range(GRID_SIZE):
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
window.configure(bg='pink')
window.title("Conway's Game of Life")

# Create buttons for start/stop and next step
button_next = tk.Button(window, text="Next step", command=click_button, activebackground='red')
button_next.pack(pady= 5, padx= 5)

button_start_stop = tk.Button(window, text="Play/Stop", command=start_stop, activebackground='orange')
button_start_stop.pack(pady= 5, padx= 5)

button_reset = tk.Button(window, text="reset settings", command=reset_settings, activebackground='yellow')
button_reset.pack(pady= 5, padx= 5)

#Create checklist for speed
labelSpeed = tk.Label(window, text = "Choisissez une vitesse")
labelSpeed.pack(pady= 5, padx= 5)

listeSpeed=[1, 2, 3, 0.5]

listeCombo = ttk.Combobox(window, values=listeSpeed)

listeCombo.current(0)

listeCombo.pack(pady= 5, padx= 5)
listeCombo.bind("<<ComboboxSelected>>", action)

#Create input user
underpop = tk.IntVar()
underpop_input = tk.Entry(window, textvariable=underpop)
underpop_input.pack(pady= 5, padx= 5)

button_underpop = tk.Button(window, text="change underpop", command=change_underpop, activebackground='green')
button_underpop.pack(pady= 5, padx= 5)


overpop = tk.IntVar()
overpop_input = tk.Entry(window, textvariable=overpop)
overpop_input.pack(pady= 5, padx= 5)

button_overpop = tk.Button(window, text="change overpop", command=change_overpop, activebackground='blue')
button_overpop.pack(pady= 5, padx= 5)


birth = tk.IntVar()
birth_input = tk.Entry(window, textvariable=birth)
birth_input.pack(pady= 5, padx= 5)

button_birth = tk.Button(window, text="change birth", command=change_birth, activebackground='purple')
button_birth.pack(pady= 5, padx= 5)



if __name__ == "__main__":
    main()




















