from tkinter import*
from tkinter import messagebox

window=Tk()
window.title("Jam")
window.geometry("500x400")
window.configure(bg="#1e1e2f")

label=Label(window,text="Enter A First Number:",font=("Arial",18,"bold"),bg="#1e1e2f",fg="white")
label.place(x=122,y=10)
label1=Label(window,text="Enter A Second Number:",font=("Arial",18,"bold"),bg="#1e1e2f",fg="white")
label1.place(x=110,y=80)

entry=Entry(window,font=("Arial"))
entry.place(x=150,y=50)
entry1=Entry(window,font=("Arial"))
entry1.place(x=150,y=120)

def hesab():
    a=int(entry.get())
    b=int(entry1.get())
    c=a+b
    messagebox.showinfo("Hesab:",f"Answer:\n{c}")

button=Button(window,text="Check",command=hesab,font="Arial",bg="green",fg="white",width=30,height=3)
button.place(x=105,y=200)

window.mainloop()
