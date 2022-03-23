
from tkinter import *
from functools import partial
import random

class Start:
    def __init__(self, parent):

       #start GUI frame
        self.start_frame = Frame(padx=10,bg="#D4E6F1")
        self.start_frame.grid()

        #define variable as integer
        self.starting_funds = IntVar()

        #title
        self.mystery_box_label = Label(self.start_frame, text="Mystery Box Game",font="times 18 bold",pady=20, padx=10,bg="#D4E6F1")
        self.mystery_box_label.grid(row=1)

        #frame for error label
        self.funds_frame = Frame(self.start_frame, width=45, bg="#D4E6F1")
        self.funds_frame.grid(row=3,column=0)

        # entry box
        self.start_entry = Entry(self.start_frame, font="times 16 bold")
        self.start_entry.grid(row=2, column=0,pady=10)

        #error label
        self.amount_error = Label(self.funds_frame , text="",bg="#D4E6F1", fg="#9B0019",font="times 12 bold", justify=LEFT, wrap =200)
        self.amount_error.grid(row=5,pady=5)

        #button frame
        self.button_frame = Frame(self.start_frame, width=45, bg="#D4E6F1")
        self.button_frame.grid(row=6,pady=10)

        # low stakes button
        self.low_stakes = Button(self.button_frame, text="Low ($5)",bg="#9FE2BF",font="times 12 bold",command=lambda: self.to_game(1))
        self.low_stakes.grid(row=0,column=0)

        # medium stakes button 
        self.medium_stakes = Button(self.button_frame, text="Medium ($10)",bg="#FFC300",font="times 12 bold",command=lambda: self.to_game(2))
        self.medium_stakes.grid(row=0,column=1,padx=5)
        
        # High_stakes
        self.high_stakes = Button(self.button_frame,text="High ($15)",bg="#FF5733",font="times 12 bold",command=lambda: self.to_game(3))
        self.high_stakes.grid(row=0,column=2,padx=5)


        #add funds button
        self.add_funds = Button(self.start_frame , width=10, text="Add Funds",font="times 12 bold", command=lambda: self.check_funds())
        self.add_funds.grid(row=4,column=0,pady=10)

    def check_funds(self):
        
        #define start balance
        start_balance = self.start_entry.get()
        
        #no errors config
        error_bkg = "#ffafaf"
        has_errors = "no"
        self.start_entry.config(bg="white")
        self.amount_error.config(text="")

        #disable all buttons
        self.low_stakes.config(state=DISABLED)
        self.medium_stakes.config(state=DISABLED)
        self.high_stakes.config(state=DISABLED)


        #Error checker
        try:
            start_balance = int(start_balance)
            
            #minimum
            if start_balance < 5:
                has_errors="yes"
                error_text = "Sorry, the least you can play with is $5"

            #maximum
            elif start_balance >50:
                has_errors="yes" 
                error_text = "Too much! The most you can risk in this game is $50, seek recovery for your gambling addiction"
            
            #enough for high stakes
            elif start_balance >=15:
               self.low_stakes.config(state=NORMAL)
               self.medium_stakes.config(state=NORMAL)
               self.high_stakes.config(state=NORMAL)
               
            #enough for medium stakes
            elif start_balance >=10:
                self.low_stakes.config(state=NORMAL)
                self.medium_stakes.config(state=NORMAL)

            #enough for low stakes
            elif start_balance >=5:
                self.low_stakes.config(state=NORMAL)
        
        #not a number
        except ValueError:
            has_errors = "yes"
            error_text = "Please enter a whole number value amount" 
        
        #error config
        if has_errors == "yes":
            self.start_entry.config(bg=error_bkg)
            self.amount_error.config(text=error_text)

        #set the starting funds for the game to the number entered
        else:

            self.starting_funds.set(start_balance)
            
    #command for the stakes buttons, starts the game
    def to_game(self):
        
        #starting balance for the game
        start_balance = self.starting_funds.get()

        #stakes for the game
        stakes= 1

        Game(self,stakes,start_balance)

        #closes the first box
        root.withdraw()

       
class Game:
    def __init__(self, partner, stakes, start_balance):
        print(start_balance)
        partner.low_stakes.config(state=DISABLED)
        partner.medium_stakes.config(state=DISABLED)
        partner.high_stakes.config(state=DISABLED)

        self.game_box = Toplevel()

        self.multiplier = IntVar()
        self.multiplier.set(stakes)

        self.start_frame = Frame(self.game_box,padx=10,bg="#D4E6F1")
        self.start_frame.grid()

       
        self.starting_funds = IntVar()
        self.starting_funds.set(start_balance)

        self.display_frame = Frame(self.start_frame, width=45, bg="#D4E6F1")
        self.display_frame.grid(row=3)
        
        self.prize_label1 = Label(self.display_frame, text="?",font="times 18 bold",pady=20, padx=10,bg="plum3", width=5)
        self.prize_label1.grid(row=0, column=0, padx=10)

        self.prize_label2 = Label(self.display_frame, text="?",font="times 18 bold",pady=20, padx=10,bg="plum3", width=5)
        self.prize_label2.grid(row=0,column=1, padx=10)

        self.prize_label3 = Label(self.display_frame, text="?",font="times 18 bold",pady=20, padx=10,bg="plum3",width=5)
        self.prize_label3.grid(row=0,column=2, padx=10)

        self.mystery_box_label = Label(self.start_frame, text="Play...",font="times 18 bold",pady=20, padx=10,bg="#D4E6F1")
        self.mystery_box_label.grid(row=1)

        self.instruction_start = Label(self.start_frame , text="Press Enter or click the 'Open Boxes' button to reveal the contents of the mystery boxes",bg="#D4E6F1",font="times 11", justify=LEFT, wrap=250)
        self.instruction_start.grid(row=2,pady=5)

        self.funds_frame = Frame(self.start_frame, width=45, bg="#D4E6F1")
        self.funds_frame.grid(row=5)

        self.amount_start = Label(self.funds_frame , text="Starting Balance: {}".format(self.starting_funds.get()),bg="#D4E6F1",font="times 12 bold", justify=LEFT)
        self.amount_start.grid(row=0,pady=5)

        self.button_frame = Frame(self.start_frame, width=45, bg="#D4E6F1")
        self.button_frame.grid(row=6,pady=10)

        self.instruction = Button(self.button_frame, text="How to play",font="times 12 bold")
        self.instruction.grid(row=1, column=1,pady=20)

        self.stats = Button(self.button_frame, text="Game Stats...",font="times 12 bold")
        self.stats.grid(row=1, column=2,pady=20)

        self.add_funds = Button(self.start_frame , width=15, text="Open Boxes",font="times 16 bold", command= lambda: self.show_boxes(self.start_balance))
        self.add_funds.grid(row=4,column=0,pady=10)


    def show_boxes(self):
        
        play_balance = self.start_balance.get()
        stakes_multiplier = self.multiplier.get()
        
        round_winnings= 0
        prizes = []

        for item in range(0,3):

            prize_num = random.randint(1,100)
            prize += " "
            
            if 0 < prize_num <= 1:
                prize += "Diamond\n(${})".format(6 * stakes_multiplier)
                round_winnings += 6 * stakes_multiplier
            
            elif 1 < prize_num <= 5:
                prize += "Gold\n(${})".format(5 * stakes_multiplier)
                round_winnings += 5 * stakes_multiplier

            elif  5 < prize_num <= 15:
                prize += "Silver\n(${})".format(3 * stakes_multiplier)
                round_winnings += 3 * stakes_multiplier

            elif 15 < prize_num <= 30:
                prize += "Bronze\n(${})".format(2 * stakes_multiplier)
                round_winnings += 2 * stakes_multiplier

            elif 30 < prize_num <= 90:
                prize += "Stone\n(${})".format(1 * stakes_multiplier)
                round_winnings += 1 * stakes_multiplier

            elif 90 < prize_num <= 100:
                prize += "Dirt\n($0)" 

            prizes.append(prize)


            self.prize_label1.configure(text=prizes[0])   
            self.prize_label2.configure(text=prizes[1])   
            self.prize_label3.configure(text=prizes[2])   

            play_balance -= 5 * stakes_multiplier
            
            play_balance += round_winnings

            self.start_balance.set(play_balance)

            final_balance = "Money in: ${}\nMoney out: ${}".format(5 * stakes_multiplier,start_balance)"

if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Box Game")
    something = Start(root)
    root.mainloop()