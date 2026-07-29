from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Mini Tools")
window.geometry("700x500")
window.configure(bg="#1e1e2f")


def clear():
    for widget in window.winfo_children():
        widget.destroy()


def main_menu():
    clear()

    Label(
        window,
        text="Mini Tools",
        font=("Arial",22,"bold"),
        bg="#1e1e2f",
        fg="white"
    ).pack(pady=20)

    Button(
        window,
        text="Password Checker",
        font=("Arial",14),
        width=25,
        command=password_page
    ).pack(pady=10)

    Button(
        window,
        text="Phone Number Cleaner",
        font=("Arial",14),
        width=25,
        command=phone_page
    ).pack(pady=10)

    Button(
        window,
        text="Text Analyzer",
        font=("Arial",14),
        width=25,
        command=text_page
    ).pack(pady=10)

    Button(
        window,
        text="Exit",
        font=("Arial",14),
        width=25,
        command=window.destroy
    ).pack(pady=10)


def password_page():

    clear()

    Label(
        window,
        text="Password Checker",
        font=("Arial",20,"bold"),
        bg="#1e1e2f",
        fg="white"
    ).pack(pady=20)

    Label(
        window,
        text="Enter Password",
        bg="#1e1e2f",
        fg="white"
    ).pack()

    entry = Entry(window,font=("Arial",15),show="*")
    entry.pack(pady=15)

    def check():

        password = entry.get()

        upper = False
        digit = False
        special = False

        if len(password) < 8:
            messagebox.showerror(
                "Error",
                "Password is too short!"
            )
            return

        if len(password) > 20:
            messagebox.showerror(
                "Error",
                "Password is too long!"
            )
            return

        for i in password:

            if i.isupper():
                upper = True

            if i.isdigit():
                digit = True

            if not i.isalnum():
                special = True

        if upper and digit and special:
            messagebox.showinfo(
                "Success",
                "Your Password Is Strong!"
            )
        else:
            messagebox.showerror(
                "Weak Password",
                "Password must contain:\n"
                "• Uppercase Letter\n"
                "• Number\n"
                "• Special Character"
            )

    Button(
        window,
        text="Check",
        command=check,
        font=("Arial",14),
        width=15
    ).pack(pady=15)

    Button(
        window,
        text="Back",
        command=main_menu,
        font=("Arial",12)
    ).pack()

def phone_page():

    clear()

    Label(
        window,
        text="Phone Number Cleaner",
        font=("Arial",20,"bold"),
        bg="#1e1e2f",
        fg="white"
    ).pack(pady=20)

    Label(
        window,
        text="Enter Phone Number",
        bg="#1e1e2f",
        fg="white"
    ).pack()

    entry = Entry(window,font=("Arial",15))
    entry.pack(pady=15)

    def check_phone():

        phone = entry.get()

        phone = phone.replace(" ","")
        phone = phone.replace("-","")
        phone = phone.replace("(","")
        phone = phone.replace(")","")

        if not phone.startswith("+98"):
            messagebox.showerror(
                "Error",
                "Phone number must start with +98"
            )
            return

        if len(phone) != 13:
            messagebox.showerror(
                "Error",
                "Phone number is not valid."
            )
            return

        messagebox.showinfo(
            "Result",
            "Clean Number:\n" + phone
        )

    Button(
        window,
        text="Clean",
        command=check_phone,
        font=("Arial",14),
        width=15
    ).pack(pady=15)

    Button(
        window,
        text="Back",
        command=main_menu,
        font=("Arial",12)
    ).pack()

def text_page():

    clear()

    Label(
        window,
        text="Text Analyzer",
        font=("Arial",20,"bold"),
        bg="#1e1e2f",
        fg="white"
    ).pack(pady=20)

    Label(
        window,
        text="Enter Your Text",
        bg="#1e1e2f",
        fg="white"
    ).pack()

    text_box = Text(window, width=60, height=10, font=("Arial",12))
    text_box.pack(pady=15)

    def analyze():

        text = text_box.get("1.0", END).strip()

        words = len(text.split())

        sentences = (
            text.count(".") +
            text.count("!") +
            text.count("?")
        )

        upper = 0
        lower = 0
        digits = 0
        spaces = 0

        for ch in text:

            if ch.isupper():
                upper += 1

            elif ch.islower():
                lower += 1

            elif ch.isdigit():
                digits += 1

            elif ch == " ":
                spaces += 1

        total = len(text)

        messagebox.showinfo(
            "Result",
            f"""Words: {words}

Sentences: {sentences}

Uppercase: {upper}

Lowercase: {lower}

Numbers: {digits}

Spaces: {spaces}

Characters: {total}"""
        )

    Button(
        window,
        text="Analyze",
        command=analyze,
        font=("Arial",14),
        width=15
    ).pack(pady=10)

    Button(
        window,
        text="Back",
        command=main_menu,
        font=("Arial",12)
    ).pack()


main_menu()

window.mainloop()
