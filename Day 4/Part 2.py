# Question
#
# --- Part Two ---
# It seems like there is still quite a bit of duplicate work planned. Instead, the Elves would like to know the number of pairs that overlap at all.
#
# In the above example, the first two pairs (2-4,6-8 and 2-3,4-5) don't overlap, while the remaining four pairs (5-7,7-9, 2-8,3-7, 6-6,4-6, and 2-6,4-8) do overlap:
#
# 5-7,7-9 overlaps in a single section, 7.
# 2-8,3-7 overlaps all of the sections 3 through 7.
# 6-6,4-6 overlaps in a single section, 6.
# 2-6,4-8 overlaps in sections 4, 5, and 6.
# So, in this example, the number of overlapping assignment pairs is 4.
#
# In how many assignment pairs do the ranges overlap?

# Solution

section_pairs = [[(16,80),(80,87)],
[(4,9),(10,97)],
...
[(70,90),(19,79)],
[(16,95),(15,96)]]

overlaps = 0
for pair in section_pairs:
    if(pair[1][0] <= pair[0][1] <= pair[1][1]) or \
    (pair[0][0] <= pair[1][1] <= pair[0][1]):
        overlaps += 1
        print(pair)
print(f"There are a total of {overlaps} in the pairs.")
