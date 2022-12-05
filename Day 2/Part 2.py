# Question
#
# --- Part Two ---
# The Elf finishes helping with the tent and sneaks back over to you. "Anyway, the second column says how the round needs to end: 
# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"
#
# The total score is still calculated in the same way, but now you need to figure out what shape to choose so the round ends as indicated. 
# The example above now goes like this:
#
# In the first round, your opponent will choose Rock (A), and you need the round to end in a draw (Y), so you also choose Rock. 
# This gives you a score of 1 + 3 = 4.
# In the second round, your opponent will choose Paper (B), and you choose Rock so you lose (X) with a score of 1 + 0 = 1.
# In the third round, you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = 7.
# Now that you're correctly decrypting the ultra top secret strategy guide, you would get a total score of 12.
#
# Following the Elf's instructions for the second column, what would your total score be if everything goes exactly according to your strategy guide?


# Solution - switching results order for rps function

input = [["B","Y"],
["A","X"],
...,
...

# returns a score based on option chosen and win/lose/draw status
def rps(elfshape, ldw):
    # Elf: Rock
    if(elfshape == "A"):
        if(myshape == "X"): # need to lose
            #print("Elf: Rock, Me: Scissors (Lose)")
            return 3 + 0
        elif(myshape == "Y"): # need to draw
            #print("Elf: Rock, Me: Rock (Draw)")
            return 1 + 3
        elif(myshape == "Z"): # need to win
         #print("Elf: Rock, Me: Paper (Win)")
            return 2 + 6
    # Elf: Paper
    elif(elfshape == "B"):
        if(myshape == "X"):
            #print("Elf: Paper, Me: Rock (Lose)")
            return 1 + 0
        elif(myshape == "Y"):
            #print("Elf: Paper, Me: Paper (Draw)")
            return 2 + 3
        elif(myshape == "Z"):
            #print("Elf: Paper, Me: Scissors (Win)")
            return 3 + 6
    # Elf: Scissors
    elif(elfshape == "C"):
        if(myshape == "X"):
            #print("Elf: Scissors, Me: Paper (Lose)")
            return 2 + 0
        elif(myshape == "Y"):
            #print("Elf: Scissors, Me: Scissors (Draw)")
            return 3 + 3
        elif(myshape == "Z"):
            #print("Elf: Scissors, Me: Rock (Win)")
            return 1 + 6
            
score = 0

elf_options = ["A", "B", "C"]
lose_draw_win = ["X", "Y", "Z"]
for round in input:
    elf = round[0]
    ldw = round[1]
    if(elf in elf_options and ldw in lose_draw_win):
        score += rps(elf, ldw)
    else:
        print("Error: Invalid option chosen for elf shape or ldw status.")
    
print(f"Total Rock, Paper, Scissors score: {score}")
