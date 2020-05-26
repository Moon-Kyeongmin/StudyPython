from tkinter import *

root=Tk()

Label(root,text="Hello World!").pack()

root.title("Hello")
root.geometry("640x400+320+60")

def callback():
    print("Event")
def quit():
    exit(0)
btnQuit=Button(root,text="Quit",width=20,command=quit)
btn=Button(root,text="Click",width=20,command=callback)

btn.pack(padx=10,pady=10)
btnQuit.pack(padx=20,pady=20)
root.mainloop()