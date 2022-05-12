
from tkinter import *
from functools import partial
import random



class Start:
    def __init__(self, partner):

       #start GUI frame
        self.start_frame = Frame(padx=10,bg="#D4E6F1")
        self.start_frame.grid()
        
        root.protocol('WM_DELETE_WINDOW', partial(self.close_button, partner))

        #define variable as integer
        self.starting_funds = IntVar()
        self.starting_funds.set(0)

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

        self.low_stakes.config(state=DISABLED)
        self.medium_stakes.config(state=DISABLED)
        self.high_stakes.config(state=DISABLED)


        #add funds button
        self.add_funds = Button(self.start_frame , width=10, text="Add Funds",font="times 12 bold", command=lambda: self.check_funds())
        self.add_funds.focus()
        self.add_funds.bind('<Return>', lambda e:self.check_funds())
        self.add_funds.grid(row=4,column=0,pady=10)

    

    def close_button(self, partner):
        root.destroy()

    
    def check_funds(self):
        
        #define start balance
        start_balance = self.start_entry.get()
        
        #no errors config
        error_bkg = "#ffafaf"
        has_errors = "no"
        self.start_entry.config(bg="white")
        self.amount_error.config(text="")




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
    def to_game(self, stakes):
        
        #starting balance for the game
        start_balance = self.starting_funds.get()
        Game(self,stakes,start_balance)
        root.withdraw()


class Game:
    def __init__(self, partner, stakes, start_balance):
    
        photo=PhotoImage(file="02_Mystery_Box\Images_mb\question.gif")

        # set the funds variable 
        self.balance = IntVar()
        self.balance.set(start_balance)
        
        # disable stakes buttons
        partner.low_stakes.config(state=DISABLED)
        partner.medium_stakes.config(state=DISABLED)
        partner.high_stakes.config(state=DISABLED)

        # open a new window
        self.game_box = Toplevel()

        self.game_box.protocol('WM_DELETE_WINDOW', partial(self.close_button, partner))


        # set the multiplier
        self.multiplier = IntVar()
        self.multiplier.set(stakes)

        # frame
        self.start_frame = Frame(self.game_box,padx=10,bg="#D4E6F1")
        self.start_frame.grid()

        # frame for prizes 1-3
        self.display_frame = Frame(self.start_frame, width=45, bg="#D4E6F1")
        self.display_frame.grid(row=3)
        
        # prize labels 
        self.prize_label1 = Label(self.display_frame,pady=20, padx=10,text="?", width = 10)

        self.prize_label1.grid(row=0, column=0, padx=10)

        self.prize_label2 = Label(self.display_frame,pady=20, padx=10, text="?",  width = 10)
    
        self.prize_label2.grid(row=0,column=1, padx=10)

        self.prize_label3 = Label(self.display_frame,pady=20, padx=10,text="?", width = 10)
       
        self.prize_label3.grid(row=0,column=2, padx=10)

        # title
        self.mystery_box_label = Label(self.start_frame, text="Play...",font="times 18 bold",pady=20, padx=10,bg="#D4E6F1")
        self.mystery_box_label.grid(row=1)

        # instructions
        self.instruction_start = Label(self.start_frame , text="Press Enter or click the 'Open Boxes' button to reveal the contents of the mystery boxes",bg="#D4E6F1",font="times 11", justify=LEFT, wrap=250)
        self.instruction_start.grid(row=2,pady=5) 

        # useless frame 
        self.funds_frame = Frame(self.start_frame, width=45, bg="#D4E6F1")
        self.funds_frame.grid(row=5)

        # starting balance label
        self.amount_start = Label(self.funds_frame , text="Starting Balance: {}".format(self.balance.get()),bg="#D4E6F1",font="times 12 bold", justify=LEFT)
        self.amount_start.grid(row=0,pady=5)

        self.amount_final = Label(self.funds_frame, text="",bg="#D4E6F1",font="times 12 bold", justify=LEFT)
        self.amount_final.grid(row=1,pady=5)

        # button frame
        self.button_frame = Frame(self.start_frame, width=45, bg="#D4E6F1")
        self.button_frame.grid(row=6,pady=10)

        # instructon button
        self.instruction = Button(self.button_frame, text="How to play",font="times 12 bold", command= self.help)
        self.instruction.grid(row=1, column=1,pady=20)

        # stats button
        self.stats = Button(self.button_frame, text="Game Stats...",font="times 12 bold")
        self.stats.grid(row=1, column=2,pady=20)

        # action
        self.open_boxes = Button(self.start_frame, text="Open Boxes",font="times 16 bold", command=self.show_boxes)
        self.open_boxes.focus()
        self.open_boxes.bind('<Return>', lambda e:self.show_boxes())
        self.open_boxes.grid(row=4,column=0,pady=10)
       

    def help(self):

        print("help")
        get_help = Help(self)
        get_help.help_text.configure(text="help", bg="white")

    def show_boxes(self):
        
        play_balance = self.balance.get()
        stakes_multiplier = self.multiplier.get()
        prizes = []
        round_winnings= 0

        for item in range(0,3):

            prize_num = random.randint(1,100)
            
            if 0 < prize_num <= 15:
                prize = "gold ${}".format( 5 * stakes_multiplier)
                round_winnings += 5 * stakes_multiplier
    
            elif  15 < prize_num <= 37:
                prize = "silver ${}".format( 2 * stakes_multiplier)
                round_winnings += 2 * stakes_multiplier
    
            elif 37 < prize_num <= 75:
                prize = "copper ${}".format( 1 * stakes_multiplier)
                round_winnings += 1 * stakes_multiplier
    
            elif 75 < prize_num <= 100:
                prize = "lead $0"
                round_winnings += 0 * stakes_multiplier

            prizes.append(prize)

        self.prize_label1.configure(text = prize)
     
        self.prize_label2.configure(text = prize)
  
        self.prize_label3.configure(text = prize) 


        play_balance -= 5 * stakes_multiplier
        
        play_balance += round_winnings

        self.balance.set(play_balance)

        balance_check = float(play_balance)
        
        if balance_check < 5 * stakes_multiplier:
            self.open_boxes.configure(state=DISABLED)
            self.game_box.focus()
            self.open_boxes.config(text="Add more Money to Play Again")

        final_balance = "Money Spent this Round: ${}\nPrize Money this Round: ${}\nMoney out: ${}".format(5 * stakes_multiplier,round_winnings,play_balance)

        self.amount_start.configure(text=final_balance)

        print("'{} | {} | {} - Cost: ${} | Payback: ${} | Current Balance: ${}'".format(prizes[0],prizes[1],prizes[2],5 * stakes_multiplier,round_winnings,play_balance))

    def close_button(self, partner):
        self.game_box.destroy()
        root.deiconify()




class Help: 

    def __init__(self, partner): 


        #background colour
        bkg_colour= "#c6e2ff" #light blue

        #Button off
        partner.instruction.config(state=DISABLED)

        #opens a new window
        self.help_box = Toplevel()
        
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_button, partner))

        #GUI Frame
        self.help_frame = Frame(self.help_box, width=400, height=300, bg=bkg_colour, padx=10, pady=10)
        
        self.help_frame.grid()

        #Help Heading 0
        self.help_converter_label = Label(self.help_frame, text="How to Use", font=("Arial 13 bold"), bg=bkg_colour, padx=10, pady=10)
       
        self.help_converter_label.grid(row=0)

        #Help Text 1 
        self.help_text = Label(self.help_frame, text="help", justify=LEFT, width=40, bg=bkg_colour , wrap=250)
        self.help_text.grid(row=1)

        #Dismiss button 2 
        self.dismiss_button = Button(self.help_frame, text="Exit", width=10, command=partial(self.close_button, partner))
        self.dismiss_button.grid(row=2,pady=10)
    
    #close help function
    def close_button(self, partner):
        self.help_box.destroy()


if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Box Game")
    something = Start(root)
    root.mainloop()