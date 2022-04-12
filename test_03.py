
from tkinter import *
from functools import partial #for removing window
import random

class Start:
    
    def __init__(self):
        
        self.converter_frame = Frame(width=400, height=300, padx=10, pady=10)
        self.converter_frame.grid()

        self.spin = Spinbox(self.converter_frame, width=40, padx=10, pady=10)
        self.spin.grid(row=0)




if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Box Game")
    something = Start(root)
    root.mainloop()