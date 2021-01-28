"""trump quotes project by hamza"""
import requests
import tkinter
import random


def get_quote():
    data = requests.get(url='https://api.whatdoestrumpthink.com/api/v1/quotes')
    data.raise_for_status()
    quote = data.json()
    quote_to_show = random.choice(quote['messages']['non_personalized'])
    canvas.itemconfig(my_quote, text=quote_to_show)


window = tkinter.Tk()
window.config(padx=50, pady=50, bg='white')
window.title('Trump Says...')

label = tkinter.Label(text='Trump says...', fg='green', font=('Arial', 20, 'bold'), bg='white', highlightthickness=0)
label.grid(column=0, row=0)
canvas = tkinter.Canvas(width=300, height=414, bg='white', highlightthickness=0)
trump_img = tkinter.PhotoImage('trump.png')
background_img = tkinter.PhotoImage(file='background.png')
canvas.create_image(150, 207, image=background_img)
my_quote = canvas.create_text(150, 207, text='press the trump button to get quote', width=250,
                              font=("Arial", 19, "bold"), fill='black')
canvas.grid(column=0, row=1)

trump_img = tkinter.PhotoImage(file='rsz_1rsz_trump.png')
button = tkinter.Button(image=trump_img, bg='white', highlightthickness=0, command=get_quote)
button.grid(column=0, row=2)
# get_quote()
window.mainloop()
