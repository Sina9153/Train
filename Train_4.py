import os
import hashlib
import pyexcel
from tkinter import *
from tkinter import messagebox

FILE = "users.xlsx"

b = 0
one_click_two_points = "off"
current_user = ""

BG = "#151522"
CARD = "#202033"
BUTTON = "#5865F2"
GREEN = "#2ECC71"
RED = "#E74C3C"
TEXT = "#FFFFFF"
GRAY = "#A0A0B0"

window = Tk()
window.title("NOVA CLICK")
window.geometry("700x600")
window.configure(bg=BG)
window.resizable(False, False)


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def create_file():
    if not os.path.exists(FILE):
        pyexcel.save_as(
            array=[
                ["Username", "Password", "Score"],
                ["admin", hash_password("admin"), 0]
            ],
            dest_file_name=FILE
        )


def get_users():
    create_file()
    records = pyexcel.iget_records(file_name=FILE)
    return list(records)


def save_users(users):
    data = [["Username", "Password", "Score"]]

    for user in users:
        data.append([
            user["Username"],
            user["Password"],
            user["Score"]
        ])

    pyexcel.save_as(
        array=data,
        dest_file_name=FILE
    )


def clear():
    for widget in window.winfo_children():
        widget.destroy()


def title_label(text):
    label = Label(
        window,
        text=text,
        bg=BG,
        fg=TEXT,
        font=("Arial", 28, "bold")
    )
    label.pack(pady=30)


def register():
    clear()

    title_label("CREATE ACCOUNT")

    card = Frame(
        window,
        bg=CARD,
        width=420,
        height=350
    )
    card.pack(pady=10)
    card.pack_propagate(False)

    Label(
        card,
        text="Username",
        bg=CARD,
        fg=TEXT,
        font=("Arial", 12, "bold")
    ).pack(pady=(30, 5))

    username = Entry(
        card,
        font=("Arial", 14),
        bg="#303045",
        fg=TEXT,
        insertbackground=TEXT,
        relief=FLAT
    )
    username.pack(ipady=8, padx=50, fill="x")

    Label(
        card,
        text="Password",
        bg=CARD,
        fg=TEXT,
        font=("Arial", 12, "bold")
    ).pack(pady=(20, 5))

    password = Entry(
        card,
        show="*",
        font=("Arial", 14),
        bg="#303045",
        fg=TEXT,
        insertbackground=TEXT,
        relief=FLAT
    )
    password.pack(ipady=8, padx=50, fill="x")

    def create_account():
        user = username.get().strip()
        pwd = password.get()

        if not user or not pwd:
            messagebox.showwarning(
                "Warning",
                "Enter username and password"
            )
            return

        users = get_users()

        for item in users:
            if item["Username"].lower() == user.lower():
                messagebox.showerror(
                    "Error",
                    "This username already exists"
                )
                return

        users.append({
            "Username": user,
            "Password": hash_password(pwd),
            "Score": 0
        })

        save_users(users)

        messagebox.showinfo(
            "Success",
            "Account created successfully"
        )

        login()

    Button(
        card,
        text="CREATE ACCOUNT",
        command=create_account,
        bg=GREEN,
        fg="white",
        activebackground=GREEN,
        activeforeground="white",
        relief=FLAT,
        font=("Arial", 11, "bold"),
        width=25,
        height=2
    ).pack(pady=25)

    Button(
        window,
        text="BACK TO LOGIN",
        command=login,
        bg=BUTTON,
        fg="white",
        activebackground=BUTTON,
        relief=FLAT,
        width=20,
        height=2
    ).pack()


def login():
    clear()

    title_label("NOVA CLICK")

    Label(
        window,
        text="LOGIN",
        bg=BG,
        fg=GRAY,
        font=("Arial", 14)
    ).pack()

    card = Frame(
        window,
        bg=CARD,
        width=420,
        height=330
    )
    card.pack(pady=20)
    card.pack_propagate(False)
    Label(
        card,
        text="Username",
        bg=CARD,
        fg=TEXT,
        font=("Arial", 12, "bold")
    ).pack(pady=(30, 5))

    username = Entry(
        card,
        font=("Arial", 14),
        bg="#303045",
        fg=TEXT,
        insertbackground=TEXT,
        relief=FLAT
    )
    username.pack(ipady=8, padx=50, fill="x")

    Label(
        card,
        text="Password",
        bg=CARD,
        fg=TEXT,
        font=("Arial", 12, "bold")
    ).pack(pady=(20, 5))

    password = Entry(
        card,
        show="*",
        font=("Arial", 14),
        bg="#303045",
        fg=TEXT,
        insertbackground=TEXT,
        relief=FLAT
    )
    password.pack(ipady=8, padx=50, fill="x")

    def login_account():
        global current_user
        global b
        global one_click_two_points

        user = username.get().strip()
        pwd = hash_password(password.get())

        users = get_users()

        for item in users:
            if (
                item["Username"].lower() == user.lower()
                and item["Password"] == pwd
            ):
                current_user = item["Username"]
                b = int(item["Score"])
                one_click_two_points = "off"
                main_menu()
                return

        messagebox.showerror(
            "Login Failed",
            "Username or password is incorrect"
        )

    Button(
        card,
        text="LOGIN",
        command=login_account,
        bg=BUTTON,
        fg="white",
        activebackground=BUTTON,
        relief=FLAT,
        font=("Arial", 11, "bold"),
        width=25,
        height=2
    ).pack(pady=25)

    Button(
        window,
        text="CREATE ACCOUNT",
        command=register,
        bg=GREEN,
        fg="white",
        activebackground=GREEN,
        relief=FLAT,
        width=20,
        height=2
    ).pack()


def update_score():
    users = get_users()

    for user in users:
        if user["Username"] == current_user:
            user["Score"] = b
            break

    save_users(users)


def click():
    global b

    if one_click_two_points == "on":
        b += 2
    else:
        b += 1

    score_label.config(text=str(b))
    update_score()


def ability():
    clear()

    title_label("ABILITIES")

    card = Frame(
        window,
        bg=CARD,
        width=500,
        height=350
    )
    card.pack(pady=10)
    card.pack_propagate(False)

    Label(
        card,
        text="ONE CLICK TWO POINTS",
        bg=CARD,
        fg=TEXT,
        font=("Arial", 18, "bold")
    ).pack(pady=(30, 5))

    Label(
        card,
        text="Cost: 20 Points",
        bg=CARD,
        fg=GRAY,
        font=("Arial", 12)
    ).pack(pady=5)

    status = "ON" if one_click_two_points == "on" else "OFF"

    status_label = Label(
        card,
        text=f"STATUS: {status}",
        bg=CARD,
        fg=GREEN if status == "ON" else RED,
        font=("Arial", 14, "bold")
    )
    status_label.pack(pady=15)

    def o_c_t_p():
        global one_click_two_points
        global b

        if one_click_two_points == "off":

            if b >= 20:
                one_click_two_points = "on"
                b -= 20
                update_score()

                status_label.config(
                    text="STATUS: ON",
                    fg=GREEN
                )

                messagebox.showinfo(
                    "Ability Activated",
                    "One Click Two Points is now ON"
                )

            else:
                messagebox.showwarning(
                    "Warning",
                    "You don't have enough points"
                )

        else:
            one_click_two_points = "off"

            status_label.config(
                text="STATUS: OFF",
                fg=RED
            )

    Button(
        card,
        text="ACTIVATE / DEACTIVATE",
        command=o_c_t_p,
        bg=BUTTON,
        fg="white",
        activebackground=BUTTON,
        relief=FLAT,
        width=25,
        height=2
    ).pack(pady=15)
    Button(
        window,
        text="MAIN MENU",
        command=main_menu,
        bg=GREEN,
        fg="white",
        activebackground=GREEN,
        relief=FLAT,
        width=20,
        height=2
    ).pack(pady=20)


def leaderboard():
    clear()

    title_label("LEADERBOARD")

    users = get_users()

    users.sort(
        key=lambda x: int(x["Score"]),
        reverse=True
    )

    frame = Frame(
        window,
        bg=CARD
    )
    frame.pack(
        padx=40,
        pady=10,
        fill="both",
        expand=True
    )

    headers = ["RANK", "USERNAME", "SCORE"]

    for col, text in enumerate(headers):
        Label(
            frame,
            text=text,
            bg="#303045",
            fg=TEXT,
            font=("Arial", 12, "bold"),
            width=20,
            height=2
        ).grid(
            row=0,
            column=col,
            sticky="nsew"
        )

    for rank, user in enumerate(users[:10], 1):

        username = user["Username"]
        score = int(user["Score"])

        if username == current_user:
            fg = GREEN
        else:
            fg = TEXT

        Label(
            frame,
            text=str(rank),
            bg=CARD,
            fg=fg,
            font=("Arial", 12, "bold")
        ).grid(
            row=rank,
            column=0,
            pady=5
        )

        Label(
            frame,
            text=username,
            bg=CARD,
            fg=fg,
            font=("Arial", 12)
        ).grid(
            row=rank,
            column=1,
            pady=5
        )

        Label(
            frame,
            text=str(score),
            bg=CARD,
            fg=fg,
            font=("Arial", 12, "bold")
        ).grid(
            row=rank,
            column=2,
            pady=5
        )

    Button(
        window,
        text="MAIN MENU",
        command=main_menu,
        bg=BUTTON,
        fg="white",
        activebackground=BUTTON,
        relief=FLAT,
        width=20,
        height=2
    ).pack(pady=15)


def logout():
    global current_user
    global b
    global one_click_two_points

    update_score()

    current_user = ""
    b = 0
    one_click_two_points = "off"

    login()


def main_menu():
    clear()

    top = Frame(
        window,
        bg=BG
    )
    top.pack(fill="x")

    Label(
        top,
        text=f"PLAYER: {current_user}",
        bg=BG,
        fg=GRAY,
        font=("Arial", 12, "bold")
    ).pack(
        side="left",
        padx=20,
        pady=15
    )

    Button(
        top,
        text="LOGOUT",
        command=logout,
        bg=RED,
        fg="white",
        activebackground=RED,
        relief=FLAT
    ).pack(
        side="right",
        padx=20
    )

    Label(
        window,
        text="NOVA CLICK",
        bg=BG,
        fg=TEXT,
        font=("Arial", 30, "bold")
    ).pack(pady=20)

    score_card = Frame(
        window,
        bg=CARD,
        width=400,
        height=110
    )
    score_card.pack(pady=5)
    score_card.pack_propagate(False)

    global score_label

    score_label = Label(
        score_card,
        text=str(b),
        bg=CARD,
        fg=GREEN,
        font=("Arial", 35, "bold")
    )
    score_label.pack(pady=25)

    Button(
        window,
        text="CLICK",
        command=click,
        bg=BUTTON,
        fg="white",
        activebackground=BUTTON,
        activeforeground="white",
        relief=FLAT,
        font=("Arial", 16, "bold"),
        width=25,
        height=3
    ).pack(pady=25)

    bottom = Frame(
        window,
        bg=BG
    )
    bottom.pack(
        side="bottom",
        fill="x",
        pady=20
    )

    Button(
        bottom,
        text="ABILITIES",
        command=ability,
        bg=GREEN,
        fg="white",
        activebackground=GREEN,
        relief=FLAT,
        width=15,
        height=2
    ).pack(
        side="left",
        padx=20
    )
    Button(
        bottom,
        text="LEADERBOARD",
        command=leaderboard,
        bg=BUTTON,
        fg="white",
        activebackground=BUTTON,
        relief=FLAT,
        width=15,
        height=2
    ).pack(
        side="right",
        padx=20
    )


create_file()
login()
window.mainloop()