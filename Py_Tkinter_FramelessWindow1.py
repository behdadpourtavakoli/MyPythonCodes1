from tkinter import Tk, Canvas, PhotoImage, NW

root = Tk()

root.attributes('-transparentcolor','#f0f0f0')

# Canvas
canvas = Canvas(root, width=450, height=600)
canvas.pack()

# Image
img = PhotoImage(file="images/panda1.png")

# Positioning the Image inside the canvas
canvas.create_image(0, 0, anchor=NW, image=img)

# Starts the GUI
root.mainloop()