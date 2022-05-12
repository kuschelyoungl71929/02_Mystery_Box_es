
from tkinter import *
from functools import partial
import random
import re


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
        self.all_game_stats = []
        # set the funds variable 
        self.balance = IntVar()
        self.balance.set(start_balance)
        
        
        self.game_stats = [start_balance , start_balance]

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
        self.prize_label1 = Label(self.display_frame,pady=20, padx=10,image=photo)
        self.prize_label1.photo = photo
        self.prize_label1.grid(row=0, column=0, padx=10)

        self.prize_label2 = Label(self.display_frame,pady=20, padx=10,image=photo)
        self.prize_label2.photo = photo       
        self.prize_label2.grid(row=0,column=1, padx=10)

        self.prize_label3 = Label(self.display_frame,pady=20, padx=10,image=photo)
        self.prize_label3.photo = photo
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
        self.stats = Button(self.button_frame, text="Game Stats...",font="times 12 bold", command=lambda: self.to_stats(self.game_stats, self.all_game_stats))
        self.stats.grid(row=1, column=2,pady=20)
        self.stats.configure(state=DISABLED)
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
        #sets the stats button to normal
        self.stats.configure(state=NORMAL)
        
        #retrieves the play balance
        play_balance = self.balance.get()
        #retrieves the stakes  multiplier
        stakes_multiplier = self.multiplier.get()
        #sets up the prize list
        prizes = []

        values = []
        #sets up the round winnings integer
        round_winnings= 0
        #defines the image lists
        copper = ["02_Mystery_Box\Images_mb\copper_low.gif", "02_Mystery_Box\Images_mb\copper_med.gif", "02_Mystery_Box\Images_mb\copper_high.gif"]
        silver = ["02_Mystery_Box\Images_mb\silver_low.gif","02_Mystery_Box\Images_mb\silver_med.gif", "02_Mystery_Box\Images_mb\silver_high.gif"]
        gold = ["02_Mystery_Box\Images_mb\gold_low.gif", "02_Mystery_Box\Images_mb\gold_med.gif", "02_Mystery_Box\Images_mb\gold_high.gif"]
        #game code, rng
        for item in range(0,3):

            prize_num = random.randint(1,100)
            
            if 0 < prize_num <= 15:
                prize = PhotoImage(file=gold[stakes_multiplier-1])
                value = "gold ${}".format( 5 * stakes_multiplier)
                round_winnings += 5 * stakes_multiplier
    
            elif  15 < prize_num <= 37:
                prize = PhotoImage(file=silver[stakes_multiplier-1])
                value = "silver ${}".format( 2 * stakes_multiplier)
                round_winnings += 2 * stakes_multiplier
    
            elif 37 < prize_num <= 75:
                prize = PhotoImage(file=copper[stakes_multiplier-1])
                value = "copper ${}".format( 1 * stakes_multiplier)
                round_winnings += 1 * stakes_multiplier
    
            elif 75 < prize_num <= 100:
                prize = PhotoImage(file="02_Mystery_Box\Images_mb\lead.gif")
                value = "lead $0"
                round_winnings += 0 * stakes_multiplier

            prizes.append(prize)
            values.append(value)
        #sets the images as prizes
        photo1= prizes[0]
        photo2= prizes[1]
        photo3= prizes[2]
        
        #display images
        self.prize_label1.configure(image=photo1)
        self.prize_label1.photo = photo1
        self.prize_label2.configure(image=photo2)   
        self.prize_label2.photo = photo2
        self.prize_label3.configure(image=photo3) 
        self.prize_label3.photo = photo3
        #minuses the cost of the game from the players balance
        play_balance -= 5 * stakes_multiplier
        #adds the money won from the game to the play balance
        play_balance += round_winnings
        #sets the balance as the play balance
        self.balance.set(play_balance)
        #sets the balance to a float to be used in the checker
        balance_check = float(play_balance)
        
        #disables the button to keep playing if the player has no money left
        if balance_check < 5 * stakes_multiplier:
            self.open_boxes.configure(state=DISABLED)
            self.game_box.focus()
            self.open_boxes.config(text="Add more Money to Play Again")
        #final balance statement
        final_balance = "Money Spent this Round: ${}\nPrize Money this Round: ${}\nMoney out: ${}".format(5 * stakes_multiplier,round_winnings,play_balance)

        self.amount_start.configure(text=final_balance)
 
        self.game_stats[1] = play_balance
        self.all_game_stats.append("'{} | {} | {} - Cost: ${} | Money Won This Round: ${} | Current Balance: ${}'".format(values[0],values[1],values[2],5 * stakes_multiplier,round_winnings,play_balance))
        #print statement
        print("'{} | {} | {} - Cost: ${} | Money Won This Round: ${} | Current Balance: ${}'".format(values[0],values[1],values[2],5 * stakes_multiplier,round_winnings,play_balance))

    def close_button(self, partner):
        self.game_box.destroy()
        root.deiconify()

    def to_stats(self, game_stats,all_game_stats):

        Stats(self, game_stats,all_game_stats)


class Stats: 
    def __init__(self, partner, game_stats, all_game_stats): 

        print(game_stats[1])
        #background colour
        bkg_colour= "#9fe5d9"
        amount = game_stats[1]-game_stats[0] 
        game_history = len(all_game_stats)
        #Button off
        partner.stats.config(state=DISABLED)


        #opens a new window
        self.stats_box = Toplevel()
        self.stats_box.protocol('WM_DELETE_WINDOW', partial(self.close_button, partner))

        #GUI Frame
        self.stats_frame = Frame(self.stats_box, width=400, height=300, bg=bkg_colour, padx=10, pady=10)
        
        self.stats_frame.grid()

        #Help Heading 0
        self.stats_label = Label(self.stats_frame, text="Stats/Export", font=("Arial 16 bold"), bg=bkg_colour, padx=10, pady=10)
       
        self.stats_label.grid(row=0)

        #sets amount variable as an integer so it can be checked
        amount = int(amount)
    
        self.stats_display = Label(self.stats_frame, text="Starting Balance: ${} \nCurrent Balance: ${} \nAmount Won: ${} \nRounds Played: {}".format(game_stats[0], game_stats[1], amount, game_history), font=("Arial 12 "), bg=bkg_colour, padx=10, pady=10)
        #decides whether to display that the player gained or lost
        if amount < 0: 
            self.stats_display.configure(text="Starting Balance: ${} \nCurrent Balance: ${} \nAmount Lost: ${} \nRounds Played: {}".format(game_stats[0], game_stats[1], amount/-1, game_history))
        self.stats_display.grid(row=1)

        self.button_frame = Frame(self.stats_frame,  bg=bkg_colour)
        
        self.button_frame.grid(column=0)
        #Dismiss button 2 
        self.dismiss_button = Button(self.button_frame, text="Exit", width=10, command=partial(self.close_button, partner))
        self.dismiss_button.grid(row=2,column= 0,pady=10)

      
        
        #retrieve full history button
        self.full_history = Button(self.button_frame, text="Export", width=10, command=lambda: self.export_button(partner, all_game_stats, game_stats))
        self.full_history.grid(row=2, column=1, pady=10)

    #export function
    def export_button(self, partner, all_game_stats, game_stats):
        self.full_history.config(state=DISABLED)
        Export(self, all_game_stats, game_stats)
        

    #close function
    def close_button(self, partner):
        partner.stats.config(state=NORMAL)
        self.stats_box.destroy()

class Export:
    def __init__(self, partner, all_game_stats, game_stats):

        #light cyan
        bkg_colour = "#9fe5d9"
    

        #export box
        self.export_box = Toplevel()
        self.export_box.protocol('WM_DELETE_WINDOW', partial(self.close_button, partner))
        
        # frame
        self.export_frame = Frame(self.export_box, width=400, height=300, bg=bkg_colour, padx=10, pady=10)
        self.export_frame.grid()
        
        # Heading
        self.export_label = Label(self.export_frame, text="Export", font=("Arial 16 bold"), bg=bkg_colour, padx=5, pady=10)
        self.export_label.grid(row=1)
        
        # User information/Instructions
        self.instructions = Label(self.export_frame, text="Enter a filename, no spaces or special characters", wrap=250, justify=LEFT, bg=bkg_colour, font="arial 11", padx=10, pady=10)
        self.instructions.grid(row=2)

        self.instructions = Label(self.export_frame, text="Warning: If the filename you choose already exists, your game history will overwrite that file", wrap=250, justify=LEFT, bg="#F3B6B6", font="arial 11 italic", padx=10, pady=10)
        self.instructions.grid(row=3, pady=5)
        #  input box
        self.filename_box = Entry(self.export_frame, width=15, font="Arial 12 bold")
        self.filename_box.grid(row=4)

        self.error_filename = Label(self.export_frame, text="", wrap=250, justify=LEFT, bg=bkg_colour, font="arial 11", padx=10, pady=10)
        self.error_filename.grid(row=5)
       
        #button frame
        self.save_exit_button_frame = Frame(self.export_frame, bg=bkg_colour)
        self.save_exit_button_frame.grid(row=6, pady=10)

        #exit
        self.dismiss_button_export = Button(self.save_exit_button_frame, text="Exit", width=7, command=partial(self.close_button, partner))
        self.dismiss_button_export.grid(row=0, column=1, padx=5)

        #save Button
        self.save_button = Button(self.save_exit_button_frame, width=7, text="Save", command=partial(lambda: self.save_as_file(partner, all_game_stats, game_stats)))
        self.save_button.grid(row=0, column=0, padx=5)

    def save_as_file(self, partner, all_game_stats, game_stats):

        valid_char = "[A-za-z0-9_]"
        has_error= "no"

        filename=  self.filename_box.get()
      
        
        for letter in filename:
            if re.match(valid_char, letter):
                continue
        
            elif letter == " ":
                problem = ("No spaces allowed.")
       
            else:
                problem = ("No {}'s allowed.".format(letter))

            has_error = "yes"
            break

        if filename == "":
            problem= "Please enter a filename."
            has_error = "yes"

        if has_error == "yes":
            self.error_filename.config(text="Invalid filename - {}".format(problem))
        else:
            filename = filename + ".txt"
            f = open(filename, "w+")
            f.write("Game Statistics\n\n")
            
            f.write("Starting Balance:")
           
            f.write("{}\n".format(game_stats[0]))
            f.write("Current Balance:")
   
            f.write("{}\n".format(game_stats[1]))

            f.write("\nRound Details\n\n")
            
            for item in all_game_stats:
                f.write("{}\n".format(item))

        f.close

        self.close_button(partner)

    def close_button(self, partner):
        
        partner.full_history.config(state=NORMAL)

        self.export_box.destroy()

    
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