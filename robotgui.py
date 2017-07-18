import tkinter as tk
# import Tkinter as tk
from guiClient import *

# Setup Window

root = tk.Tk()

root.resizable(width=False, height=False)
root.geometry("600x400")
root.title('Backup Robot Interface')

# Left Toggle
'''
lblDirections = tk.Label(root, text='Directions')
lblDirections.grid(row=0, column=0)

btnForward = tk.Button(root, text='Forward', command=forward)
btnBackward = tk.Button(root, text='Backward', command=backward)

btnForward.grid(row=1, column=0)
btnBackward.grid(row=2, column=0)
'''
### Left and Right Directions may be impossible to be the same as evdev controller ???
'''
btnLeft = tk.Button(root, text='Left', command=help)
btnRight = tk.Button(root, text='Right', command=help)

btnLeft.grid(row=3, column=0)
btnRight.grid(row=4, column=0)
'''

# Controller Buttons

lblButtons = tk.Label(root, text='Controller Buttons')
lblButtons.grid(row=0, column=1)

btnX = tk.Button(root, text='X', command=X)
btnY = tk.Button(root, text='Y', command=Y)
btnA = tk.Button(root, text='A', command=A)
btnB = tk.Button(root, text='B', command=B)

btnX.grid(row=1, column=1)
btnY.grid(row=2, column=1)
btnA.grid(row=3, column=1)
btnB.grid(row=4, column=1)

# Right Toggle

lblRToggle = tk.Label(root, text='Controller Right Toggle')
lblRToggle.grid(row=0, column=2)

btnRTup = tk.Button(root, text='Up', command=rForward)
btnRTdown = tk.Button(root, text='Down', command=rBackward)

btnRTup.grid(column=2, row=1)
btnRTdown.grid(column=2, row=2)

q = lambda : root.destroy()

btnEnd = tk.Button(root, text='Exit', command=q)
btnEnd.grid(column=0, row=5)

# Back Buttons

lblBackButtons = tk.Label(root, text='R1,L1,R2,L2')
lblBackButtons.grid(row=0, column=3)

btnR1 = tk.Button(root, text='R1', command=R1)
btnR2 = tk.Button(root, text='R2', command=R2)
btnL1 = tk.Button(root, text='L1', command=L1)
btnL2 = tk.Button(root, text='L2', command=L2)

btnR1.grid(row=1, column=3)
btnR2.grid(row=2, column=3)
btnL1.grid(row=3, column=3)
btnL2.grid(row=4, column=3)

btnStop = tk.Button(root, text='Stop Movement', command = restart)
btnStop.grid(row=5, column=1)

root.mainloop()


