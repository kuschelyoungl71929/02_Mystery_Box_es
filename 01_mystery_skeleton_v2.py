
from tkinter import *
from functools import partial
import random

class Start:
    def __init__(self, parent):

       
        self.start_frame = Frame(padx=10,bg="#D4E6F1")
        self.start_frame.grid()

        self.starting_funds = IntVar()

        self.mystery_box_label = Label(self.start_frame, text="Mystery Box Game",font="times 18 bold underline",pady=20, padx=10,bg="#D4E6F1")
        self.mystery_box_label.grid(row=1)

        self.funds_frame = Frame(self.start_frame, width=45, bg="#D4E6F1")
        self.funds_frame.grid(row=2)

        # entry box
        self.start_entry = Entry(self.funds_frame, font="times 16 bold")
        self.start_entry.grid(row=2,pady=10)

        self.amount_error = Label(self.funds_frame , text="",bg="#D4E6F1", fg="#9B0019",font="times 12 bold", justify=LEFT, wrap =200)
        self.amount_error.grid(row=3,pady=5)

        self.button_frame = Frame(self.start_frame, width=45, bg="#D4E6F1")
        self.button_frame.grid(row=4,pady=10)

        # low stakes button
        self.low_stakes = Button(self.button_frame, text="Low ($5)",bg="#9FE2BF",font="times 12 bold",command=lambda: self.to_game(1))
        self.low_stakes.grid(row=0,column=0)

        # medium stakes button 
        self.medium_stakes = Button(self.button_frame, text="Medium ($10)",bg="#FFC300",font="times 12 bold",command=lambda: self.to_game(2))
        self.medium_stakes.grid(row=0,column=1,padx=5)
        
        # High_stakes
        self.high_stakes = Button(self.button_frame,text="High ($15)",bg="#FF5733",font="times 12 bold",command=lambda: self.to_game(3))
        self.high_stakes.grid(row=0,column=2,padx=5)

        self.instruction = Button(self.button_frame, text="How to play",bg="#C4B4F3",fg="white",font="times 12 bold")
        self.instruction.grid(row=1, column=1,pady=20)

        self.add_funds = Button(self.funds_frame , width=10, text="Add Funds",font="times 12 bold", command=self.check_funds)
        self.add_funds.grid(row=2,column=1,pady=10)

    def check_funds(self, stakes):
        start_balance = self.start_entry.get()
        error_bkg = "#ffafaf"
        has_errors = "no"
        self.start_entry.config(bg="white")
        self.amount_error.config(text="")

        self.low_stakes.config(state=DISABLED)
        self.medium_stakes.config(state=DISABLED)
        self.high_stakes.config(state=DISABLED)

        try:
            start_balance = int(start_balance)

            if start_balance < 5:
                has_errors="yes"
                error_text = "Sorry, the least you can play with is $5"


            elif start_balance >50:
                has_errors="yes" 
                error_text = "Too much! The most you can risk in this game is $50, seek recovery for your gambling addiction"
            
            elif start_balance <10 and stakes == 2 or stakes == 3:
                has_errors = "yes"
                error_text = "Balance insuffiecient for selected game"

            elif start_balance < 15 and stakes == 3:
                has_errors = "yes"
                error_text = "Balance insuffiecient for selected game"

        except ValueError:
            has_errors = "yes"
            error_text = "Please enter a whole number value amount" 
            
        if has_errors == "yes":
            self.start_entry.config(bg=error_bkg)
            self.amount_error.config(text=error_text)

        else:

            self.starting_funds.set(start_balance)
            

    def to_game(self, stakes):
        
        start_balance = self.starting_funds.get()

        Game(self,stakes,start_balance)

        root.withdraw()

class Game:
    def __init__(self, partner, stakes, start_balance):
        print(stakes)
        print(start_balance)
        partner.low_stakes.config(state=DISABLED)
        partner.medium_stakes.config(state=DISABLED)
        partner.high_stakes.config(state=DISABLED)

        self.balance = IntVar()

        self.balance.set(start_balance)

        self.game_box = Toplevel()
        self.game_frame = Frame(self.game_box,padx=10,bg="#D4E6F1")
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
        current_balance = self.balance.get()

        current_balance += 2

        self.balance.set(current_balance)

        self.balance_label.configure(text="Balance: {}".format(current_balance))

if __name__ == "__main__":
    root = Tk()
    root.title("title goes here")
    something = Start(root)
    root.mainloop()