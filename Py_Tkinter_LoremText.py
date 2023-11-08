# Import required libraries
from tkinter import *
from tkinter import ttk
from lorem_text import lorem

# Create an instance of tkinter frame
win= Tk()

# Set the window size
win.geometry("700x350")

# Add a Text widget and insert some dummy text
text= Text(win, wrap= WORD, font= ('Courier 15 bold'))
text.insert(END,lorem.sentence())
text.place(x=20, y= 30, width= 400, height= 300)

frame1 = Frame(win)
frame1.place(x=100, y=33)

cmdb1 = Button(frame1, text="Wow")
cmdb1.pack()

win.mainloop()