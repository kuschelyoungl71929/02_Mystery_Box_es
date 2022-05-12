
from tkinter import *
from functools import partial
import random



class Game:
    def __init__(self, partner):


        self.game_history = 1
        self.game_stats = [45,16]
        self.round_stats = ['copper $3 | copper $3 | copper $3 - Cost: $15 | Payback: $9 | Current Balance: $39', 'gold $15 | copper $3 | gold $15 - Cost: $15 | Payback: $33 | Current Balance: $57', 'lead $0 | silver $6 | lead $0 - Cost: $15 | Payback: $6 | Current Balance: $48', 'lead $0 | copper $3 | copper $3 - Cost: $15 | Payback: $6 | Current Balance: $39', 'copper $3 | copper $3 | gold $15 - Cost: $15 | Payback: $21 | Current Balance: $45', 'copper $3 | lead $0 | lead $0 - Cost: $15 | Payback: $3 | Current Balance: $33', 'copper $3 | copper $3 | copper $3 - Cost: $15 | Payback: $9 | Current Balance: $39', 'gold $15 | copper $3 | gold $15 - Cost: $15 | Payback: $33 | Current Balance: $57', 'lead $0 | silver $6 | lead $0 - Cost: $15 | Payback: $6 | Current Balance: $48', 'lead $0 | copper $3 | copper $3 - Cost: $15 | Payback: $6 | Current Balance: $39', 'copper $3 | copper $3 | gold $15 - Cost: $15 | Payback: $21 | Current Balance: $45', 'copper $3 | lead $0 | lead $0 - Cost: $15 | Payback: $3 | Current Balance: $33', 'copper $3 | copper $3 | copper $3 - Cost: $15 | Payback: $9 | Current Balance: $39', 'gold $15 | copper $3 | gold $15 - Cost: $15 | Payback: $33 | Current Balance: $57', 'lead $0 | silver $6 | lead $0 - Cost: $15 | Payback: $6 | Current Balance: $48', 'lead $0 | copper $3 | copper $3 - Cost: $15 | Payback: $6 | Current Balance: $39', 'copper $3 | copper $3 | gold $15 - Cost: $15 | Payback: $21 | Current Balance: $45', 'copper $3 | lead $0 | lead $0 - Cost: $15 | Payback: $3 | Current Balance: $33']

        # frame
        self.game_frame = Frame(padx=10,bg="#D4E6F1")
        self.game_frame.grid()

        self.stats_button = Button(self.game_frame, text="Game Stats...",font="times 12 bold", command=lambda: self.to_stats(self.game_history, self.game_stats))
        self.stats_button.grid(row=1)

    def to_stats(self, game_history, game_stats):

        Stats(self, game_history, game_stats)

class Stats: 
    def __init__(self, partner, game_history, game_stats): 

        print(game_history)
        #background colour
        bkg_colour= "#9fe5d9"

        amount = ()
        #Button off
        partner.stats_button.config(state=DISABLED)

        #opens a new window
        self.stats_box = Toplevel()

        #GUI Frame
        self.stats_frame = Frame(self.stats_box, width=400, height=300, bg=bkg_colour, padx=10, pady=10)
        
        self.stats_frame.grid()

        #Help Heading 0
        self.stats_label = Label(self.stats_frame, text="Stats/Export", font=("Arial 16 bold"), bg=bkg_colour, padx=10, pady=10)
       
        self.stats_label.grid(row=0)

        self.stats_display = Label(self.stats_frame, text="Starting Balance: ${} \nCurrent Balance: ${} \nAmount Lost: ${} \nRounds Played: {}".format(game_stats[0], game_stats[1], amount, game_history), font=("Arial 12 bold"), bg=bkg_colour, padx=10, pady=10)
       
        self.stats_display.grid(row=1)

        self.button_frame = Frame(self.stats_frame,  bg=bkg_colour)
        
        self.button_frame.grid(column=0)
        #Dismiss button 2 
        self.dismiss_button = Button(self.button_frame, text="Exit", width=10, command=partial(self.close_button, partner))
        self.dismiss_button.grid(row=2,column= 0,pady=10)

        #retrieve full history button
        self.full_history = Button(self.button_frame, text="Export", width=10)
        self.full_history.grid(row=2, column=1, pady=10)
    
    #close help function
    def close_button(self, partner):
        partner.stats_button.config(state=NORMAL)
        self.stats_box.destroy()




if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Box Game")
    something = Game(root)
    root.mainloop()