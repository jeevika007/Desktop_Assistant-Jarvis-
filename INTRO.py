from tkinter import *  # pip install tkinter
from PIL import Image, ImageTk, ImageSequence  # pip install Pillow
import time

root = Tk()
root.geometry("1200x700")


def play_gif():
    root.lift()
    root.attributes("-topmost", True)
    global img
    img = Image.open("j_a_r_v_i_s_ui_by_drkdna_da2h0ba.gif")
    lbl = Label(root)
    lbl.place(x=0, y=0)
    i = 0
    for img in ImageSequence.Iterator(img):
        img = img.resize((1200, 700))
        img = ImageTk.PhotoImage(img)
        lbl.config(image=img)
        root.update()
        time.sleep(0.05)
    # root.destroy()


#play_gif()


