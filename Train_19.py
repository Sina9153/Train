from tkinter import*
from tkinter import messagebox

window=Tk()
window.title("Click Game")
window.geometry("700x700")
window.configure(bg="#1e1e2f")

all_clicks=0

def click():
    ac=all_clicks.get()
    ac+=1
    ac=all_clicks

label1=Label(window,bg="white",fg="black",text=all_clicks,width=10).pack(pady=10)

button1=Button(window,text="Click",command=click,bg="green",fg="white",height=3,width=10).pack(pady=50)

window.mainloop()