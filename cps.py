from tkinter import *

c = 0
cps = 0
#time = 10

def kps():
	global c, cps
	kps = c / 10
	text4.config(text = kps)

def clicks():
	global c
	c += 1
	text2.config(text = c)

# Not used in the final version
# def ttime():
# 	global time
# 	time -= 1
# 	text5.config(text = time)

def start():
	root.after(10000, kps)

root = Tk()
root.resizable(0, 0)
root.title("Clicker test")
root.geometry("130x270")

text1 = Label(root, text = "Clicks")
text1.pack()

text2 = Label(root, text = c)
text2.config(font = ("Arial", 30, 'bold'))
text2.pack()

text3 = Label(root, text = "CPS")
text3.pack()

text4 = Label(root, text = cps)
text4.config(font = ("Arial", 30, 'bold'))
text4.pack()

butt1 = Button(root, text = "Click me", width = 15, height = 5, command = clicks)
butt1.pack()

butt2 = Button(root, text = "Start", width = 15, command = start)
butt2.pack()

root.mainloop()
