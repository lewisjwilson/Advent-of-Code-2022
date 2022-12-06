# Question

# --- Part Two ---
# As you watch the crane operator expertly rearrange the crates, you notice the process isn't following your prediction.
# 
# Some mud was covering the writing on the side of the crane, and you quickly wipe it away. The crane isn't a CrateMover 9000 - it's a CrateMover 9001.
# 
# The CrateMover 9001 is notable for many new and exciting features: air conditioning, leather seats, an extra cup holder, 
# and the ability to pick up and move multiple crates at once.
# 
# Again considering the example above, the crates begin in the same configuration:
# 
#     [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 
# Moving a single crate from stack 2 to stack 1 behaves the same as before:
# 
# [D]        
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 
# However, the action of moving three crates from stack 1 to stack 3 means that those three moved crates stay in the same order, resulting in this new configuration:
# 
#         [D]
#         [N]
#     [C] [Z]
#     [M] [P]
#  1   2   3
# Next, as both crates are moved from stack 2 to stack 1, they retain their order as well:
# 
#         [D]
#         [N]
# [C]     [Z]
# [M]     [P]
#  1   2   3
# Finally, a single crate is still moved from stack 1 to stack 2, but now it's crate C that gets moved:
# 
#         [D]
#         [N]
#         [Z]
# [M] [C] [P]
#  1   2   3
# In this example, the CrateMover 9001 has put the crates in a totally different order: MCD.
# 
# Before the rearrangement process finishes, update your simulation so that the Elves know where they should stand to be ready to unload the final supplies. 
# After the rearrangement procedure completes, what crate ends up on top of each stack?


# Solution

# (no. of crates, from stack, to stack)
instructions = [(3, 2, 9),
(1, 1, 6),
...
(1, 7, 4),
(6, 7, 5)]

stacks = {1: ["T", "D", "W", "Z", "V", "P"],
    2: ["L", "S", "W", "V", "F", "J", "D"],
    3: ["Z", "M", "L", "S", "V", "T", "B", "H"],
    4: ["R", "S", "J"],
    5: ["C", "Z", "B", "G", "F", "M", "L", "W"],
    6: ["Q", "W", "V", "H", "Z", "R", "G", "B"],
    7: ["V", "K", "P", "C", "B", "D", "N"],
    8: ["P", "T", "B", "Q"],
    9: ["H", "G", "Z", "R", "C"]
    }
for instruction in instructions:
    crates = instruction[0]
    from_stack = instruction[1]
    to_stack = instruction[2]
    removed = list()
    for c in range(crates):
        removed.append(stacks[from_stack].pop())
    
    removed.reverse()
    
    for c in range(crates):
        stacks[to_stack].append(removed[c])

final_text = ""
for stack in stacks:
    final_text += stacks[stack].pop()
    
print(final_text)
