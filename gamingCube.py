import random
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os

def randomize():
    cubeValue = random.randint(1,6)
    print(cubeValue)
    match cubeValue:
        case 1:
            l0.pack_forget()
            l2.pack_forget()
            l3.pack_forget()
            l4.pack_forget()
            l5.pack_forget()
            l6.pack_forget()
            l1.pack()
        case 2:
            l0.pack_forget()
            l1.pack_forget()
            l3.pack_forget()
            l4.pack_forget()
            l5.pack_forget()
            l6.pack_forget()
            l2.pack()
        case 3:
            l0.pack_forget()
            l1.pack_forget()
            l2.pack_forget()
            l4.pack_forget()
            l5.pack_forget()
            l6.pack_forget()
            l3.pack()
        case 4:
            l0.pack_forget()
            l1.pack_forget()
            l2.pack_forget()
            l3.pack_forget()
            l5.pack_forget()
            l6.pack_forget()
            l4.pack()
        case 5:
            l0.pack_forget()
            l1.pack_forget()
            l2.pack_forget()
            l3.pack_forget()
            l4.pack_forget()
            l6.pack_forget()
            l5.pack()
        case 6:
            l0.pack_forget()
            l1.pack_forget()
            l2.pack_forget()
            l3.pack_forget()
            l4.pack_forget()
            l5.pack_forget()
            l6.pack()
        case _:
            l1.pack_forget()
            l2.pack_forget()
            l3.pack_forget()
            l4.pack_forget()
            l5.pack_forget()
            l6.pack_forget()
            l0.pack()

scriptDir = os.path.dirname(__file__)


root = Tk()
root.geometry('200x200')

buttonFrame = ttk.Frame(root)
buttonFrame.pack(side=BOTTOM)

#images
e = Image.open(os.path.join(scriptDir, 'pictures/e.png'))
c1 = Image.open(os.path.join(scriptDir, 'pictures/1.png'))
c2 = Image.open(os.path.join(scriptDir, 'pictures/2.png'))
c3 = Image.open(os.path.join(scriptDir, 'pictures/3.png'))
c4 = Image.open(os.path.join(scriptDir, 'pictures/4.png'))
c5 = Image.open(os.path.join(scriptDir, 'pictures/5.png'))
c6 = Image.open(os.path.join(scriptDir, 'pictures/6.png'))

ei = ImageTk.PhotoImage(e)
ci1 = ImageTk.PhotoImage(c1)
ci2 = ImageTk.PhotoImage(c2)
ci3 = ImageTk.PhotoImage(c3)
ci4 = ImageTk.PhotoImage(c4)
ci5 = ImageTk.PhotoImage(c5)
ci6 = ImageTk.PhotoImage(c6)

l0 = Label(root, image=ei)
l1 = Label(root, image=ci1)
l2 = Label(root, image=ci2)
l3 = Label(root, image=ci3)
l4 = Label(root, image=ci4)
l5 = Label(root, image=ci5)
l6 = Label(root, image=ci6)

button = ttk.Button(buttonFrame, text='Play', command=lambda : randomize())
button.pack()

mainloop()