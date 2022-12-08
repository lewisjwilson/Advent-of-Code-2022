import re

input = ["REDACTED",
"REDACTED",
"REDACTED",
...]

cur_dir = ""
dir_sizes = {}
for line in input:
    parts = line.split(" ")
    
    # Setting current directory
    if(parts[0] == "$" and parts[1] == "cd"):
        move_to_dir = parts[2] 
        if(move_to_dir == "/"):
            continue
        elif(move_to_dir == ".."):
            #print("Moving out a directory")
            cur_dir = "/".join(cur_dir.split("/")[:-1])
        else:
            #print(f"Moving to: {move_to_dir}")
            cur_dir +="/" +  move_to_dir
        # print(f"Current directory: {cur_dir}")
        
    # if the first part is a number (filesize)
    if(parts[0].isnumeric()):
        dir_sizes[cur_dir] = dir_sizes.get(cur_dir, 0) + int(parts[0])
        
# for dirs with no files
to_append = {}

# Iterating through dictionary to add files from sublevels
for key, val in dir_sizes.items():
    #print(f"{key}   {val} bytes")
    up_dir = "/".join(key.split("/")[:-1])
    if up_dir in dir_sizes:
        dir_sizes[up_dir] = dir_sizes[up_dir] + val
    else:
        #print(key)
        # dir has no files
        to_append[up_dir] = dir_sizes.get("up_dir", 0)

# merging dicts
dir_sizes = {**dir_sizes , **to_append}
#ordering to move appended values to respective positions
dir_sizes = dict(sorted(dir_sizes.items()))

# Iterating through dictionary to add dirs with no files
for key, val in dir_sizes.items():
    #print(f"{key}   {val} bytes")
    up_dir = "/".join(key.split("/")[:-1])
    if val == 0:
        #print(key)
        for key2, val2 in dir_sizes.items():
            # Regex to match key + "/ccccc" (only one sub folder)
            if(re.search(key + "\/[a-zA-Z0-9]+$", key2)):
                #print(f"2:{key2}")
                dir_sizes[key] += val2

total_size = 0
to_discard = {}

# Iterate through to find dires below 100000 bytes in size
for key, val in dir_sizes.items():
    print(f"{key}   {val} bytes")
    if(val <= 100000):
        to_discard[key] = val
        total_size += val
        
        
print(f"Total size of dirs <= 100000 bytes is: {total_size} bytes.\n")
print("The directories to discard are:\n")
for key, val in to_discard.items():
    print(f"{key} ({val} bytes)")
