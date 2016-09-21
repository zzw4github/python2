from Tkinter import *


class Menu1(Frame):
    def __init__(self, master):
        Frame.__init__(self,master)
        top = self.winfo_toplevel()

        self.mb = Menubutton(master, text='condiments', relief=RAISED)
        self.mb.grid(row=0, column=1)

        self.mb.menu = Menu(self.mb, tearoff=0)
        self.mb['menu'] = self.mb.menu

        self.mayoVar = IntVar()
        self.ketchVar = IntVar()
        self.mb.menu.add_checkbutton(label='mayo', variable=self.mayoVar)
        self.mb.menu.add_checkbutton(label='ketchup', variable=self.ketchVar)

        self.menu = Menu(master,title="menu1")
        top['menu'] = self.menu

        self.subMenu = Menu(self.menu)
        self.menu.add_cascade(label='Help', menu=self.subMenu)
        self.subMenu.add_command(label='About', command=self.__abouthandler)
        # self.pack()

        self.message = Message(master, bg='red', text='message\nmessage')
        self.message.grid(row=1, column=1)

        optionList = ('train', 'plain', 'boat')
        self.v = StringVar()
        self.v .set(optionList[0])
        self.om = OptionMenu(master,self.v, *optionList)
        self.om.grid(row=2,column=1)

        self.panedwindow = PanedWindow(master,width=300, height=400)
        self.panedwindow.grid(row=3, column=1)
        child1 = Message(master, bg='#ff00ff', text='message1\nmessage1')
        child2 = Message(master, bg='#ffeeff', text='message2\nmessage2')
        self.panedwindow.add(child1)
        self.panedwindow.add(child2, after=child1)

        self.male = Radiobutton(master, text="male")
        self.female = Radiobutton(master, text="female")
        self.male.grid(row=4, column=1)
        self.female.grid(row=4, column=2)

        self.scale = Scale(master, orient=HORIZONTAL )
        self.scale.grid(row=5, column=1)

    def __abouthandler(self):
        print "this is a menu"

root = Tk()
app = Menu1(root)

root.mainloop()