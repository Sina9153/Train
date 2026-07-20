from tkinter import*
from tkinter import messagebox

window=Tk()
window.title("school scores")
window.geometry("300x400")
window.configure(bg="#1e1e2f")

Label(window,text="Enter The Score:",font=("Arial", 18, "bold"),bg="#1e1e2f",fg="white").pack(pady=15)
Label(window,text="Enter Student's Name:",font=("Arial", 18, "bold"),bg="#1e1e2f",fg="white").pack(pady=30)

entry=Entry(window,font=("Arial", 18))
entry.pack()
entry.place(x=25,y=50)
entry1=Entry(window,font=("Arial", 18))
entry1.pack()
entry1.place(x=25,y=130)

studentscores=[]
studentname=[]

def add():
    studentscores.append(entry.get())
    studentname.append(entry1.get())

def show():
    messagebox.showinfo(
        "Students",
        f"Names:\n{studentname}\n\nScores:\n{studentscores}")
    
button=Button(window,text="Add",command=add,font=("Arial", 15, "bold"),bg="green",fg="white",width=15)
button.place(x=10,y=300)

button1=Button(window,text="Show All",command=show,font=("Arial", 15, "bold"),bg="green",fg="white")
button1.place(x=200,y=300)

window.mainloop()
