from tkinter import *
import time
from playsound import playsound
import threading
import subprocess
import multiprocessing
import random

'''for r in range(4):
	for c in range(4):
		if c%2 == 1 :
			color = "#292fd9"
		else:
			color =  "#ad2ad1"
		if c < 2:
			t = "DRUM"
		elif c == 2:
			t = "BASS"
		else:
			t = "MELODY"

		print("button{}{} = Button(root,bg = '{}', activebackground='#e8914f', text = '{}', highlightcolor = '#e8914f', command  = lambda : press({},{}), width = 25,height = 10 )".format(r,c,color, t,r,c))
		print("button{}{}.grid(row = {}, column = {}, padx = 25, pady = 25)".format(r,c,r,c))'''

 
root = Tk()
root.geometry("1500x840")
root.configure(background = 'black')

    
button00 = Button(root,bg = '#ad2ad1', activebackground='#e8914f', text = 'DRUM', highlightcolor = '#e8914f', command  = lambda : press(0,0), width = 25,height = 10 )
button00.grid(row = 0, column = 0, padx = 25, pady = 25)
button01 = Button(root,bg = '#292fd9', activebackground='#e8914f', text = 'DRUM', highlightcolor = '#e8914f', command  = lambda : press(0,1), width = 25,height = 10 )
button01.grid(row = 0, column = 1, padx = 25, pady = 25)
button02 = Button(root,bg = '#ad2ad1', activebackground='#e8914f', text = 'BASS', highlightcolor = '#e8914f', command  = lambda : press(0,2), width = 25,height = 10 )
button02.grid(row = 0, column = 2, padx = 25, pady = 25)
button03 = Button(root,bg = '#292fd9', activebackground='#e8914f', text = 'MELODY', highlightcolor = '#e8914f', command  = lambda : press(0,3), width = 25,height = 10 )
button03.grid(row = 0, column = 3, padx = 25, pady = 25)
button10 = Button(root,bg = '#ad2ad1', activebackground='#e8914f', text = 'DRUM', highlightcolor = '#e8914f', command  = lambda : press(1,0), width = 25,height = 10 )
button10.grid(row = 1, column = 0, padx = 25, pady = 25)
button11 = Button(root,bg = '#292fd9', activebackground='#e8914f', text = 'DRUM', highlightcolor = '#e8914f', command  = lambda : press(1,1), width = 25,height = 10 )
button11.grid(row = 1, column = 1, padx = 25, pady = 25)
button12 = Button(root,bg = '#ad2ad1', activebackground='#e8914f', text = 'BASS', highlightcolor = '#e8914f', command  = lambda : press(1,2), width = 25,height = 10 )
button12.grid(row = 1, column = 2, padx = 25, pady = 25)
button13 = Button(root,bg = '#292fd9', activebackground='#e8914f', text = 'MELODY', highlightcolor = '#e8914f', command  = lambda : press(1,3), width = 25,height = 10 )
button13.grid(row = 1, column = 3, padx = 25, pady = 25)
button20 = Button(root,bg = '#ad2ad1', activebackground='#e8914f', text = 'DRUM', highlightcolor = '#e8914f', command  = lambda : press(2,0), width = 25,height = 10 )
button20.grid(row = 2, column = 0, padx = 25, pady = 25)
button21 = Button(root,bg = '#292fd9', activebackground='#e8914f', text = 'DRUM', highlightcolor = '#e8914f', command  = lambda : press(2,1), width = 25,height = 10 )
button21.grid(row = 2, column = 1, padx = 25, pady = 25)
button22 = Button(root,bg = '#ad2ad1', activebackground='#e8914f', text = 'BASS', highlightcolor = '#e8914f', command  = lambda : press(2,2), width = 25,height = 10 )
button22.grid(row = 2, column = 2, padx = 25, pady = 25)
button23 = Button(root,bg = '#292fd9', activebackground='#e8914f', text = 'MELODY', highlightcolor = '#e8914f', command  = lambda : press(2,3), width = 25,height = 10 )
button23.grid(row = 2, column = 3, padx = 25, pady = 25)
button30 = Button(root,bg = '#ad2ad1', activebackground='#e8914f', text = 'DRUM', highlightcolor = '#e8914f', command  = lambda : press(3,0), width = 25,height = 10 )
button30.grid(row = 3, column = 0, padx = 25, pady = 25)
button31 = Button(root,bg = '#292fd9', activebackground='#e8914f', text = 'DRUM', highlightcolor = '#e8914f', command  = lambda : press(3,1), width = 25,height = 10 )
button31.grid(row = 3, column = 1, padx = 25, pady = 25)
button32 = Button(root,bg = '#ad2ad1', activebackground='#e8914f', text = 'BASS', highlightcolor = '#e8914f', command  = lambda : press(3,2), width = 25,height = 10 )
button32.grid(row = 3, column = 2, padx = 25, pady = 25)
button33 = Button(root,bg = '#292fd9', activebackground='#e8914f', text = 'MELODY', highlightcolor = '#e8914f', command  = lambda : press(3,3), width = 25,height = 10 )
button33.grid(row = 3, column = 3, padx = 25, pady = 25)


button04 = Button(root,bg = '#ad2ad1', activebackground='#e8914f', text = 'CUSTOM', highlightcolor = '#e8914f', command  = lambda : press(0,4), width = 25,height = 10 )
button04.grid(row = 0, column = 4, padx = 205, pady = 25)
button14 = Button(root,bg = '#ad2ad1', activebackground='#e8914f', text = 'CUSTOM', highlightcolor = '#e8914f', command  = lambda : press(1,4), width = 25,height = 10 )
button14.grid(row = 1, column = 4, padx = 205, pady = 25)
button24 = Button(root,bg = '#ad2ad1', activebackground='#e8914f', text = 'CUSTOM', highlightcolor = '#e8914f', command  = lambda : press(2, 4), width = 25,height = 10 )
button24.grid(row = 2, column = 4, padx = 205, pady = 25)
button34 = Button(root,bg = '#ad2ad1', activebackground='#e8914f', text = 'CUSTOM', highlightcolor = '#e8914f', command  = lambda : press(3,4), width = 25,height = 10 )
button34.grid(row = 3, column = 4, padx = 205, pady = 25)


history = []

states = [[0, 0, 0, 0, 0], \
          [0, 0, 0, 0, 0], \
          [0, 0, 0, 0, 0], \
          [0, 0, 0, 0, 0]]


clock_timer = time.time()
current_timer = clock_timer
current_tiles = 0#number of tiles playing
select_tiles = []


count = 0
def randomize():
    global count

    for c in range(4):
        r2 = random.choice([0,1,2,3])
        press(r2,c)

    r2 = random.choice([0,1,2,3])
    press(r2,4)
    
    if count == 0:

        if random.random() > 0.3:

            t1 = threading.Timer(8,randomize)
            t1.start()
        if random.random() > 0.3:
            
            t2 = threading.Timer(18,randomize)
            t2.start()
        if random.random() > 0.3:
            t3 = threading.Timer(28,randomize)
            t3.start()
        if random.random() > 0.3:
            t4= threading.Timer(38,randomize)
            t4.start()
        if random.random() > 0.3:
            t5 = threading.Timer(48,randomize)
            t5.start()
        if random.random() > 0.3:
            t6 = threading.Timer(58,randomize)
            t6.start()
        if random.random() > 0.3:
            t7 = threading.Timer(68,randomize)
            t7.start()
        if random.random() > 0.3:
            t8 = threading.Timer(78,randomize)
            t8.start()
        if random.random() > 0.3:
            t9 = threading.Timer(88,randomize)
            t9.start()
        if random.random() > 0.3:
            t10 = threading.Timer(98,randomize)
            t10.start()
        if random.random() > 0.3:
            t11 = threading.Timer(108,randomize)
            t11.start()
        if random.random() > 0.3:
            t12 = threading.Timer(118,randomize)
            t12.start()
        count = 1



def press(r,c):
    if current_tiles == 0:
        clock_timer = time.time()
        #current_timer = clock_timer
    toggle(r,c)#colors
    

def toggle(r,c):
    global current_tiles, select_tiles, clock_timer, current_timer
    if states[r][c] == 1:
        reset(r,c)
        current_tiles -= 1
    else:
        add_tile = 1
        for row in range(len(states)):
            if (states[row][c] == 1) :
                reset(row,c)
                add_tile = 0
                select_tiles.remove([row,c])
                break
        set(r,c)
        current_tiles += add_tile
        select_tiles.append([r,c])

                           
def play():
    cycle1 = []
    for r,c in select_tiles:
        print("R: ", r)
        print("C: ", c)
        exec("startthreads{}{}()".format(r,c))
        cycle1.append([r,c])
    history.append(cycle1)
    print(history)

       
def reset(r,c):
    halt(r,c)
    time.sleep(0.1)#change to next cycle
    states[r][c] = 0
    if (c%2 == 1 ):
            color = "#292fd9"
    else:
            color =  "#ad2ad1"
    exec("button{}{}.configure(bg = '{}')".format(r,c,color))
    return;

def set(r,c):
    print("Set {},{} ".format(r,c))
    states[r][c] = 1
    exec("button{}{}.configure(bg = 'red')".format(r,c))

def halt(r,c):
    states[r][c] = 0
    exec("button{}{}.configure(bg = '#e8914f')".format(r,c))


def startdrums1():
    playsound('drums1.wav')

def startdrums2():
    playsound('drums2.wav')

def startdrums3():
    playsound('drums3.wav')

def startdrums4():
    playsound('drums4.wav')

def startdrums5():
    playsound('drums5.wav')

def startdrums6():
    playsound('drums6.wav')

def startdrums7():
    playsound('drums7.wav')

def startdrums8():
    playsound('drums8.wav')

def startbass1():
    playsound('bass1.wav')

def startbass2():
    playsound('bass2.wav')

def startbass3():
    playsound('bass3.wav')

def startbass4():
    playsound('bass4.wav')

def startmel1():
    playsound('mel1.wav')

def startmel2():
    playsound('mel2.wav')

def startmel3():
    playsound('mel3.wav')

def startmel4():
    playsound('mel4.wav')

def startcustom1():
    playsound('custom1.wav')
    try:
        select_tiles.remove([0,4])
    except:
        pass
    reset(0,4)


def startcustom2():
    playsound('custom2.wav')
    try:
        select_tiles.remove([1,4])
    except:
        pass
    reset(1,4)


def startcustom3():
    playsound('custom3.wav')
    try:
        select_tiles.remove([2,4])
    except:
        pass
    reset(2,4)


def startcustom4():
    playsound('custom4.wav')
    try:
        select_tiles.remove([3,4])
    except:
        pass
    reset(3,4)

  


def startthreads00():
    thread1 = threading.Thread(target=startdrums1)
    thread1.start()

def startthreads10():
    thread1 = threading.Thread(target=startdrums2)
    thread1.start()

def startthreads20():
    thread1 = threading.Thread(target=startdrums3)
    thread1.start()

def startthreads30():
    thread1 = threading.Thread(target=startdrums4)
    thread1.start()

def startthreads01():
    thread1 = threading.Thread(target=startdrums5)
    thread1.start()

def startthreads11():
    thread1 = threading.Thread(target=startdrums6)
    thread1.start()

def startthreads21():
    thread1 = threading.Thread(target=startdrums7)
    thread1.start()

def startthreads31():
    thread1 = threading.Thread(target=startdrums8)
    thread1.start()

def startthreads02():
    thread1 = threading.Thread(target=startbass1)
    thread1.start()

def startthreads12():
    thread1 = threading.Thread(target=startbass2)
    thread1.start()

def startthreads22():
    thread1 = threading.Thread(target=startbass3)
    thread1.start()

def startthreads32():
    thread1 = threading.Thread(target=startbass4)
    thread1.start()

def startthreads03():
    thread1 = threading.Thread(target=startmel1)
    thread1.start()

def startthreads13():
    thread1 = threading.Thread(target=startmel2)
    thread1.start()

def startthreads23():
    thread1 = threading.Thread(target=startmel3)
    thread1.start()

def startthreads33():
    thread1 = threading.Thread(target=startmel4)
    thread1.start()

def startthreads04():
    thread1 = threading.Thread(target=startcustom1)
    thread1.start()

def startthreads14():
    thread1 = threading.Thread(target=startcustom2)
    thread1.start()

def startthreads24():
    thread1 = threading.Thread(target=startcustom3)
    thread1.start()

def startthreads34():
    thread1 = threading.Thread(target=startcustom4)
    thread1.start()



play()

t1 = threading.Timer(10,play)
t1.start()

t2 = threading.Timer(20,play)
t2.start()

t3 = threading.Timer(30,play)
t3.start()
t4= threading.Timer(40,play)
t4.start()
t5 = threading.Timer(50,play)
t5.start()
t6 = threading.Timer(60,play)
t6.start()
t7 = threading.Timer(70,play)
t7.start()
t8 = threading.Timer(80,play)
t8.start()
t9 = threading.Timer(90,play)
t9.start()
t10 = threading.Timer(100,play)
t10.start()
t11 = threading.Timer(110,play)
t11.start()
t12 = threading.Timer(120,play)
t12.start()

root.mainloop()

