import tkinter as Tk
from functools import partial

def square(x):
    print("munyi")
    return x*x

root = Tk.Tk()
var = Tk.IntVar(root, value=0) #the variable the gets passed to the class call
menu = Tk.OptionMenu(root, var, *[0,1,2,3,4,5]) #a drop-down list to choose a value for the variable
menu.pack()
button = Tk.Button(root, text='click', command = partial(square,var.get())) #a button that calls the class
button.pack()
root.mainloop()