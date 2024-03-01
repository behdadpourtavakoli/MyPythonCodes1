import tkinter as tk

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

myapp = App()
myapp.master.title('Tkinter Pack Layout')

intWidth = 550
intHeight = 300
myapp.master.minsize(intWidth, intHeight)
myapp.master.maxsize(1024, 768)

screen_width = myapp.master.winfo_screenwidth()
screen_height = myapp.master.winfo_screenheight()
inyPosX = (screen_width / 2) - (intWidth / 2)
intPosY = (screen_height / 2) - (intHeight / 2)
myapp.master.geometry("%dx%d+%d+%d" % (intWidth, intHeight, inyPosX, intPosY))

label1 = tk.Label(master=myapp.master, text='Tkinter',bg='red',fg='white').pack(side=tk.TOP)
label2 = tk.Label(master=myapp.master,text='Pack Layout',bg='green', fg='white').pack(side=tk.TOP)
label3 = tk.Label(master=myapp.master, text='Demo',bg='blue', fg='white').pack(side=tk.TOP)

myapp.master.mainloop()
exit(0)

from tkinter import *

class simpledialog(object):
    def __init__(self, parent):
        # The "return value" of the dialog,
        # entered by user in self.entry Entry box.
        self.data = None

        self.root=Toplevel(parent)
        self.entry = Entry(self.root)
        self.entry.pack()
        self.ok_btn = Button(self.root, text="ok", command=self.ok)
        self.ok_btn.pack()

        # Modal window.
        # Wait for visibility or grab_set doesn't seem to work.
        self.root.wait_visibility()   # <<< NOTE
        self.root.grab_set()          # <<< NOTE
        self.root.transient(parent)   # <<< NOTE

        self.parent = parent

    def ok(self):
        self.data = self.entry.get()
        self.root.grab_release()      # <<< NOTE
        self.root.destroy()

class MainWindow:
    def __init__(self, window):
        window.geometry('600x400')
        Button(window, text='popup', command=self.popup).pack()
        Button(window, text='quit', command=self.closeme).pack()
        self.window = window
        window.bind('<Key>', self.handle_key)

    def handle_key(self, event):
        k = event.keysym
        print(f"got k: {k}")

    def popup(self):
        d = simpledialog(self.window)
        print('opened login window, about to wait')
        self.window.wait_window(d.root)   # <<< NOTE
        print('end wait_window, back in MainWindow code')
        print(f'got data: {d.data}')

    def closeme(self):
        self.window.destroy()

root = Tk()
app = MainWindow(root)
root.mainloop()
print('exit main loop')