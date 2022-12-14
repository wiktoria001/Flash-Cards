from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
index = 0
# --------------------------- CREATE FLASHCARDS ---------------------------- #

# 1.The csv file is made into Pandas DataFrame
words_df = pandas.read_csv("data/french_words.csv")  # <--- this is a pandas DataFrame
# 2. In order to make the csv file a dictionary
words = words_df.to_dict(orient="records")  # <--- a pandas DataFrame made into a Dictionary

# Create a words_to_learn file that had french_words as a base
try:
    with open("data/words_to_learn.csv", "r") as file:
        file.read()
except FileNotFoundError:
    with open("data/french_words.csv", "r") as file:
        contents = file.read()
    with open("data/words_to_learn.csv", "w") as file:
        file.write(contents)

words_to_learn_df = pandas.read_csv("data/words_to_learn.csv")
words_to_learn = words_to_learn_df.to_dict(orient="records") # <--- LIST of dictionaries

# I wanted to add "Show learned words" option - maybe some other day?


def know():
    global words_to_learn, words_to_learn_df
    try:
        current_word = words_to_learn[index]["French"]
    except IndexError:
        next_card()
    else:
        words_to_learn_df.drop(index, axis=0, inplace=True)
        words_to_learn_df.to_csv("data/words_to_learn.csv", index=False)

        words_to_learn_df = pandas.read_csv("data/words_to_learn.csv")
        words_to_learn = words_to_learn_df.to_dict(orient="records")  # <--- a List of Dictionaries

        next_card()


def show_meaning():
    canvas.tag_raise(card_back)
    canvas.tag_raise(title)
    canvas.tag_raise(word)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=words_to_learn[index]["English"], fill="white")


def next_card():
    global index, flip_timer
    window.after_cancel(flip_timer)
    with open("data/words_to_learn.csv", "r") as f:
        f.read()
    try:
        index = random.randint(0, (len(words_to_learn) - 1))
    except ValueError:
        canvas.itemconfig(word, text="No words left", fill="black")
    else:
        canvas.tag_raise(card_front)
        canvas.tag_raise(title)
        canvas.tag_raise(word)
        canvas.itemconfig(title, text="French", fill="black")

    # INDEX ERROR
    try:
        canvas.itemconfig(word, text=words_to_learn[index]["French"], fill="black")
        flip_timer = window.after(3000, show_meaning)
    except IndexError:
        canvas.tag_raise(card_front)
        canvas.tag_raise(word)
        canvas.itemconfig(word, text="No words left", fill="black")


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
tick = Button(command=know, image=tick_img, highlightthickness=0, borderwidth=0, activebackground=BACKGROUND_COLOR)
tick.grid(column=1, row=1)

words_learned_img = PhotoImage(file="./images/button_show-learned-words.png")
words_learned = Button(image=words_learned_img, highlightthickness=0, borderwidth=0, activebackground=BACKGROUND_COLOR)
words_learned.grid(column=1, row=1, sticky=E)

next_card()

window.mainloop()
