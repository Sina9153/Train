b=0
from tkinter import*
window=Tk()

window.title("click game")
window.geometry("1000x1000")
window.configure(bg="blue")

a=Entry(window)
a.pack()

def click():
    global b
    b+=1
    button1.config(text=b)

button1=Button(window,text=b)
button1.place(x=100,y=200)

button2=Button(window,text="click",command=click,bg="white")
button2.place(x=100,y=300)

window.mainloop()
