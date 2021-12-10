from pathlib import Path
import sys
import os
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import numpy as np
import pandas as pd

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./search_assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def to_home():
    window.destroy()
    os.system('python home_page.py')
    
def search_add():
    
    button_2.destroy()
    
    dt = pd.read_csv('data.csv')
    
    rslt_df = dt.sort_values(by = 'price', ascending = True)
    final_dt = rslt_df.reset_index(drop=True)
    
    value = int(entry_1.get())
    index = abs(final_dt['price'] - value).idxmin()
    
    ad1_s = final_dt.iloc[index+1]['street']
    ad2_s = final_dt.iloc[index-1]['street']
    ad3_s = final_dt.iloc[index+2]['street']

    ad1_c = final_dt.iloc[index+1]['city']
    ad2_c = final_dt.iloc[index-1]['city']
    ad3_c = final_dt.iloc[index+2]['city']

    ad1_p = final_dt.iloc[index+1]['price']
    ad2_p = final_dt.iloc[index-1]['price']
    ad3_p = final_dt.iloc[index+2]['price']



    add1 = "{}, {} , price = {} $".format(ad1_s,ad1_c,ad1_p)
    add2 = "{}, {} , price = {} $".format(ad2_s,ad2_c,ad2_p)
    add3 = "{}, {} , price = {} $".format(ad3_s,ad3_c,ad3_p)
    
    canvas.create_text(
    68.0,
    430.0,
    anchor="nw",
    text=add1,
    fill="#FFFFFF",
    font=("RobotoCondensed Regular", 24 * -1)
    )

    canvas.create_text(
        68.0,
        548.0,
        anchor="nw",
        text=add2,
        fill="#FFFFFF",
        font=("RobotoCondensed Regular", 24 * -1)
    )

    canvas.create_text(
        68.0,
        709.0,
        anchor="nw",
        text=add3,
        fill="#FFFFFF",
        font=("RobotoCondensed Regular", 24 * -1)
    )

window = Tk()

window.geometry("1440x1024")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
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
    512.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=to_home,
    relief="flat"
)
button_1.place(
    x=1095.0,
    y=928.0,
    width=306.0,
    height=65.0
)
button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=search_add,
    relief="flat"
)
button_2.place(
    x=31.0,
    y=928.0,
    width=306.0,
    height=65.0
)
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    1032.5,
    226.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0
)
entry_1.place(
    x=762.0,
    y=199.0,
    width=541.0,
    height=52.0
)
window.resizable(False, False)
window.mainloop()
