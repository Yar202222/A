from tkinter import *
import random
root=Tk()
root.geometry("500x550")
canvas=Canvas(root,width=500,height=500,bg="white")
canvas.pack()
def button():
    a=random.randint(1,3)
    canvas.delete("all")
    if a==1:
        canvas.create_oval(random.randint(50,450),random.randint(50,450),random.randint(100,450),random.randint(100,450),fill="black")
    elif a==2:
        canvas.create_polygon(random.randint(50,450),random.randint(50,450),random.randint(100,450),random.randint(100,450),random.randint(100,450),random.randint(100,450))
    elif a==3:
        canvas.create_rectangle(random.randint(50,450),random.randint(50,450),random.randint(100,450),random.randint(100,450),fill="black")
Button(command=button).place(width=50,height=50)
root.mainloop()