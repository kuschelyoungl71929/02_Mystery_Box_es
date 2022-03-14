
from tkinter import *
from functools import partial
import random

class Start:
    def __init__(self, parent):

       

        #D4E6F1 is blue


        self.start_frame = Frame(padx=10,bg="#D4E6F1")
        self.start_frame.grid()

        
        # mystery box label
        self.mystery_box_label = Label(self.start_frame, text="Mystery Box Game",font="times 18 bold underline",pady=20, padx=10,bg="#D4E6F1")
        self.mystery_box_label.grid(row=1)

        # entry box
        self.start_entry = Entry(self.start_frame, font="times 16 bold")
        self.start_entry.grid(row=2,pady=10)

        self.button_frame = Frame(self.start_frame, width=45, bg="#D4E6F1")
        self.button_frame.grid(row=3,pady=10)

        # low stakes button
        self.low_stakes = Button(self.button_frame, text="Low ($5)",bg="#9FE2BF",font="times 12 bold",command=lambda: self.to_game(1))
        self.low_stakes.grid(row=0,column=0,padx=5)

        # medium stakes button 
        self.medium_stakes = Button(self.button_frame, text="Medium ($10)",bg="#FFC300",font="times 12 bold",command=lambda: self.to_game(1))
        self.medium_stakes.grid(row=0,column=1,padx=5)
        
        # High_stakes
        self.high_stakes = Button(self.button_frame,text="High ($15)",bg="#FF5733",font="times 12 bold",command=lambda: self.to_game(1))
        self.high_stakes.grid(row=0,column=2,padx=5)

        self.instruction = Button(self.button_frame, text="How to play",bg="#C4B4F3",fg="white",font="times 12 bold", command=self.help)
        self.instruction.grid(row=1, column=1,pady=20)
    def help(self):  
        print("help")
        get_help = Help(self)
        get_help.help_text.configure(text="")

    def to_game(self, stakes):
        start_balance = self.start_entry.get()
        Game(self, stakes, start_balance)

class Help:
    def __init__(self, partner): 

        #background colour
        bkg_colour= "#C4B4F3"

        #Button off
        partner.instruction.config(state=DISABLED)

        #opens a new window
        self.help_box = Toplevel()

        #GUI Frame
        self.help_frame = Frame(self.help_box, width=400, height=300, bg=bkg_colour, padx=10, pady=10)
        
        self.help_frame.grid()

        #Help Heading 0
        self.help_label = Label(self.help_frame, text="How to Play", font=("TImes 13 bold"), bg=bkg_colour, padx=10, pady=10)
       
        self.help_label.grid(row=0)

        #Help Text 1 
        self.help_text = Label(self.help_frame, text="help", justify=LEFT, width=40, bg=bkg_colour , wrap=250)
        self.help_text.grid(row=1)

        #Dismiss button 2 
        self.dismiss_button = Button(self.help_frame, text="Exit", width=10, font="times 12", command=partial(self.close_button, partner))
        self.dismiss_button.grid(row=2,pady=10)
    
    #close help function
    def close_button(self, partner):
        partner.instruction.config(state=NORMAL)
        self.help_box.destroy()


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
        current_balance = self.balance.get
        current_balance += 2

        self.balance.set(current_balance)

        self.balance_label.configure(text="Balance: {}".format(current_balance))

if __name__ == "__main__":
    root = Tk()
    root.title("title goes here")
    something = Start(root)
    root.mainloop()