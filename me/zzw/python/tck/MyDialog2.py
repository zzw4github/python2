import tkSimpleDialog
from Tkinter import *


class MyDialog2(tkSimpleDialog.Dialog):

    def body(self, master):
        Label(master, text="First:").grid(row=0, sticky=W)
        Label(master, text="Second:").grid(row=1, sticky=W)

        self.e1 = Entry(master,bg="red",fg="black")
        self.e2 = Entry(master)

        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)

        self.cb = Checkbutton(master, text="Hardcopy")
        self.cb.grid(row=2, columnspan=2, sticky=W)

        self.entry = Entry(master, width=10)
        self.entry.grid(row=3, sticky=E+W)
        self.entryScroll = Scrollbar(master, orient=HORIZONTAL, command=self.__scrollHandler)
        self.entryScroll.grid(row=4, sticky=E+W)
        self.entry['xscrollcommand'] = self.entryScroll.set

    def apply(self):
        first = int(self.e1.get())
        second = int(self.e2.get())
        print first, second

    def __scrollHandler(self, *L):
        op, howMany = L[0], L[1]
        if op == 'scroll':
            units = L[2]
            self.entry.xview_scroll(howMany, units)
        elif op == 'moveto':
            self.entry.xview_moveto(howMany)

root = Tk()
d = MyDialog2(root)
d.mainloop()





