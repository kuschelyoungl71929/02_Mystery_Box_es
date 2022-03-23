import random
NUM_TRIALS = 1000
winnings= 0

cost = NUM_TRIALS * 5

for item in range(0, NUM_TRIALS): 
    prize = ""
    round_winnings = 0

    for thing in range(0,3):

        prize_num = random.randint(1,100)
        prize += " "
        
        if 0 < prize_num <= 1:
            prize += "Diamond"
            round_winnings += 11
        
        elif 1 < prize_num <= 5:
            prize += "Gold"
            round_winnings += 5

        elif  5 < prize_num <= 15:
            prize += "Silver"
            round_winnings += 3

        elif 15 < prize_num <= 30:
            prize += "Bronze"
            round_winnings += 2

        elif 30 < prize_num <= 90:
            prize += "Stone"
            round_winnings += 1

        elif 90 < prize_num <= 100:
            prize += "Dirt"
          

        



    print("You won {}, which is worth {}".format(prize, round_winnings))
    winnings += round_winnings

print("Money in: ${}".format(cost))
print("Money out: ${}".format(winnings))
    
    
if winnings > cost:
    print("You came out ${} ahead".format(winnings-cost))

else:
    print("You lost ${}".format(cost-winnings))


   
   
   