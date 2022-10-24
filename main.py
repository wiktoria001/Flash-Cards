from tkinter import *
import pandas
import random
import time
BACKGROUND_COLOR = "#B1DDC6"

# --------------------------- CREATE FLASHCARDS ---------------------------- #
words_df = pandas.read_csv("data/french_words.csv")  # <--- this is a pandas DataFrame

words = words_df.to_dict(orient="records")  # <--- a pandas DataFrame made into a Dictionary
index = 0

def show_meaning():
    canvas.tag_raise(card_back)
    canvas.tag_raise(title)
    canvas.tag_raise(word)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=words[index]["English"], fill="white")

def next_card():
    global index, flip_timer
    window.after_cancel(flip_timer)
    index = random.randint(0, 100)
    canvas.tag_raise(card_front)
    canvas.tag_raise(title)
    canvas.tag_raise(word)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=words[index]["French"], fill="black")
    flip_timer = window.after(3000, show_meaning)

# -------------------------------- UI SETUP -------------------------------- #
window = Tk()
window.title("Flash Cards")
window.geometry("900x670")
window.config(bg=BACKGROUND_COLOR, pady=30, padx=50)

flip_timer = window.after(3000, show_meaning)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.grid(column=0, row=0, columnspan=2)

card_front_img = PhotoImage(file="./images/card_front.png")
card_front = canvas.create_image(400, 265, image=card_front_img)

card_back_img = PhotoImage(file="images/card_back.png")
card_back = canvas.create_image(400, 265, image=card_back_img)

title = canvas.create_text(400, 100, font=("Arial", 40, "italic"), text="")
word = canvas.create_text(400, 250, font=("Arial", 60, "bold"), text="")

cross_img = PhotoImage(file="./images/wrong.png")
cross = Button(command=next_card, image=cross_img, highlightthickness=0, borderwidth=0, activebackground=BACKGROUND_COLOR)
cross.grid(column=0, row=1)

tick_img = PhotoImage(file="./images/right.png")
tick = Button(command=next_card, image=tick_img, highlightthickness=0, borderwidth=0, activebackground=BACKGROUND_COLOR)
tick.grid(column=1, row=1)

next_card()

window.mainloop()
