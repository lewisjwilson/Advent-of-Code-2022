instructions = [("R", 4),
("U", 4),
("L", 3),
("D", 1),
("R", 4),
("D", 1),
("L", 5),
("R", 2)]

head = [0, 0]
minus_one = [0, 0]
minus_two = [0, 0]
tail = [0, 0]

head_moves = list()
head_moves.append(head)

tail_moves = list()
tail_moves.append(tail)

for i in instructions:
    direction = i[0]
    moves = i[1]
    
    for m in range(moves):
        
        if(len(head_moves)>=2):
            minus_one = head_moves[-1]
            minus_two = head_moves[-2]
        
        if(head == tail):
            tail_moves.append(tail)
        
        
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
        
        print(f"H: {head}, H-1: {minus_one}, H-2: {minus_two}, T: {tail}")
        
    
print(head_moves)
        
