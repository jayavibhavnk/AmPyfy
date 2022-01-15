import random
from tkinter import *

import threading

root=Tk()

root.geometry("640x520")
root.configure(background = '#AFAFAF')

lb1=Label(root,background='#AFAFAF',text="amPYfy",font=("Calibri Bold",50,"underline"))
lb1.grid(row = 0, column = 0, padx = 225, pady = 25)

button00 = Button(root,bg = '#09F7C6', activebackground='#e8914f', text = 'LAUNCHPAD', highlightcolor = '#e8914f', width = 25,height = 5, command = lambda : launchpad() )
button00.grid(row = 1, column = 0, padx = 225, pady = 35)

button10 = Button(root,bg = '#09F7C6', activebackground='#e8914f', text = 'AUTO-COMPOSE', highlightcolor = '#e8914f', width = 25,height = 5, command=lambda : auto_compose() )
button10.grid(row = 2, column = 0, padx = 225, pady = 35)

'''
button21 = Button(root,bg = '#09F7C6', activebackground='#e8914f', text = 'BEATS CHALLENGE', highlightcolor = '#e8914f',width = 25,height = 5 )
button21.grid(row = 3, column = 0, padx = 225, pady = 35)'''

def auto_compose():
    import auto
    count = 1

def launchpad():
    import layout

root.mainloop()

