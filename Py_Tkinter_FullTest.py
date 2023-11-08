from tkinter import *

## example 1
root = Tk()  # create a root widget
root.title("Tk Example")
root.configure(background="yellow")
root.minsize(200, 200)  # width, height
root.maxsize(500, 500)
root.geometry("300x300+50+50")  # width x height + x + y
root.mainloop()

## example 2
root = Tk()
root.title("Tk Example")
root.minsize(200, 200)  # width, height
root.geometry("300x300+50+50")

# Create Label in our window
text = Label(root, text="Nothing will work unless you do.")
text.pack()
text2 = Label(root, text="- Maya Angelou")
text2.pack()
root.mainloop()

## example 3
root = Tk()
root.title("Tk Example")
root.minsize(200, 200)  # width, height
root.geometry("300x300+50+50")

# Create Label in our window
image = PhotoImage(file="Images/Pokémon_Pikachu_art.png")
img = Label(root, image=image)
img.pack()
root.mainloop()

