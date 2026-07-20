from tkinter import*
from tkinter import messagebox

window=Tk()
window.title("Phone Numbers")
window.geometry("500x300")
window.configure(bg="#1e1e2f")

label=Label(window,text="Enter A Phone Number:",font=("B nazanin",18,"bold"),bg="#1e1e2f",fg="white")
label.place(x=105,y=10)
label1=Label(window,text="Enter His/Her Name:",font=("B nazanin",18,"bold"),bg="#1e1e2f",fg="white")
label1.place(x=120,y=100)

phonebook={}

entry=Entry(window,font=("Arial",18,"bold"))
entry.place(x=120,y=45)
entry1=Entry(window,font=("Arial",18,"bold"))
entry1.place(x=120,y=135)

def add():
    if entry.get().isdigit() == True:
       phonebook["number"]=entry.get()
    else:
        messagebox.showerror("Error:","Number Is False")
    if entry1.get.isalpha() == True:
       phonebook["name"]=entry1.get()
    else:
       messagebox.showerror("Error:","Name Is False")

def check():
    phonebook["number"]=entry.get()
    phonebook["name"]=entry1.get()
    messagebox.showinfo("Numbers:",f"{phonebook['name']}:{phonebook['number']}")

button=Button(window,text="Show All",command=check,font=("Arial",18,"bold"),bg="green",fg="white",width=10,height=1)
button.place(x=90,y=200)
button1=Button(window,text="Add",command=add,font=("Arial",18,"bold"),bg="green",fg="white",width=10,height=1)
button1.place(x=250,y=200)

window.mainloop()
