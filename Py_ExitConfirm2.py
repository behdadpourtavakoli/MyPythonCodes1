import tkinter as tk
##_______________EXIT_______________
def closeyes():
    exit()
def closeno():
    exitsure.destroy()
def close_window():
    exitsure = tk.Tk()
    areyousure = tk.Label(text="Are you sure you want to exit?")
    areyousure.grid(column=0, row=0)
    ExitYes = tk.Button(text="Yes", command = closeyes)
    ExitYes.grid(column=0, row=2)
    ExitNo = tk.Button(text="No", command = closeno)
    ExitNo.grid(column=2, row=2)
    exitsure.mainloop()
#_______________START_______________
start = tk.Tk()
start.title("THE MEGA POP QUIZ")
#Start Title
start_title = tk.Label(text="Welcome to THE MEGA POP QUIZ")
start_title.grid(column=0, row=1)
#Begin button
def BEGIN():
    start.destroy()
Button1 = tk.Button(text="BEGIN", command = BEGIN)
Button1.grid(column=0, row=2)
#Exit
ExitButton = tk.Button(text="EXIT", width = 14, command = close_window)
ExitButton.grid(column=0, row=0)
start.mainloop()