from Tkinter import *
import os

root = Tk()
termf = Frame(root, height=1300, width=1000)

termf.pack(fill=BOTH, expand=YES)

wid = termf.winfo_id()
font = "'dejavu serif'"
os.system('xterm -into %d  -geometry 70x60 -sb  -fa -%s- & ' % (wid, font))
root.mainloop()
