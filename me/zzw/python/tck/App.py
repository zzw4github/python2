from Tkinter import *
from tkMessageBox import *


class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        self.button = Button(
            frame, text="QUIT", fg="red", command=frame.quit
        )
        self.button.pack(side=LEFT)

        self.hi_there = Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=LEFT)

        self.new_frame = Button(frame, text="new frame", command=self.new_frame)
        self.new_frame.pack(side=LEFT)

        self.listbox = Listbox(frame, width=50, activestyle='dotbox',listvariable='listCon')
        self.listbox.pack()
        self.listbox.insert(0,"abc")
        self.listbox.insert(1,"def")



        #self.menu.pack()

    def say_hi(self):
        print "hi there, everyone!"

    def new_frame(self):
        root1 = Tk()
        frame1 = Frame(root1)
        frame1.pack()
        self.button = Button(
            frame1, text="QUIT", fg="red", command=frame1.quit
        )
        self.button.pack(side=LEFT)


root = Tk()
app = App(root)
root.mainloop()
root.destroy() # optional; see description below
