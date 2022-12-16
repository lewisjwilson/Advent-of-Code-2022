# Question

# --- Day 8: Treetop Tree House ---
# The expedition comes across a peculiar patch of tall trees all planted carefully in a grid. 
# The Elves explain that a previous expedition planted these trees as a reforestation effort. 
# Now, they're curious if this would be a good location for a tree house.
# 
# First, determine whether there is enough tree cover here to keep a tree house hidden. 
# To do this, you need to count the number of trees that are visible from outside the grid when looking directly along a row or column.
# 
# The Elves have already launched a quadcopter to generate a map with the height of each tree (your puzzle input). For example:
# 
# 30373
# 25512
# 65332
# 33549
# 35390
# Each tree is represented as a single digit whose value is its height, where 0 is the shortest and 9 is the tallest.
# 
# A tree is visible if all of the other trees between it and an edge of the grid are shorter than it. 
# Only consider trees in the same row or column; that is, only look up, down, left, or right from any given tree.
# 
# All of the trees around the edge of the grid are visible - since they are already on the edge, there are no trees to block the view. 
# In this example, that only leaves the interior nine trees to consider:
# 
# The top-left 5 is visible from the left and top. (It isn't visible from the right or bottom since other trees of height 5 are in the way.)
# The top-middle 5 is visible from the top and right.
# The top-right 1 is not visible from any direction; for it to be visible, there would need to only be trees of height 0 between it and an edge.
# The left-middle 5 is visible, but only from the right.
# The center 3 is not visible from any direction; for it to be visible, there would need to be only trees of at most height 2 between it and an edge.
# The right-middle 3 is visible from the right.
# In the bottom row, the middle 5 is visible, but the 3 and 4 are not.
# With 16 trees visible on the edge and another 5 visible in the interior, a total of 21 trees are visible in this arrangement.
# 
# Consider your map; how many trees are visible from outside the grid?


# Solution

input = ["102200120221123133322123221134224301040024344534431245323303212210030001244234132301200020310012011",
"210101220131232022104432220132221131234351145114524135253112332342312410211104233102330122201111010",
...
"211120022231100333330313111120423213143252332533514251453113433321354142442041432101120010313310122",
"111210213300233203233222413444104203323252533215253431341253534525013210232012413312211122123302112"]

def isVisible(row, col, val):
    top, bottom, left, right = [True, True, True, True]
    # current row values
    for c in range(col):
        if(trees[row][c]>=val):
            left = False
    for c in range(col+1, cols):
        if(trees[row][c]>=val):
            right = False
    # current column values
    for r in range(row):
        if(trees[r][col]>=val):
            top = False
    for r in range(row+1, rows):
        if(trees[r][col]>=val):
            bottom = False
    
    if(not top and not bottom and not left and not right):
        return False
    else:
        return True
        

trees = []

for row in input:
    # list comprehension to convert number into list of ints
    tree_row = [int(x) for x in str(row)]
    trees.append(tree_row)

rows = len(trees[0])
cols = len(trees)
print(f"Rows: {rows}, Cols: {cols}\n")

# number of trees on perimiter
visible = 2*rows+2*cols-4

# for inside subsquare (not on perimeter)
for r in range(1, rows-1):
    for c in range(1, cols-1):
        can_you_see_the_tree = isVisible(r, c, trees[r][c])
        if(can_you_see_the_tree):
            visible += 1
        #print(f"row: {r}, col: {c}, value: {trees[r][c]}, visible?: {can_you_see_the_tree}")
print(f"\nThe number of visible trees is: {visible}")
