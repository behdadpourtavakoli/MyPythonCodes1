from tkinter import *
import random as rm
import time
import keyboard as kb

# Creating the window and the canvas
root = Tk()
root.geometry("390x390")
root.resizable(False, False)

c = Canvas(root, width=390, height=390, bg="white")
c.pack()

#Creating lists of all possible x and y coordinates
board = []
for i in range(39):
    for j in range(39):
        board.append([i, j])

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
        self.body_cords.append(self.head_cords)

        # Moving the head according to the Snake direction
        if self.direction == "up":
            self.head_cords[1] = self.head_cords[1] - 1
        if self.direction == "down":
            self.head_cords[1] = self.head_cords[1] + 1
        if self.direction == "left":
            self.head_cords[0] = self.head_cords[0] - 1
        if self.direction == "right":
            self.head_cords[0] = self.head_cords[0] + 1

    def check_dead(self):
        # Creating the function to check if the Snake is dead basing on 2 conditions:

        # 1: If the Snake hits the wall
        if self.head_cords[0] > 39 or self.head_cords[0] < 1 or self.head_cords[1] > 39 or self.head_cords[1] < 1:
            return True
        # 2: If the Snake hits itself
        elif self.head_cords in self.body_cords:
            return True
        else:
            return False

    def grow(self):
        # Creating the growth function (it will be called if the Snake eats an Apple)
        self.body_cords.insert(0, [self.body_cords[0][0], self.body_cords[0][1]])

Jordan = Snake()    # Creating an instance of the Snake class


# Creating the Apple class
class Apple:
    def __init__(self):
        # Initializating the x and the y coordinates


        # To place the Apple somewhere on the board, we should check which cells are already occupied by the Snake
        snake_positions = []
        for pos in Jordan.body_cords:
            snake_positions.append(pos)
        snake_positions.append(Jordan.head_cords)


        # Then we choose which cells are not occupied by the Snake
        possinle_positions = []
        for pos in board:
            if pos in snake_positions:
                pass
            else:
                possinle_positions.append(pos)

        # And choose one of them randomly
        rm.choice(possinle_positions)
        self.pos = rm.choice(possinle_positions)

    def check_eaten(self):
        # Creating the function to check if the Apple it eaten by the Snake
        if Jordan.head_cords == self.pos:
            return True
        else:
            return False

    def __del__(self):
        # Creating the Apple delete function
        print("+1 Apple")



nessy = Apple()    # Creating an instance of the Apple class


# Creating the visualization function
def visualizate():

    # Clearing everything
    c.create_rectangle(0, 0, 390, 390, fill="white")

    # Visualizing the Snake

    # Head
    c.create_rectangle(Jordan.head_cords[0]*10-9, Jordan.head_cords[0]*10, Jordan.head_cords[1]*10-9, Jordan.head_cords[1]*10,
                       fill="yellow", outline="black", width=2)
    # Body
    for block in Jordan.body_cords:
        c.create_rectangle(block[0]*10-9, block[0]*10, block[1]*10-9, block[1]*10, fill="yellow", outline="white", width=2)

    # Visualizing the Apple
    c.create_rectangle(nessy.pos[0]*10-9, nessy.pos[0]*10, nessy.pos[1]*10-9, nessy.pos[1]*10, fill="red", outline="black", width=1)




# Creating the contlors

# If you are from stackoverflow - ignore the controls. They do nothing now
def change_direction(id):
    if id == 1:
        Jordan.direction = "up"
    if id == 2:
        Jordan.direction = "down"
    if id == 3:
        Jordan.direction = "left"
    if id == 4:
        Jordan.direction = "right"

kb.add_hotkey("up", change_direction(1))
kb.add_hotkey("down", change_direction(2))
kb.add_hotkey("left", change_direction(3))
kb.add_hotkey("right", change_direction(4))



# The game cycle
while True:
    visualizate()    # Visualizing what we have

    # Checking if the Snake is dead
    if Jordan.check_dead():
        time.sleep(5)
        root.destroy()    #Closing 
        print("You died")
        break


    # Checking if the Apple is eaten
    if nessy.check_eaten():
        del nessy
        Jordan.grow()
        nessy = Apple()

    Jordan.move()

    print("move")
    time.sleep(1)

root.mainloop()