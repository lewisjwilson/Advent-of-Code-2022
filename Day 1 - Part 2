# Question
# By the time you calculate the answer to the Elves' question, they've already realized that the Elf carrying the most Calories of food might 
# eventually run out of snacks.
# To avoid this unacceptable situation, the Elves would instead like to know the total Calories carried by the top three Elves carrying the most Calories. 
# That way, even if one of those Elves runs out of snacks, they still have two backups.

# In the example above, the top three Elves are the fourth Elf (with 24000 Calories), then the third Elf (with 11000 Calories), 
# then the fifth Elf (with 10000 Calories). The sum of the Calories carried by these three elves is 45000.

# Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?



# Solution

# Preformatted using online regex find and replace
calories = [2494,
8013,
...,
...
1311,
1121]

elves = []

cals = 0
for c in calories:
    if(c==0):
        elves.append(cals)
        cals = 0
    else:
        cals += c
        
elves_order = elves.copy()
elves.sort(reverse=True)
      
print(f"Elf {elves_order.index(elves[0]) + 1} is carrying {elves[0]} calories!")
print(f"Elf {elves_order.index(elves[1]) + 1} is carrying {elves[1]} calories!")
print(f"Elf {elves_order.index(elves[2]) + 1} is carrying {elves[2]} calories!")
print(f"The sum of calories of these elves is {elves[0]+elves[1]+elves[2]} calories!")
