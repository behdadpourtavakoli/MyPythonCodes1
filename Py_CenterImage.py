# Import required libraries
from tkinter import *
from PIL import ImageTk, Image

# Create an instance of tkinter window
win = Tk()

# Define the geometry of the window
win.geometry("700x500")

frame = Frame(win, width=600, height=400)
frame.pack()
frame.place(anchor="center", relx=0.5, rely=0.5)

# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open("Images/Python3.png"))

# Create a Label Widget to display the text or Image
label = Label(frame, image = img)
label.pack()

win.mainloop()
exit(0)

import tkinter as tk
from PIL import Image, ImageTk

# Create the main window
parent = tk.Tk()
parent.title("Image in Tkinter")

# Load and display an image 
#(replace 'your_logo.png' with the path to your image file)
image = Image.open('Images/Python3.png')
image = ImageTk.PhotoImage(image)

# Create a label to display the image
image_label = tk.Label(parent, image=image)
image_label.pack()

# Start the Tkinter event loop
parent.mainloop()
