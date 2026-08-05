from tkinter import *

root = Tk()
root.title("Vocabulary")
root.geometry("700x800")

words = {
    "age":"Age is just a number if you keep learning new things every day.",
    "afterward":"We finished our homework, and afterward we went to the park.",
    "appreciation":"She showed her appreciation by thanking everyone for their help.",
    "aspect":"One important aspect of learning English is practicing every day.",
    "beast":"The brave knight fought a dangerous beast in the forest.",
    "choice":"Choosing to study every day was the best choice he ever made.",
    "courtesy":"Showing courtesy to other people makes everyone feel respected.",
    "delighted":"She was delighted when she heard the good news about her exam.",
    "desk clerk":"The desk clerk welcomed us and gave us the room key.",
    "disappointment":"Losing the final match was a great disappointment for the team.",
    "drop off":"My father dropped me off at school before going to work.",
    "entitle":"This ticket entitles you to enter the museum for free.",
    "fancy":"I don't like fancy resturants. They're not really my thing.",
    "groan":"He groaned loudly because his leg was hurting badly.",
    "impression":"His kindness made a very good impression on everyone.",
    "mad":"She was mad because her little brother broke her favorite toy.",
    "member":"Every member of the club must follow the rules carefully.",
    "moan":"The patient began to moan because he was in great pain.",
    "moody":"He becomes moody whenever he does not get enough sleep.",
    "order":"The teacher asked the students to keep the classroom in order.",
    "point of view":"From my point of view, honesty is always the best policy.",
    "raging":"A raging storm caused serious damage to many houses.",
    "regarding":"I have a few questions regarding tomorrow's English test.",
    "sheer":"It was sheer luck that we caught the last bus home.",
    "splash out":"They decided to splash out on a new car after saving money for years.",
    "show off":"He likes to show off his new phone to his friends.",
    "sulk":"The little boy began to sulk after losing the game.",
    "sympathetic":"Our teacher was very sympathetic when she heard about the problem.",
    "trunk":"The elephant used its trunk to pick up some water.",
    "turn":"Please turn left when you reach the traffic lights.",
    "untidy":"His bedroom was so untidy that he could not find his books.",
    "wave":"She waved goodbye to her friends before getting on the bus.",
    "change one's mind":"He changed his mind after listening to his parents' advice.",
    "do one's bit":"Everyone should do their bit to protect the environment.",
    "every now and then":"Every now and then we visit our grandparents in the countryside.",
    "made of money":"I can't buy everything because I'm not made of money.",
    "no way":"There is no way I will cheat in the exam.",
    "on one's own":"She learned to cook on her own by watching videos online.",
    "pull faces":"The children pulled funny faces at each other and started laughing.",
    "right, left, and center":"The team won matches right, left, and center during the tournament."
}

label = Label(root, text="Click a word", font=("Arial",14), wraplength=400)
label.pack(pady=10)

frame = Frame(root)
frame.pack()

row = 0
col = 0

for w, s in words.items():
    Button(
        frame,
        text=w,
        width=15,
        command=lambda t=s: label.config(text=t)
    ).grid(row=row, column=col, padx=3, pady=2)

    col += 1
    if col == 4:      
        col = 0
        row += 1
root.mainloop()