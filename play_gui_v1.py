from tkinter import *
from functools import partial
import random
from tkinter import filedialog
from PIL import Image, ImageTk

class Start:

    def __init__(self,parent):

        self.o_start_frame = Frame(padx=10,bg="#D4E6F1")
        self.o_start_frame.grid()

class Play:
    def __init__(self, parent):

       
        self.start_frame = Frame(padx=10,bg="#D4E6F1")
        self.start_frame.grid()

        self.starting_funds = IntVar()

        self.mystery_box_label = Label(self.start_frame, text="Play...",font="times 18 bold underline",pady=20, padx=10,bg="#D4E6F1")
        self.mystery_box_label.grid(row=1)

        self.instruction_start = Label(self.start_frame , text="Press Enter or click the 'Open Boxes' button to reveal the contents of the mystery boxes",bg="#D4E6F1",font="times 11", justify=LEFT, wrap=250)
        self.instruction_start.grid(row=2,pady=5)

        self.funds_frame = Frame(self.start_frame, width=45, bg="#D4E6F1")
        self.funds_frame.grid(row=5)

        self.amount_start = Label(self.funds_frame , text="Welcome, your starting balance is {}",bg="#D4E6F1",font="times 12 bold", justify=LEFT)
        self.amount_start.grid(row=0,pady=5)

        self.button_frame = Frame(self.start_frame, width=45, bg="#D4E6F1")
        self.button_frame.grid(row=6,pady=10)

        self.instruction = Button(self.button_frame, text="How to play",font="times 12 bold")
        self.instruction.grid(row=1, column=1,pady=20)

        self.stats = Button(self.button_frame, text="Game Stats...",font="times 12 bold")
        self.stats.grid(row=1, column=2,pady=20)

        self.add_funds = Button(self.start_frame , width=15, text="Open Boxes",font="times 16 bold")
        self.add_funds.grid(row=4,column=0,pady=10)


if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Box Game")
    something = Start(root)
    root.mainloop()