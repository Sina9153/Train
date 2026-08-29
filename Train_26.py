from tkinter import *

window = Tk()
window.geometry("800x700")

canvas = Canvas(window, width=800, height=700, bg="lightblue")
canvas.pack()

canvas.create_polygon(
    100,100,
    180,80,
    230,130,
    190,190,
    110,180,
    fill="gray",
    outline="black"
)

window.mainloop()