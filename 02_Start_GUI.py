
from tkinter import *
from functools import partial
import random

class Start:
    def __init__(self, parent):

        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        # mystery box label
        self.mystery_box_label = Label(self.start_frame, text="Mystery Box Game", font="arial, 16", justify=LEFT, padx=10, pady=10)
        self.mystery_box_label.grid(row=1)

        # entry box
        self.start_entry = Entry(self.start_frame, font="Arial 16 bold")
        self.start_entry.place(x=10, y=40, width=185, height=100)
        self.start_entry.grid()
        
        # low stakes button
        self.low_stakes = Button(text="Low ($5)", command=lambda: self.to_game(1))
        self.low_stakes.grid(row=2, pady=0)

    def to_game(self, stakes):
        start_balance = self.start_entry.get()
        Game(self, stakes, start_balance)


class Game:
    def __init__(self, partner, stakes, start_balance):
        print(stakes)
        print(start_balance)
        partner.low_stakes.config(state=DISABLED)

        self.balance = IntVar()

        self.balance.set(start_balance)

        self.game_box = Toplevel()
        self.game_frame = Frame(self.game_box)
        self.game_frame.grid()

        self.heading_label = Label(self.game_frame, text="Heading",
                                   font="Arial 24 bold", padx=10, pady=10)
        self.heading_label.grid(row=0)

        self.balance_frame = Frame(self.game_frame)
        self.balance_frame.grid(row=1)

        self.balance_label = Label(self.game_frame, text="Balance...")
        self.balance_label.grid(row=2)

        self.play_button = Button(self.game_frame, text="Gain", padx=10,
                                  pady=10, command=self.show_boxes)
        self.play_button.grid(row=3)

    def show_boxes(self):
        current_balance = self.balance.get
        current_balance += 2

        self.balance.set(current_balance)

        self.balance_label.configure(text="Balance: {}".format(current_balance))

if __name__ == "__main__":
    root = Tk()
    root.title("title goes here")
    something = Start(root)
    root.mainloop()