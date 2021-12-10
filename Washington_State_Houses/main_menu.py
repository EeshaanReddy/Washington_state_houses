from pathlib import Path
import sys
import os
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./main_assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def helloCallBack():
    window.destroy()
    os.system('python home_page.py')

def quit():
    window.destroy()


window = Tk()
window.geometry("1459x1024")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 1024,
    width = 1459,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    729.0,
    512.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=helloCallBack,
    relief="flat"
)
button_1.place(
    x=50.0,
    y=922.0,
    width=306.0,
    height=65.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=quit,
    relief="flat"
)
button_2.place(
    x=1133.0,
    y=922.0,
    width=306.0,
    height=65.0
)
window.resizable(False, False)
window.mainloop()
