from tkinter import*
from tkinter import messagebox
from PIL import Image,ImageTk
import sqlite3
import os
import hashlib

window=Tk()
window.geometry("800x700")
window.title("Mini Hearts Of Iron")
window.configure(bg="#596052")

database_path=os.path.join(os.path.dirname(os.path.abspath(__file__)),"game_database.db")
connection=sqlite3.connect(database_path)
cursor=connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS players(
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT UNIQUE NOT NULL,
password TEXT NOT NULL,
country TEXT NOT NULL,
year INTEGER NOT NULL,
month INTEGER NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS researches(
id INTEGER PRIMARY KEY AUTOINCREMENT,
player_id INTEGER NOT NULL,
research_name TEXT NOT NULL,
researching INTEGER NOT NULL DEFAULT 0,
finished INTEGER NOT NULL DEFAULT 0,
finish_year INTEGER NOT NULL DEFAULT 0,
finish_month INTEGER NOT NULL DEFAULT 0,
UNIQUE(player_id,research_name)
)
""")

connection.commit()

all_countries={"1":"Germany","2":"Italy","3":"United Kingdom","4":"France","5":"Spain"}
country_width=150
country_height=125
playing_as=""
player_id=0
username=""

year=1936
month=1

researching=False
colt_finish=False
colt_research_finish_year=0
colt_research_finish_month=0

months=["January","February","March","April","May","June","July","August","September","October","November","December"]

country_colors={
"Germany":"#555555",
"Italy":"#4CAF50",
"United Kingdom":"#4A69BD",
"France":"#3498DB",
"Spain":"#E67E22"
}

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def clear():
    for widget in window.winfo_children():
        widget.destroy()

def get_date():
    return f"{months[month-1]} {year}"

def save_game():
    if player_id==0:
        return
    cursor.execute(
        "UPDATE players SET country=?,year=?,month=? WHERE id=?",
        (playing_as,year,month,player_id)
    )
    cursor.execute(
        """UPDATE researches
        SET researching=?,finished=?,finish_year=?,finish_month=?
        WHERE player_id=? AND research_name=?""",
        (int(researching),int(colt_finish),colt_research_finish_year,colt_research_finish_month,player_id,"M9 Pistol")
    )
    connection.commit()

def load_game():
    global year,month,playing_as,researching,colt_finish,colt_research_finish_year,colt_research_finish_month
    cursor.execute(
        "SELECT country,year,month FROM players WHERE id=?",
        (player_id,)
    )
    player=cursor.fetchone()
    if player:
        playing_as=player[0]
        year=player[1]
        month=player[2]
    cursor.execute(
        """SELECT researching,finished,finish_year,finish_month
        FROM researches
        WHERE player_id=? AND research_name=?""",
        (player_id,"M9 Pistol")
    )
    research_data=cursor.fetchone()
    if research_data:
        researching=bool(research_data[0])
        colt_finish=bool(research_data[1])
        colt_research_finish_year=research_data[2]
        colt_research_finish_month=research_data[3]
    else:
        cursor.execute(
            "INSERT INTO researches(player_id,research_name) VALUES(?,?)",
            (player_id,"M9 Pistol")
        )
        connection.commit()

def next_month():
    global year,month
    month+=1
    if month>12:
        month=1
        year+=1
    re_colt_2()
    save_game()
    update_date()

def re_colt_2():
    global researching,colt_finish
    if researching:
        if year>colt_research_finish_year or (year==colt_research_finish_year and month>=colt_research_finish_month):
            researching=False
            colt_finish=True
            save_game()
            messagebox.showinfo("Research","M9 Pistol Research Finished!")

def update_date():
    if "date_label" in globals():
        date_label.config(text=get_date())

def register():
    global player_id,username,playing_as
    new_username=username_entry.get().strip()
    new_password=password_entry.get()
    selected_country=country_var.get()
    if new_username=="" or new_password=="":
        messagebox.showwarning("Warning","Please enter username and password.")
        return
    if selected_country=="":
        messagebox.showwarning("Warning","Please choose a country.")
        return
    try:
        cursor.execute(
            "INSERT INTO players(username,password,country,year,month) VALUES(?,?,?,?,?)",
            (new_username,hash_password(new_password),selected_country,1936,1)
        )
        connection.commit()
        player_id=cursor.lastrowid
        username=new_username
        playing_as=selected_country
        load_game()
        home()
    except sqlite3.IntegrityError:
        messagebox.showerror("Error","This username already exists.")

def login():
    global player_id,username
    entered_username=username_entry.get().strip()
    entered_password=password_entry.get()
    if entered_username=="" or entered_password=="":
        messagebox.showwarning("Warning","Please enter username and password.")
        return
    cursor.execute(
        "SELECT id,username FROM players WHERE username=? AND password=?",
        (entered_username,hash_password(entered_password))
    )
    player=cursor.fetchone()
    if player is None:
        messagebox.showerror("Error","Username or password is incorrect.")
        return
    player_id=player[0]
    username=player[1]
    load_game()
    home()

def account_screen():
    clear()
    window.configure(bg="#1e1e2f")
    Label(window,text="Mini Hearts Of Iron",font=("Arial",28,"bold"),bg="#1e1e2f",fg="white").place(x=245,y=70)
    Label(window,text="Username",font=("Arial",14),bg="#1e1e2f",fg="white").place(x=260,y=160)
    global username_entry,password_entry,country_var
    username_entry=Entry(window,width=30)
    username_entry.place(x=260,y=190)
    Label(window,text="Password",font=("Arial",14),bg="#1e1e2f",fg="white").place(x=260,y=230)
    password_entry=Entry(window,width=30,show="*")
    password_entry.place(x=260,y=260)
    Label(window,text="Country",font=("Arial",14),bg="#1e1e2f",fg="white").place(x=260,y=300)
    country_var=StringVar()
    country_menu=OptionMenu(window,country_var,"Germany","Italy","United Kingdom","France","Spain")
    country_menu.config(width=25)
    country_menu.place(x=260,y=330)
    Button(window,text="Register",command=register,width=12).place(x=260,y=390)
    Button(window,text="Login",command=login,width=12).place(x=390,y=390)

def home():
    clear()
    window.configure(bg="#596052")
    control_panel=Label(window,bg="#202024",height=2,width=800)
    control_panel.place(x=1,y=1)
    global date_label
    date_label=Label(window,text=get_date(),bg="#202024",fg="white",font=("Arial",16,"bold"))
    date_label.place(x=630,y=5)
    Button(window,text="▶",command=next_month).place(x=600,y=6)
    Label(window,text=f"Playing as: {playing_as}",bg="#202024",fg="white").place(x=400,y=7)

    def research():
        clear()
        window.configure(bg="#1e1e2f")
        control_panel_research=Label(window,bg="#ffffff",height=2,width=800)
        control_panel_research.place(x=1,y=1)
        Button(window,text="←",command=home).place(x=3,y=6)

        def arm():
            clear()
            window.configure(bg="#1e1e2f")
            control_panel_arm=Label(window,bg="#ffffff",height=2,width=800)
            control_panel_arm.place(x=1,y=1)
            Button(window,text="←",command=research).place(x=3,y=6)
            Label(window,font=("Arial",50),text="1930").place(x=3,y=70)
            Label(window,font=("Arial",50),text="1950").place(x=3,y=220)
            Label(window,font=("Arial",50),text="1980").place(x=3,y=370)

            def re_colt_1():
                global researching,colt_research_finish_year,colt_research_finish_month
                if colt_finish:
                    messagebox.showwarning("Warning","You Did That")
                    return
                if researching:
                    messagebox.showwarning("Warning","One Research Is Already In Progress")
                    return
                researching=True
                colt_research_finish_year=year
                colt_research_finish_month=month+3
                while colt_research_finish_month>12:
                    colt_research_finish_month-=12
                    colt_research_finish_year+=1
                save_game()
                messagebox.showinfo("Research","It Will Finish After 3 Months")

            m9_image=Image.open("D:/Python/Sina/Train/M9-pistolet.jpg")
            m9_image=m9_image.resize((90,60))
            m9_image=ImageTk.PhotoImage(m9_image)
            m9_button=Button(window,image=m9_image,command=re_colt_1)
            m9_button.place(x=200,y=70)
            window.m9_image=m9_image
            Label(window,font=("Arial",15),text="M9 Pistol").place(x=203,y=135)

            if colt_finish:
                m9_button.config(state=DISABLED)
                Label(window,text="COMPLETED",font=("Arial",11,"bold")).place(x=200,y=155)
            elif researching:
                Label(window,text=f"Finishes: {months[colt_research_finish_month-1]} {colt_research_finish_year}",font=("Arial",10)).place(x=175,y=155)

        def armor():
            clear()
            window.configure(bg="#1e1e2f")
            control_panel_armor=Label(window,bg="#ffffff",height=2,width=800)
            control_panel_armor.place(x=1,y=1)
            Button(window,text="←",command=research).place(x=3,y=6)
            Label(window,font=("Arial",50),text="1930").place(x=3,y=70)
            Label(window,font=("Arial",50),text="1950").place(x=3,y=220)
            Label(window,font=("Arial",50),text="1980").place(x=3,y=370)
            Button(window,text="Colt").place(x=200,y=70)

        Button(window,text="Armament",command=arm).place(x=60,y=6)
        Button(window,text="Armor",command=armor).place(x=150,y=6)

    Button(window,text="Research",command=research).place(x=3,y=6)

    germany_line=Canvas(window,width=country_width,height=country_height,bg=country_colors["Germany"])
    germany_line.place(x=100,y=50)
    germany_line.create_text(country_width/2,country_height/2,text=all_countries["1"],fill="white")

    italy_line=Canvas(window,width=country_width,height=country_height,bg=country_colors["Italy"])
    italy_line.place(x=550,y=125)
    italy_line.create_text(country_width/2,country_height/2,text=all_countries["2"],fill="white")

    united_Kingdom_line=Canvas(window,width=country_width,height=country_height,bg=country_colors["United Kingdom"])
    united_Kingdom_line.place(x=400,y=325)
    united_Kingdom_line.create_text(country_width/2,country_height/2,text=all_countries["3"],fill="white")

    france_line=Canvas(window,width=country_width,height=country_height,bg=country_colors["France"])
    france_line.place(x=50,y=325)
    france_line.create_text(country_width/2,country_height/2,text=all_countries["4"],fill="white")

    spain_line=Canvas(window,width=country_width,height=country_height,bg=country_colors["Spain"])
    spain_line.place(x=600,y=450)
    spain_line.create_text(country_width/2,country_height/2,text=all_countries["5"],fill="white")

account_screen()
window.mainloop()
connection.close()
