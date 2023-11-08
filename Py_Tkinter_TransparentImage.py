from tkinter import Tk, Canvas, PhotoImage, NW
from PIL import Image

root = Tk()

root.attributes('-transparentcolor','#f0f0f0')

# Canvas
canvas = Canvas(root, width=450, height=600)
canvas.pack()

im = Image.open("Images/Panda1.png")

img = im.convert("RGBA")

width = img.size[0] 
height = img.size[1] 
for x in range(0,width):# process all pixels
    for y in range(0,height):
        data = img.getpixel((x, y))
        if (data[0] == 255 and data[1] == 255 and data[2] == 255 ):
            img.putpixel((x, y), (255, 255, 255, 0))

canvas.create_image(0, 0, anchor=NW, image=img)
root.mainloop()

exit(0)



root.attributes('-transparentcolor','#f0f0f0')

# Canvas
canvas = Canvas(root, width=450, height=600)
canvas.pack()

# Image
img = PhotoImage(file="Images/Python3.png")

# Positioning the Image inside the canvas
canvas.create_image(0, 0, anchor=NW, image=img)

# Starts the GUI
root.mainloop()