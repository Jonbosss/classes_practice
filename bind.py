from tkinter import *

root = Tk()
root.title('Classy')
root.geometry('400x400')


def clicker():
    myLabel = Label(root, text='YOU DID IT!')
    myLabel.pack()


myButton = Button(root, text='Click Me!', command=clicker)
myButton.pack(pady=10)


root.mainloop()
