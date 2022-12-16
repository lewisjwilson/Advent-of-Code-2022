# Question

# --- Part Two ---
# Content with the amount of tree cover available, the Elves just need to know the best spot to build their tree house: 
# they would like to be able to see a lot of trees.
# 
# To measure the viewing distance from a given tree, look up, down, left, and right from that tree; 
# stop if you reach an edge or at the first tree that is the same height or taller than the tree under consideration. 
# (If a tree is right on the edge, at least one of its viewing distances will be zero.)
# 
# The Elves don't care about distant trees taller than those found by the rules above; the proposed tree house has large eaves to keep it dry, 
# so they wouldn't be able to see higher than the tree house anyway.
# 
# In the example above, consider the middle 5 in the second row:
# 
# 30373
# 25512
# 65332
# 33549
# 35390
# Looking up, its view is not blocked; it can see 1 tree (of height 3).
# Looking left, its view is blocked immediately; it can see only 1 tree (of height 5, right next to it).
# Looking right, its view is not blocked; it can see 2 trees.
# Looking down, its view is blocked eventually; it can see 2 trees (one of height 3, then the tree of height 5 that blocks its view).
# A tree's scenic score is found by multiplying together its viewing distance in each of the four directions. For this tree, this is 4 
# (found by multiplying 1 * 1 * 2 * 2).
# 
# However, you can do even better: consider the tree of height 5 in the middle of the fourth row:
# 
# 30373
# 25512
# 65332
# 33549
# 35390
# Looking up, its view is blocked at 2 trees (by another tree with a height of 5).
# Looking left, its view is not blocked; it can see 2 trees.
# Looking down, its view is also not blocked; it can see 1 tree.
# Looking right, its view is blocked at 2 trees (by a massive tree of height 9).
# This tree's scenic score is 8 (2 * 2 * 1 * 2); this is the ideal spot for the tree house.
# 
# Consider each tree on your map. What is the highest scenic score possible for any tree?



# Solution

input = ["102200120221123133322123221134224301040024344534431245323303212210030001244234132301200020310012011",
"210101220131232022104432220132221131234351145114524135253112332342312410211104233102330122201111010",
...
"211120022231100333330313111120423213143252332533514251453113433321354142442041432101120010313310122",
"111210213300233203233222413444104203323252533215253431341253534525013210232012413312211122123302112"]

def treesVisible(row, col, val):
    
    up, down, left, right = [0, 0, 0, 0]
    # current row values
    for c in range(col-1, -1, -1):
        if(trees[row][c]<val):
            left += 1
        elif(trees[row][c]>=val):
            left += 1
            break
    for c in range(col+1, cols):
        if(trees[row][c]<val):
            right += 1
        elif(trees[row][c]>=val):
            right += 1
            break
    # current column values
    for r in range(row-1, -1, -1):
        if(trees[r][col]<val):
            up += 1
        elif(trees[r][col]>=val):
            up += 1
            break
    for r in range(row+1, rows):
        if(trees[r][col]<val):
            down += 1
        elif(trees[r][col]>=val):
            down += 1
            break
            
    return up*down*left*right
        

trees = []

for row in input:
    # list comprehension to convert number into list of ints
    tree_row = [int(x) for x in str(row)]
    trees.append(tree_row)

rows = len(trees[0])
cols = len(trees)
print(f"Rows: {rows}, Cols: {cols}\n")

best_tree = (0, 0, 0)

for r in range(rows):
    for c in range(cols):
        vis_idx = treesVisible(r, c, trees[r][c])
        if(best_tree[2]<vis_idx):
            best_tree = (r, c, vis_idx)
            
print(f"\nThe tree with best visibility is at:\nRow: {best_tree[0]}, col: {best_tree[1]}\nwith a visibility index of {best_tree[2]}")
