import tkinter as tk

root = tk.Tk()
b = tk.Button(root, text="Example")

def move(i):
    if i<=50:
        b.place(x=i, y=i)
        b.after(20, lambda: move(i)) #after every 100ms
        i = i+1

move(0) #Start animation instantly
root.mainloop()