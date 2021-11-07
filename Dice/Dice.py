import tkinter
from PIL import Image, ImageTk
import random

#Create tkinter window 
root = tkinter.Tk()
root.geometry('400x400')
root.title('Roll Dice')

#take and draw a random image
dice = ['die1.png', 'die2.png', 'die3.png', 'die4.png', 'die5.png', 'die6.png']
image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))


label1 = tkinter.Label(root, image=image1)
label2 = tkinter.Label(root, image=image2)

label1.image = image1
label2.image = image2
label1.pack(side=tkinter.LEFT)
label2.pack(side=tkinter.RIGHT)


def roll_dice():
    image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

    label1.configure(image=image1)

    label1.image = image1

    image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

    label2.configure(image=image2)

    label2.image = image2


button = tkinter.Button(root, text='roll dice', foreground='green', command=roll_dice)


button.pack()

root.mainloop()
