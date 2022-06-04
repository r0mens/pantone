from tkinter import *
from threading import Thread
import time


def flashing():
    while True:
        butt.config(bg = 'red')
        time.sleep(0.2)
        butt.config(bg = 'green')
        time.sleep(0.2)


root = Tk()
root.geometry("200x200+300+100")
butt = Button(root, text = 'мигающая кнопка')
butt.pack()
Thread(target = flashing, args = [], daemon = True).start()
root.mainloop()
