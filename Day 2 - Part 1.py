# Question 
#
# --- Day 2: Rock Paper Scissors ---
# The Elves begin to set up camp on the beach. To decide whose tent gets to be closest to the snack storage, 
# a giant Rock Paper Scissors tournament is already in progress.
#
# Rock Paper Scissors is a game between two players. Each game contains many rounds; in each round, the players each simultaneously 
# choose one of Rock, Paper, or Scissors using a hand shape. Then, a winner for that round is selected: Rock defeats Scissors,
# Scissors defeats Paper, and Paper defeats Rock. If both players choose the same shape, the round instead ends in a draw.
#
# Appreciative of your help yesterday, one Elf gives you an encrypted strategy guide (your puzzle input) that they say will be sure to help you win. 
# "The first column is what your opponent is going to play: A for Rock, B for Paper, and C for Scissors. 
# The second column--" Suddenly, the Elf is called away to help with someone's tent.
#
# The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, and Z for Scissors. 
# Winning every time would be suspicious, so the responses must have been carefully chosen.
#
# The winner of the whole tournament is the player with the highest score. Your total score is the sum of your scores for each round. 
# The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) 
# plus the score for #the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).
#
# Since you can't be sure if the Elf is trying to help you or trick you, you should calculate the score you would get if you were to follow the strategy guide.
#
# For example, suppose you were given the following strategy guide:
#
# A Y
# B X
# C Z
#
#This strategy guide predicts and recommends the following:
#
# In the first round, your opponent will choose Rock (A), and you should choose Paper (Y). 
# This ends in a win for you with a score of 8 (2 because you chose Paper + 6 because you won).
# In the second round, your opponent will choose Paper (B), and you should choose Rock (X).
# This ends in a loss for you with a score of 1 (1 + 0).
# The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.
# In this example, if you were to follow the strategy guide, you would get a total score of 15 (8 + 1 + 6).
#
# What would your total score be if everything goes exactly according to your strategy guide?



# Solution

input = [["B","Y"],
["A","X"],
...,
...,
["A","X"],
["B","Y"]]

# returns a score based on option chosen and win/lose/draw status
def rps(elfshape, myshape):
    # Elf: Rock
    if(elfshape == "A"):
        if(myshape == "X"):
            #print("Elf: Rock, Me: Rock (Draw)")
            return 1 + 3
        elif(myshape == "Y"):
            #print("Elf: Rock, Me: Paper (Win)")
            return 2 + 6
        elif(myshape == "Z"):
            #print("Elf: Rock, Me: Scissors (Lose)")
            return 3 + 0
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
            #print("Elf: Scissors, Me: Rock (Win)")
            return 1 + 6
        elif(myshape == "Y"):
            #print("Elf: Scissors, Me: Paper (Lose)")
            return 2 + 0
        elif(myshape == "Z"):
            #print("Elf: Scissors, Me: Scissors (Draw)")
            return 3 + 3
            
score = 0

elf_options = ["A", "B", "C"]
me_options = ["X", "Y", "Z"]
for round in input:
    elf = round[0]
    me = round[1]
    if(elf in elf_options and me in me_options):
        score += rps(elf, me)
    else:
        print("Error: Invalid option chosen for elf/me shape.")
    
print(f"Total Rock, Paper, Scissors score: {score}")
