input = ["$ cd /",
"$ ls",
...
"$ ls",
"202264 cpqhb.jsf"]

cur_dir = ""
dir_sizes = {}
for line in input:
    parts = line.split(" ")
    #print(line)
    
    # Setting current directory
    if(parts[0] == "$" and parts[1] == "cd"):
        move_to_dir = parts[2] 
        if(move_to_dir == "/"):
            continue
        elif(move_to_dir == ".."):
            #print("Moving up a directory")
            cur_dir = "/".join(cur_dir.split("/")[:-1])
        else:
            #print(f"Moving to: {move_to_dir}")
            cur_dir +="/" +  move_to_dir
        #print(f"Current directory: {cur_dir}")
        
    # if the first part is a number (filesize)
    if(parts[0].isnumeric()):
        dir_sizes[cur_dir] = dir_sizes.get(cur_dir, 0) + int(parts[0])

# Iterating through dictionary to add files from sublevels
for key, val in dir_sizes.items():
    #print(f"{key}   {val} bytes")
    up_dir = "/".join(key.split("/")[:-1])
    if up_dir in dir_sizes:
        dir_sizes[up_dir] = dir_sizes[up_dir] + val

total_size = 0
for key, val in dir_sizes.items():
    if(val <= 100000):
        print(key, val)
        total_size += val
print(f"Total size of dirs <= 100000 bytes is: {total_size} bytes.")
