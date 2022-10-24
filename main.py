from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"

# -------------------------------- UI SETUP -------------------------------- #
window = Tk()
window.title("Flash Cards")
window.geometry("900x670")
window.config(bg=BACKGROUND_COLOR, pady=30, padx=50)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.grid(column=0, row=0, columnspan=2)

card_front_img = PhotoImage(file="./images/card_front.png")
card_front = canvas.create_image(400, 265, image=card_front_img)

title = canvas.create_text(400, 100, font=("Arial", 40, "italic"), text="Title")
word = canvas.create_text(400, 250, font=("Arial", 60, "bold"), text="word")

cross_img = PhotoImage(file="./images/wrong.png")
cross = Button(image=cross_img, highlightthickness=0, borderwidth=0, activebackground=BACKGROUND_COLOR)
cross.grid(column=0, row=1, sticky=W)

tick_img = PhotoImage(file="./images/right.png")
tick = Button(image=tick_img, highlightthickness=0, borderwidth=0, activebackground=BACKGROUND_COLOR)
tick.grid(column=1, row=1, sticky=E)





window.mainloop()
