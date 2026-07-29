from tkinter import*
from tkinter import messagebox

window=Tk()
window.title("Takhfif")
window.geometry("500x400")
window.configure(bg="#1e1e2f")

label=Label(window,text="Gheymat:",font=("Arial",18,"bold"),bg="#1e1e2f",fg="white")
label.place(x=190,y=10)
label1=Label(window,text="Takhfif:",font=("Arial",18,"bold"),bg="#1e1e2f",fg="white")
label1.place(x=200,y=100)
label2=Label(window,text="Sood:",font=("Arial",18,"bold"),bg="#1e1e2f",fg="white")
label2.place(x=212,y=190)

entry=Entry(window,font=("Arial",18,"bold"))
entry.place(x=120,y=40)

entry1=Entry(window,font=("Arial",18,"bold"))
entry1.place(x=120,y=130)

entry2=Entry(window,font=("Arial",18,"bold"))
entry2.place(x=120,y=220)

def takhfif():
    a=int(entry.get())
    b=int(entry1.get())
    javab=0
    b=100-b
    javab=(b*a)/100
    messagebox.showinfo("Javab:",f"{javab}")

def sood():
    a=int(entry.get())
    c=int(entry2.get())
    javab=0
    if c<100:
        c+=100
        javab=(c*a)/100
        messagebox.showinfo("Javab:",f"{javab}")
    elif c>100:
        javab=(c*a)/100
        messagebox.showinfo("Javab:",f"{javab}")
    else:
        messagebox.showinfo("Javab:",f"{a}")

button=Button(window,text="Check Takhfif",command=takhfif,font=("Arial",18,"bold"),bg="green",fg="white",width=15,height=2)
button.place(x=10,y=300)

button1=Button(window,text="Check Sood",command=sood,font=('Arial',18,"bold"),bg="green",fg="white",width=15,height=2)
button1.place(x=250,y=300)

window.mainloop()
