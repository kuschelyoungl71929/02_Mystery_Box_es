import random
NUM_TRIALS = 3
winnings= 0

cost = NUM_TRIALS * 5

for item in range(0, NUM_TRIALS): 
    prize = ""
    round_winnings = 0

    for thing in range(0,1):

        prize_num = random.randint(1,100)
        prize += " "
        
        if 0 < prize_num <= 1:
            prize += "diamond ($11)"
            round_winnings += 11
        
        elif 1 < prize_num <= 5:
            prize += "gold ($5)"
            round_winnings += 5

        elif  5 < prize_num <= 15:
            prize += "silver ($3)"
            round_winnings += 3

        elif 15 < prize_num <= 30:
            prize += "bronze ($2)"
            round_winnings += 2

        elif 30 < prize_num <= 90:
            prize += "stone ($1)"
            round_winnings += 1

        elif 90 < prize_num <= 100:
            prize += "dirt ($0)"
          

        



    print("|{}".format(prize))
    winnings += round_winnings

print("|Cost: ${}".format(cost))
print("|Payback ${}".format(winnings))
print("|Current Balance: ${}'".format(cost+winnings))



