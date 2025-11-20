from tkinter import *

root = Tk()
root.title('Classy')
root.geometry('400x400')

# Event types <Enter>, <Leave>, <Button-1,2,3>(mouse buttons), <FocusIn>, <FocusOut>, <Return>(Enter Button), <Key> (any keyboard key)


def clicker(event):
    myLabel = Label(root, text='You clicked this button: ' + event.char)
    myLabel.pack()


myButton = Button(root, text='Click Me!', command=clicker)
myButton.bind('<Key>', clicker)
myButton.pack(pady=10)


root.mainloop()
