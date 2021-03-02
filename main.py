from tkinter import *
import pandas
import random

# --- CONSTANTS --- #
BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ('Ariel', 40, 'italic')
VOC_FONT = ('Ariel', 60, 'bold')


# --- READ DATA --- #
data = pandas.read_csv('data/russian_words.csv')

english_voc = data['English'].to_list()


# --- DISPLAY RANDOM VOC --- #
russian_voc = data['Russian'].to_list()


def random_voc():
    random_voc = random.randint(0, len(russian_voc))
    russian_word = russian_voc[random_voc]
    canvas.itemconfig(voc_text, text=russian_word)
    #flip_card()
    
    
# --- UI SETUP --- #
window = Tk()
window.title('Flash Card')
window.config(height=800, width=1000, padx=50, pady=50, bg=BACKGROUND_COLOR)

# Card Image
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card_img = PhotoImage(file='images/card_front.png')
back_card_img = PhotoImage(file='images/card_back.png')

canvas_image = canvas.create_image(400, 263, image=front_card_img)
canvas.grid(column=0, row=0, columnspan=2)

# Card Text
language_text = canvas.create_text(370, 110, font=LANGUAGE_FONT, text='Language')
voc_text = canvas.create_text(380, 260, font=VOC_FONT, text='Voc')


# Button
right_button_img = PhotoImage(file='images/right.png')
wrong_button_img = PhotoImage(file='images/wrong.png')

right_button = Button(image=right_button_img, highlightthickness=0, command=random_voc)
wrong_button = Button(image=wrong_button_img, highlightthickness=0, command=random_voc)

right_button.grid(column=0, row=1)
wrong_button.grid(column=1, row=1)


window.mainloop()
