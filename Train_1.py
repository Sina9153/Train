import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Calculator")
app.geometry("450x600")
app.resizable(False, False)

expression = ""

display = ctk.CTkEntry(
    app,
    width=340,
    height=70,
    font=("Arial", 28),
    justify="right"
)
display.pack(pady=20)

def press(value):
    global expression
    expression += str(value)
    display.delete(0, "end")
    display.insert(0, expression)

def clear():
    global expression
    expression = ""
    display.delete(0, "end")

def equal():
    global expression
    try:
        result = str(eval(expression))
        display.delete(0, "end")
        display.insert(0, result)
        expression = result
    except:
        display.delete(0, "end")
        display.insert(0, "Error")
        expression = ""

buttons = [
    ["C","%","/","*"],
    ["7","8","9","-"],
    ["4","5","6","+"],
    ["1","2","3","="],
    ["0",".","",""]
]

frame = ctk.CTkFrame(app, fg_color="transparent")
frame.pack()

for r, row in enumerate(buttons):
    for c, text in enumerate(row):
        if text == "":
            continue

        if text == "=":
            cmd = equal
            color = "#ff9500"
        elif text == "C":
            cmd = clear
            color = "#555555"
        else:
            cmd = lambda t=text: press(t)
            color = "#2b2b2b"

        btn = ctk.CTkButton(
            frame,
            text=text,
            command=cmd,
            width=75,
            height=75,
            corner_radius=38,
            font=("Arial", 24, "bold"),
            fg_color=color,
            hover_color="#444444"
        )

        btn.grid(row=r, column=c, padx=8, pady=8)

app.mainloop()