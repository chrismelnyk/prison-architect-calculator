__author__ = 'chrismelnyk'
import tkinter as tk
from subprocess import call

laundry = 'laundry_gui.py'
workshop = 'workshop_gui.py'
kitchen = 'kitchen_canteen_gui.py'
intake = 'intake_interface.py'

def callpy1():
    call(['python', laundry] )

def callpy2():
    call(['python', workshop])

def callpy3():
    call(['python', workshop])

def callpy4():
    call(['python', intake])

root = tk.Tk()
img = tk.Image("photo", file="p_icon.png")
root.tk.call('wm','iconphoto', root._w, img)
root.geometry('400x400')
root.title('Prison Architect Calculator v0.1')
l1 = tk.Label(text="Prison Architect Calculator v0.1", fg="black", bg="white")

b1 = tk.Button(root, text='Laundry Calculator', command=callpy1, height=6, width=57).grid(row=0, column=1)
b2 = tk.Button(root, text='Workshop Calculator', command=callpy2, height=6, width=57).grid(row=1, column=1)
b3 = tk.Button(root, text='Kitchen/Canteen Calculator (WIP PROBABLY WILL NOT WORK)', command=callpy3, height=6, width=57).grid(row=2, column=1)
b4 = tk.Button(root, text='Prisoner Intake Guard Calculator', command=callpy4, height=6, width=57).grid(row=3, column=1)


root.mainloop()