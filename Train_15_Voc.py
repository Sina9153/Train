from tkinter import *

root = Tk()
root.title("Vocabulary")
root.geometry("700x800")

words = {
"accomplishment":"Winning the competition was a great accomplishment because I worked hard for many years.",
"achieve":"She achieved her goal after studying and practicing every day.",
"ahead":"Our team is ahead of the others because we have more points.",
"arrest":"The police arrested the criminal after they found strong evidence.",
"attack":"The animal attacked the man when he got too close.",
"burglar":"The burglar entered the house at night and stole valuable things.",
"bury":"They decided to bury the treasure in a secret place.",
"cab":"I took a cab to the airport because I was late.",
"career":"She wants to have a successful career in medicine.",
"case":"The detective is working on a difficult case.",
"chief":"The police chief gave an important speech about safety.",
"concern":"Parents always concern themselves with their children's future.",
"convince":"He tried to convince his friend to tell the truth.",
"crime":"Stealing money from people is a serious crime.",
"criminal":"The criminal was caught by the police after a long investigation.",
"detective":"The detective solved the mystery by finding hidden clues.",
"disappointed":"She was disappointed because she did not get the result she wanted.",
"effort":"Success requires a lot of effort and patience.",
"fellow":"He is a nice fellow who always helps other people.",
"forgery":"The expert discovered that the painting was a forgery.",
"guilty":"The man was found guilty after the court examined the evidence.",
"hide":"The child tried to hide behind the door during the game.",
"hid hidden":"The thief hid the stolen money in a hidden place.",
"jaywalking":"Jaywalking can be dangerous because cars may not stop in time.",
"litter":"People should not litter the streets because it makes the city dirty.",
"mystery":"The strange event remained a mystery for many years.",
"political":"They talked about an important political issue on television.",
"possession":"The phone was in his possession when the police found him.",
"prove":"She needs to prove that her answer is correct.",
"peace":"Everyone hopes to live in a world full of peace.",
"pickpocketing":"Pickpocketing is a crime that often happens in crowded places.",
"punishment":"The punishment was given because he broke the rules.",
"reason":"Can you reason with him and explain why this is wrong?",
"reward":"The winner received a valuable reward for his hard work.",
"satisfy":"The delicious food satisfied everyone at the party.",
"scene":"The detective carefully examined the crime scene.",
"set up":"They set up a new business after saving enough money.",
"steal":"You should never steal something that belongs to another person.",
"stole stolen":"He stole a valuable item, but it was later found stolen by the police.",
"square":"The room has a square shape with four equal sides.",
"thief":"The thief ran away before the police arrived.",
"thoroughly":"You should read the instructions thoroughly before starting.",
"thump":"I heard a loud thump when the box fell on the floor.",
"valuable":"This old watch is very valuable because it is rare.",
"let us say":"Let us say you have one million dollars; what would you buy?",
"kind of":"I am kind of tired because I studied all night.",
"out of sight":"The keys were out of sight under the table.",
"every inch":"The detective searched every inch of the room carefully.",
"in vain":"They tried to open the door, but their efforts were in vain.",
"turn out to be":"The strange person turned out to be a famous actor."
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