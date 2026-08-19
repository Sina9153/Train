from tkinter import *

root = Tk()
root.title("English Learning")
root.geometry("700x800")


# =========================
# Vocabulary
# =========================

words = {
    "affair": "The government has to deal with important public affairs.",
    "attach": "Please attach the baggage tag to your ticket.",
    "beat": "Our team beat the other team in the final match.",
    "beneficial": "Exercise is beneficial for your health.",
    "build up": "You need to build up your confidence before the competition.",
    "charity": "She gave some of her money to charity.",
    "check in": "We arrived at the airport early to check in.",
    "effect": "The new rule had a positive effect on the students.",
    "depressed": "He felt depressed after losing his job.",
    "disc jockey": "The disc jockey played some great music at the party.",
    "drop off": "My father will drop me off at school.",
    "drowsy": "I felt drowsy after taking the medicine.",
    "embarrassed": "She felt embarrassed when she made a mistake in class.",
    "fire": "The workers decided to fire him because he was always late.",
    "go without": "We had to go without electricity for several hours.",
    "heal": "It took several weeks for his injury to heal.",
    "limit": "There is a limit to the amount of luggage you can take.",
    "maintenance": "The car needs regular maintenance.",
    "nightmare": "I had a terrible nightmare last night.",
    "nod off": "I started to nod off while watching TV.",
    "ordeal": "The long journey was a difficult ordeal for them.",
    "organize": "We need to organize the meeting carefully.",
    "raise": "The company decided to raise the workers' salaries.",
    "reckon": "I reckon he will arrive soon.",
    "REM sleep": "People usually have vivid dreams during REM sleep.",
    "scale": "Put your luggage on the scale, please.",
    "siesta": "My grandfather usually takes a short siesta after lunch.",
    "sleepwalker": "The sleepwalker walked into the hallway during the night.",
    "sort out": "I need to sort out this problem before tomorrow.",
    "sound": "You sound tired today.",
    "survive": "The family managed to survive the difficult situation.",
    "tag": "The clerk attached a tag to my suitcase.",
    "telly": "We watched a movie on the telly last night.",
    "tricky": "This question is quite tricky.",
    "twitch": "His eye began to twitch because he was tired.",
    "move": "Please move your chair a little to the left.",

    "burst into flames": "The old car suddenly burst into flames.",
    "on sb's side": "Don't worry. I'm on your side.",
    "to some extent": "I agree with you to some extent.",
    "up to": "You can borrow up to three books from the library."
}


# =========================
# Persian meanings + synonyms
# =========================

meanings = {
    "affair": ("موضوع / امور", "matter"),
    "attach": ("وصل کردن / پیوست کردن", "connect"),
    "beat": ("شکست دادن", "defeat"),
    "beneficial": ("مفید", "useful"),
    "build up": ("تقویت کردن / افزایش دادن", "develop"),
    "charity": ("خیریه", "aid"),
    "check in": ("پذیرش کردن / ثبت ورود کردن", "register"),
    "effect": ("تأثیر", "impact"),
    "depressed": ("افسرده / ناراحت", "sad"),
    "disc jockey": ("دی‌جی", "DJ"),
    "drop off": ("رساندن / پیاده کردن", "deliver"),
    "drowsy": ("خواب‌آلود", "sleepy"),
    "embarrassed": ("خجالت‌زده", "ashamed"),
    "fire": ("اخراج کردن", "dismiss"),
    "go without": ("بدون چیزی سر کردن", "manage without"),
    "heal": ("بهبود یافتن / خوب شدن", "recover"),
    "limit": ("محدودیت", "restriction"),
    "maintenance": ("تعمیر و نگهداری", "upkeep"),
    "nightmare": ("کابوس", "bad dream"),
    "nod off": ("چرت زدن", "doze"),
    "ordeal": ("تجربه سخت", "hardship"),
    "organize": ("سازمان‌دهی کردن", "arrange"),

"raise": ("افزایش دادن", "increase"),
    "reckon": ("فکر کردن / گمان کردن", "think"),
    "REM sleep": ("خواب REM", "dream sleep"),
    "scale": ("ترازو", "weighing machine"),
    "siesta": ("چرت بعدازظهر", "nap"),
    "sleepwalker": ("خواب‌گرد", "somnambulist"),
    "sort out": ("حل و فصل کردن", "resolve"),
    "sound": ("به نظر رسیدن", "seem"),
    "survive": ("زنده ماندن / دوام آوردن", "endure"),
    "tag": ("برچسب", "label"),
    "telly": ("تلویزیون", "TV"),
    "tricky": ("دشوار / پیچیده", "difficult"),
    "twitch": ("پرش کردن / لرزیدن", "jerk"),
    "move": ("حرکت کردن / جابه‌جا کردن", "shift"),

    "burst into flames": ("آتش گرفتن ناگهانی", "catch fire"),
    "on sb's side": ("طرف کسی بودن", "support"),
    "to some extent": ("تا حدی", "partly"),
    "up to": ("تا / حداکثر", "as much as")
}


# =========================
# Conversation
# =========================

conversation = """At the Airport

Mr. Sina is checking in at the airport.

Check-in clerk: Please put your luggage on the scales.

Mr. Sina: Here you are. I think it's within the allowed weight.

Check-in clerk: I'm afraid your luggage is way too heavy.

Mr. Sina: Oh, really? How much does it weigh?

Check-in clerk: It weighs almost 33 kilos. The maximum is 30 kilos.

Mr. Sina: It's because of the books. I'll take them onto the plane with me.

Check-in clerk: That's fine. I've attached the baggage tag to your ticket.

Mr. Sina: Thank you. What should I do next?

Check-in clerk: Please go to passport control.
"""


# =========================
# Clear window
# =========================

def clear_window():
    for widget in root.winfo_children():
        widget.destroy()


# =========================
# Home
# =========================

def home():
    clear_window()

    Label(
        root,
        text="English Learning",
        font=("Arial", 26, "bold")
    ).pack(pady=100)

    Button(
        root,
        text="Vocabulary",
        font=("Arial", 16, "bold"),
        width=20,
        height=2,
        command=show_vocabulary
    ).pack(pady=15)

    Button(
        root,
        text="Conversation",
        font=("Arial", 16, "bold"),
        width=20,
        height=2,
        command=show_conversation
    ).pack(pady=15)


# =========================
# Show word information
# =========================

def show_word(word):

    example_label.config(
        text=words[word]
    )

    meaning_label.config(
        text="Meaning: " + meanings[word][0]
    )

    synonym_label.config(
        text="Synonym: " + meanings[word][1]
    )


# =========================
# Vocabulary page
# =========================

def show_vocabulary():

    clear_window()

    Button(
        root,
        text="← Back",
        command=home
    ).pack(
        anchor="w",
        padx=10,
        pady=5
    )

    Label(
        root,
        text="Vocabulary",
        font=("Arial", 24, "bold")
    ).pack(pady=5)


    # =================================
    # INFORMATION BOX
    # =================================

    info_box = Frame(
        root,
        bd=3,
        relief="groove",
        padx=15,
        pady=15
    )

    info_box.pack(
        fill="x",
        padx=20,
        pady=10
    )

    Label(
        info_box,
        text="Example sentence",
        font=("Arial", 12, "bold")
    ).pack()

    global example_label
    example_label = Label(
        info_box,
        text="Click a word",
        font=("Arial", 12),
        wraplength=600
    )

    example_label.pack(pady=8)

    global meaning_label
    meaning_label = Label(
        info_box,
        text="Meaning: ---",
        font=("Arial", 12)
    )

    meaning_label.pack(pady=3)

    global synonym_label
    synonym_label = Label(
        info_box,
        text="Synonym: ---",
        font=("Arial", 12)
    )

    synonym_label.pack(pady=3)


    # =================================
    # WORDS AREA
    # =================================

    words_frame = Frame(root)
    words_frame.pack(
        fill="both",
        expand=True,
        padx=10,
        pady=10
    )

    canvas = Canvas(words_frame)

    scrollbar = Scrollbar(
        words_frame,
        orient="vertical",
        command=canvas.yview
    )

    buttons_frame = Frame(canvas)

    buttons_frame.bind(
        "<Configure>",
        lambda event: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window(
        (0, 0),
        window=buttons_frame,
        anchor="nw"
    )

    canvas.configure(
        yscrollcommand=scrollbar.set
    )

    canvas.pack(
        side="left",
        fill="both",
        expand=True
    )

    scrollbar.pack(
        side="right",
        fill="y"
    )


    # =================================
    # CREATE WORD BUTTONS
    # =================================

    row = 0
    col = 0

    for word in words:

        Button(
            buttons_frame,
            text=word,
            width=18,
            command=lambda w=word: show_word(w)
        ).grid(
            row=row,
            column=col,
            padx=4,
            pady=4
        )

        col += 1

        if col == 3:
            col = 0
            row += 1


# =========================
# Conversation page
# =========================

def show_conversation():

    clear_window()

    Button(
        root,
        text="← Back",
        command=home
    ).pack(
        anchor="w",
        padx=10,
        pady=5
    )

    Label(
        root,
        text="At the Airport",
        font=("Arial", 24, "bold")
    ).pack(pady=10)


    frame = Frame(root)
    frame.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=10
    )

    scrollbar = Scrollbar(frame)
    scrollbar.pack(
        side="right",
        fill="y"
    )

    text_box = Text(
        frame,
        font=("Arial", 13),
        wrap="word",
        yscrollcommand=scrollbar.set
    )

    text_box.pack(
        side="left",
        fill="both",
        expand=True
    )

    scrollbar.config(
        command=text_box.yview
    )

    text_box.insert(
        "1.0",
        conversation
    )

    text_box.config(
        state="disabled"
    )


# =========================
# Start
# =========================

home()

root.mainloop()