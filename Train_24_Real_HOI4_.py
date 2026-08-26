from tkinter import*
from tkinter import messagebox

window=Tk()
window.geometry("800x700")
window.title("Mini Hearts Of Iron")
window.configure(bg="#596052")

all_countries={"1":"Germany","2":"Italy","3":"United Kingdom","4":"France","5":"Spain"}
country_width=150
country_height=125
players_country=""

def start():
    Label(window,text="Choose One Country:",font=("Arial",18,"bold"),bg="#1e1e2f",fg="white").place(x=1,y=1)
    def germany1():
        global players_country
        players_country="Germany"
        home()

    def italy1():
        global players_country
        players_country="Italy"
        home()

    def united_Kingdom1():
        global players_country
        players_country="United Kingdom"
        home()

    def france1():
        global players_country
        players_country="France"
        home()

    def spain1():
        global players_country
        players_country="Spain"
        home()


    germany=Button(window,text="Germany",command=germany1,width=20,height=20,bg="green")
    germany.place(x=100,y=50)
    
    italy=Button(window,text="Italy",command=italy1,width=20,height=20,bg="green")
    italy.place(x=550,y=125)
    
    united_Kingdom=Button(window,command=united_Kingdom1,text="United Kingdom",width=20,height=20,bg="green")
    united_Kingdom.place(x=400,y=325)
    
    france=Button(window,command=france1,text="France",width=20,height=20,bg="green")
    france.place(x=50,y=325)
    
    spain=Button(window,command=spain1,text="Spain",width=20,height=20,bg="green")
    spain.place(x=290,y=450)
    
def home():

    control_panel=Label(window,bg="#202024",height=2,width=800).place(x=1,y=1)

    germany_line=Canvas(window,width=country_width,height=country_height,bg="green")
    germany_line.place(x=100,y=125)
    germany_line.create_text(country_width/2,country_height/2,text=all_countries["1"],fill="white")

    italy_line=Canvas(window,width=country_width,height=country_height,bg="green")
    italy_line.place(x=550,y=125)
    italy_line.create_text(country_width/2,country_height/2,text=all_countries["2"],fill="white")

    united_Kingdom_line=Canvas(window,width=country_width,height=country_height,bg="green")
    united_Kingdom_line.place(x=400,y=325)
    united_Kingdom_line.create_text(country_width/2,country_height/2,text=all_countries["3"],fill="white")

    france_line=Canvas(window,width=country_width,height=country_height,bg="green")
    france_line.place(x=50,y=325)
    france_line.create_text(country_width/2,country_height/2,text=all_countries["4"],fill="white")

    spain_line=Canvas(window,width=country_width,height=country_height,bg="green")
    spain_line.place(x=290,y=450)
    spain_line.create_text(country_width/2,country_height/2,text=all_countries["5"],fill="white")

start()
window.mainloop()