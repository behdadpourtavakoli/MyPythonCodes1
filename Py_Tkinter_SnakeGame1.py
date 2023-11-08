## from tkinter import *
## import tkinter
## screen = Tk()
## screen.title("My GUI")
## screen.geometry("600x600")
## screen.configure(background="Gray")
## frame_enabled = False
## def toggle_frame():
##     global frame_enabled
##     if not frame_enabled:
##         my_frame.pack(fill='both', expand=True)
##     else:
##         my_frame.pack_forget()
##     frame_enabled = not frame_enabled
## button1 = Button(screen, text="Toggle frame", command=toggle_frame)
## button1.pack()
## my_frame = Frame(screen, bg="red")
## screen.mainloop()
## exit(0)

import tkinter as tk  # PE8: `import *` is not preferred
import random
import time

# --- classes ---  # PEP8: all classes directly after imports
# Creating the Snake class
class Snake:
    def __init__(self):
        # Initializating:
        self.head_cords = [20, 20]    # A list that contains the x and the y coordinate of the Snake head
        self.body_cords = [[17, 20], [18, 20], [19, 20]]    # A list with smaller lists with coordinates of each Snake block
        self.direction = "right"    # The directions the Snake is facing
        self.lenght = 4    # The Snake length (Not the game score, that is the number of eaten Apples, but the number of the Snake blocks + 1 for the head)
    def move(self):
        # Creating the movement function
        # Movineg the body
        self.body_cords.pop(0)
        self.body_cords.append(self.head_cords.copy())
        # Moving the head according to the Snake direction
        if self.direction == "up":
            self.head_cords[1] -= 1    # shorter with `-=` / `+=`
        if self.direction == "down":
            self.head_cords[1] += 1    # shorter with `-=` / `+=`
        if self.direction == "left":
            self.head_cords[0] -= 1    # shorter with `-=` / `+=`
        if self.direction == "right":
            self.head_cords[0] += 1    # shorter with `-=` / `+=`
    def check_dead(self):
        # Creating the function to check if the Snake is dead basing on 2 conditions:
        # 1: If the Snake hits the wall
        if self.head_cords[0] > 39 or self.head_cords[0] < 1 or self.head_cords[1] > 39 or self.head_cords[1] < 1:
            print('collide wall')
            return True
        # 2: If the Snake hits itself
        elif self.head_cords in self.body_cords:
            print('collide itself')
            return True
        else:
            return False
    def grow(self):
        # Creating the growth function (it will be called if the Snake eats an Apple)
        self.body_cords.insert(0, [self.body_cords[0][0], self.body_cords[0][1]])
    def change_direction(self, direction):
        self.direction = direction
        
# Creating the Apple class
class Apple:
    def __init__(self):
        # Initializating the x and the y coordinates
        # To place the Apple somewhere on the board, we should check which cells are already occupied by the Snake
        snake_positions = []
        for pos in jordan.body_cords:
            snake_positions.append(pos)
        snake_positions.append(jordan.head_cords)
        # Then we choose which cells are not occupied by the Snake
        possinle_positions = []
        for pos in board:
            if pos not in snake_positions:
                possinle_positions.append(pos)
        # And choose one of them randomly
        self.pos = random.choice(possinle_positions)
    def check_eaten(self):
        # Creating the function to check if the Apple it eaten by the Snake
        #if jordan.head_cords == self.pos:
        #    return True
        #else:
        #    return False
        return (jordan.head_cords == self.pos)  # `==` gives `True` or `False`
    def __del__(self):
        # Creating the Apple delete function
        print("+1 Apple")

# --- functions ---  # PEP8: all functions directly after classes
# Creating the visualization function
def visualizate():
    # Clearing everything
    #c.create_rectangle(0, 0, 390, 390, fill="white")
    c.delete('all')
    
    # Visualizing the Snake
    # Head
    x = jordan.head_cords[0]*10
    y = jordan.head_cords[1]*10
    c.create_rectangle(x-9, y-9, x, y, fill="green", outline="black", width=2)
    
    # Body
    for block in jordan.body_cords:
        x = block[0]*10
        y = block[1]*10
        c.create_rectangle(x-9, y-9, x, y, fill="yellow", outline="white", width=2)
    # Visualizing the Apple
    x = nessy.pos[0]*10
    y = nessy.pos[1]*10
    c.create_rectangle(x-9, y-9, x, y, fill="red", outline="black", width=1)
# --- main ---
# Creating the window and the canvas
root = tk.Tk()
root.geometry("390x390")
root.resizable(False, False)
c = tk.Canvas(root, width=390, height=390, bg="white")
c.pack()
# Creating lists of all possible x and y coordinates
board = []
for i in range(39):
    for j in range(39):
        board.append([i, j])
jordan = Snake()  # Creating an instance of the Snake class  # PEP8: `CamelCaseNames` only for classes - it helps to recognize class in code
nessy  = Apple()  # Creating an instance of the Apple class

root.bind("up", lambda event:jordan.change_direction("up"))
root.bind("down", lambda event:jordan.change_direction("down"))
root.bind("left", lambda event:jordan.change_direction("left"))
root.bind("right", lambda event:jordan.change_direction("right"))
# The game cycle
while True:
    visualizate()    # Visualizing what we have
    print('check snake')
    # Checking if the Snake is dead
    if jordan.check_dead():
        print("You died")
        root.update()
        time.sleep(5)
        root.destroy()    # Closing 
        break
    print('check apple')
    # Checking if the Apple is eaten
    if nessy.check_eaten():
        del nessy
        jordan.grow()
        nessy = Apple()
    print("move")
    jordan.move()
    root.update()   # allow `mainloop()` to update window
    time.sleep(0.5)
#root.mainloop()  # no need if you use `root.update()`