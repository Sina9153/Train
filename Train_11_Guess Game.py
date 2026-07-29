import random
from tkinter import*
from tkinter import messagebox
import pyfiglet 

window=Tk()
window.title("Guess Game")
window.geometry("700x500")
window.configure(bg="#1e1e2f")

label1=Label(window,text="Guess",font=("Arial",18,"bold"),bg="#1e1e2f",fg="white").pack(pady=10)
entry1=Entry(window,font="Arial")
entry1.pack(pady=10)
label2=Label(window,text="version=1.2.0",font=("Arial",20,"bold"),bg="#1e1e2f",fg="white")
label2.place(x=520,y=460)

a=random.randint(0,10)

def check():
    d=entry1.get()
    if d.isalpha()==True:
        messagebox.showwarning("Warning","You Didn't Enter A Number")
        entry1.delete("0,End")
    else:
        b=int(entry1.get())
    if b>a:
        messagebox.showwarning("Wrong","Lower")
    elif b<a:
        messagebox.showwarning("Wrong","Higher")
    elif b==a:
        messagebox.showinfo("Success","You Got It")

Button(window,text="check",font=("Arial",14),bg="green",fg="white",width=25,command=check).pack(pady=10)

window.mainloop()