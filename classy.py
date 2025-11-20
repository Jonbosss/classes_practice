from tkinter import *

root = Tk()
root.title('Classy')
root.geometry('400x400')


class Jonbosss:
    def __init__(self, master):
        myFrame = Frame(master)
        myFrame.pack()

        self.myButton = Button(master, text='Click Me!', command=self.clicker)
        self.myButton.pack(pady=20)

    def clicker(self):
        print("Look at you... You clicked a button!")


J = Jonbosss(root)

root.mainloop()
