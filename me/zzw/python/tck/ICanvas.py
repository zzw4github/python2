from Tkinter import *


class ICanvas:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        self.canvas = Canvas(
            frame
        )
        self.canvas.pack(side=LEFT)
        self.canvas.create_arc(10,10,200,200)


root = Tk()

app = ICanvas(root)

root.mainloop()
# root.destroy() # optional; see description below
