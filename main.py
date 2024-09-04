from pandas.core.internals.construction import dataclasses_to_dicts

BACKGROUND_COLOR = "#B1DDC6"
import pandas
import random
data=pandas.read_csv("data/french_words.csv")
to_learn=data.to_dict(orient="records")
french={}
def next_card():
    global french,flip_timer
    window.after_cancel(flip_timer)
    french=random.choice(to_learn)
    learn=french["French"]
    canvas.itemconfig(flash_image, image=front)
    canvas.itemconfig(card_title,text="FRENCH",fill="black")
    canvas.itemconfig(card_word, text=learn,fill="black")
    flip_timer=window.after(3000,flip_card)


def flip_card():
    canvas.itemconfig(flash_image,image=back)
    canvas.itemconfig(card_title, text="ENGLISH",fill="white")
    canvas.itemconfig(card_word, text=french["English"],fill="white")

def is_known():
    to_learn.remove(french)
    data=pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn")
    next_card()




from tkinter import *
window=Tk()
window.configure(padx=50,pady=50,bg=BACKGROUND_COLOR)
flip_timer=window.after(3000,flip_card)
canvas=Canvas(width=800,height=526)
front=PhotoImage(file="images/card_front.png", width=800, height=526)
back=PhotoImage(file="images/card_back.png", width=800, height=526)
flash_image=canvas.create_image(400,263,image=front)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(column=0,row=0,columnspan=2)
right=PhotoImage(file="images/right.png")
rightB=Button(image=right,highlightthickness=0,command=is_known)
rightB.grid(column=0,row=1)
wrong=PhotoImage(file="images/wrong.png")
wrongB=Button(image=wrong,highlightthickness=0,command=flip_card)
wrongB.grid(column=1,row=1)
card_title=canvas.create_text(400,150,text="title",font=("Ariel",40,"bold"))
card_word=canvas.create_text(400,264,text="word",font=("Ariel",60,"italic"))
next_card()
window.mainloop()