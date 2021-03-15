rom tkinter import *
import pandas
import random

# --- CONSTANTS --- #
BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ('Ariel', 40, 'italic')
VOC_FONT = ('Ariel', 60, 'bold')


# --- READ DATA --- #
data = pandas.read_csv('data/russian_words.csv')
to_learn = data.to_dict(orient='records')
current_card = {}


# --- FLIP CARD --- #
def delay():
    window.after(3000, flip_card)


def random_voc():
    global current_card, timer
    window.after_cancel(timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(language_text, fill='black', text='Russian')
    canvas.itemconfig(voc_text, fill='black', text=current_card["Russian"])
    canvas.itemconfig(canvas_image, image=front_card_img)
    timer = window.after(3000, flip_card)


def flip_card():
    global current_card
    canvas.itemconfig(language_text, fill='white', text='English')
    canvas.itemconfig(voc_text, fill='white', text=current_card["English"])
    canvas.itemconfig(canvas_image, image=back_card_img)


# --- UI SETUP --- #
window = Tk()
window.title('Flash Card')
window.config(height=800, width=1000, padx=50, pady=50, bg=BACKGROUND_COLOR)


timer = window.after(3000, flip_card)

# Card Image
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card_img = PhotoImage(file='images/card_front.png')
back_card_img = PhotoImage(file='images/card_back.png')

canvas_image = canvas.create_image(400, 263, image=front_card_img)
canvas.grid(column=0, row=0, columnspan=2)


# Card Text
language_text = canvas.create_text(370, 110, font=LANGUAGE_FONT, text='Russian')
voc_text = canvas.create_text(380, 260, font=VOC_FONT, text='')


# Button
right_button_img = PhotoImage(file='images/right.png')
wrong_button_img = PhotoImage(file='images/wrong.png')

right_button = Button(image=right_button_img, highlightthickness=0, command=random_voc)
wrong_button = Button(image=wrong_button_img, highlightthickness=0, command=random_voc)

right_button.grid(column=0, row=1)
wrong_button.grid(column=1, row=1)


random_voc()

window.mainloop()
