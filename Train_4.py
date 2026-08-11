b=0
one_click_two_points="off"
from tkinter import*
from tkinter import messagebox

window=Tk()
window.title("click game")
window.geometry("500x500")
window.configure(bg="#1e1e2f")

def clear():
    for widget in window.winfo_children():
        widget.destroy()

def ability():
    clear()
    def o_c_t_p():
        global one_click_two_points
        global b
        if one_click_two_points=="off":
            if b>=20:
                one_click_two_points="on"
                b-=20
                messagebox.showinfo("Info","You Lost 20 Points")
            else:
                messagebox.showwarning("Warning","You Don't Have Enough Point")
        else:
            one_click_two_points="off"
    button4=Button(window,text="One Click Two Points\n Point Need=20",command=o_c_t_p,bg="green",fg="white",width=25,height=3)
    button4.place(x=160,y=200)
    button5=Button(window,text="Main Menu",command=main_menu,bg="green",fg="white")
    button5.place(x=425,y=465)

def main_menu():

    clear()

    def click():
        global b
        if one_click_two_points=="on":
            b+=2
            button1.config(text=b)
        else:
           b+=1
           button1.config(text=b)

    button1=Button(window,text=b,width=25,height=1)
    button1.place(x=160,y=20)

    button2=Button(window,text="click",command=click,bg="green",fg="white",width=25,height=3)
    button2.place(x=160,y=200)

    button3=Button(window,text="Abilities",command=ability,bg="green",fg="white",width=5)
    button3.place(x=450,y=465)

main_menu()
window.mainloop()