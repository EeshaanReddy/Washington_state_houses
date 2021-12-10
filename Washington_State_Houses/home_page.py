from pathlib import Path
import sys
import os
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./home_assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def to_main_menu():
    window.destroy()
    os.system('python main_menu.py')
    
def to_predict():
    window.destroy()
    os.system('python predict_page.py')
    
def to_search():
    window.destroy()
    os.system('python search_page.py')


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
    command=to_search,
    relief="flat"
)
button_1.place(
    x=39.0,
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
    command=to_main_menu,
    relief="flat"
)
button_2.place(
    x=1095.0,
    y=928.0,
    width=306.0,
    height=65.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=to_predict,
    relief="flat"
)
button_3.place(
    x=567.0,
    y=928.0,
    width=306.0,
    height=65.0
)
window.resizable(False, False)
window.mainloop()
