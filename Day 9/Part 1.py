instructions = [("U", 2),
("D", 2),
...
("R", 4),
("D", 7)]

def euclidean(head, tail):
    return ((head[0]-tail[0])**2 + (head[1]-tail[1])**2)**.5

head = [0, 0]
minus_one = [0, 0]
tail = [0, 0]
saved_tail = [0, 0]

ed = euclidean(head, tail)

head_moves = list()
head_moves.append(head)

tail_moves = list()
tail_moves.append(tail)

for i in instructions:
    direction = i[0]
    moves = i[1]
    
    for m in range(moves):
        
        if(len(head_moves)>=1):
            minus_one = head_moves[-1]
        
        new_head = head
        if(direction=="U"):
            new_head = [ head[0] + 1, head[1]]
        elif(direction=="D"):
            new_head = [ head[0] - 1, head[1]]
        elif(direction=="R"):
            new_head = [ head[0], head[1] + 1]
        elif(direction=="L"):
            new_head = [ head[0], head[1] - 1]
        else:
            print("Incorrect direction supplied")
         
        head = new_head
        head_moves.append(head)
        
        # calculate euclidean distance between head and tail
        ed = euclidean(head, tail)
        
        # process tail
        if(head==tail or ed<2):
            tail = saved_tail
            tail_moves.append(tail)
        else:
            tail = minus_one
            tail_moves.append(tail)
            saved_tail = tail

# removing duplicate values from list of lists

no_dups = []
for coord in tail_moves:
    if(coord not in no_dups):
        no_dups.append(coord)
        
print(f"The Tail traversed {len(no_dups)} unique spaces.")
