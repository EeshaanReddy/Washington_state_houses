from pathlib import Path
import sys
import os
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import numpy as np
import pickle

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./predict_assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def to_home():
    window.destroy()
    os.system('python home_page.py')
    
def get_prediction():
    
    button_1.destroy()
    
    e1=entry_1.get()
    e2=entry_2.get()
    e3=entry_3.get()
    e4=entry_4.get()
    e5=entry_5.get()
    e6=entry_6.get()
    e7=entry_7.get()
    e8=entry_8.get()
    e9=entry_9.get()
    
    
    user_input = [[e1,e2,e3,e4,e5,e6,e7,e8,e9]]
    final_arr = np.asarray(user_input, dtype = np.float64, 
                        order ='C')
    
    with open('house_model','rb') as file:
        mp = pickle.load(file)
    
    user_pred = int(mp.predict(final_arr))

    canvas.create_text(
    644.0,
    699.0,
    anchor="nw",
    text="{} $".format(user_pred),
    fill="#FFFFFF",
    font=("RobotoCondensed Regular", 36 * -1)
)


window = Tk()

window.geometry("1440x1024")
window.configure(bg = "#000000")


canvas = Canvas(
    window,
    bg = "#000000",
    height = 1024,
    width = 1440,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    720.0,
    537.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=get_prediction,
    relief="flat"
)
button_1.place(
    x=39.0,
    y=927.0,
    width=306.0,
    height=65.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=to_home,
    relief="flat"
)
button_2.place(
    x=1095.0,
    y=927.0,
    width=306.0,
    height=65.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    786.0,
    192.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0
)
entry_1.place(
    x=689.0,
    y=180.0,
    width=194.0,
    height=22.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    786.0,
    271.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0
)
entry_2.place(
    x=689.0,
    y=259.0,
    width=194.0,
    height=22.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    786.0,
    350.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0
)
entry_3.place(
    x=689.0,
    y=338.0,
    width=194.0,
    height=22.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    786.0,
    429.0,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0
)
entry_4.place(
    x=689.0,
    y=417.0,
    width=194.0,
    height=22.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    1304.0,
    271.0,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0
)
entry_5.place(
    x=1207.0,
    y=259.0,
    width=194.0,
    height=22.0
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    1304.0,
    192.0,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0
)
entry_6.place(
    x=1207.0,
    y=180.0,
    width=194.0,
    height=22.0
)

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    1302.0,
    350.0,
    image=entry_image_7
)
entry_7 = Entry(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0
)
entry_7.place(
    x=1205.0,
    y=338.0,
    width=194.0,
    height=22.0
)

entry_image_8 = PhotoImage(
    file=relative_to_assets("entry_8.png"))
entry_bg_8 = canvas.create_image(
    1304.0,
    429.0,
    image=entry_image_8
)
entry_8 = Entry(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0
)
entry_8.place(
    x=1207.0,
    y=417.0,
    width=194.0,
    height=22.0
)

entry_image_9 = PhotoImage(
    file=relative_to_assets("entry_9.png"))
entry_bg_9 = canvas.create_image(
    1302.0,
    478.0,
    image=entry_image_9
)
entry_9 = Entry(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0
)
entry_9.place(
    x=1205.0,
    y=466.0,
    width=194.0,
    height=22.0
)

window.resizable(False, False)
window.mainloop()
