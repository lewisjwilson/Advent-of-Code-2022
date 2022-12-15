# Question

# --- Part Two ---
# Now, you're ready to choose a directory to delete.
# 
# The total disk space available to the filesystem is 70000000. To run the update, you need unused space of at least 30000000. 
# You need to find a directory you can delete that will free up enough space to run the update.
# 
# In the example above, the total size of the outermost directory (and thus the total amount of used space) is 48381165; 
# this means that the size of the unused space must currently be 21618835, which isn't quite the 30000000 required by the update. 
# Therefore, the update still requires a directory with total size of at least 8381165 to be deleted before it can run.
# 
# To achieve this, you have the following options:
# 
# Delete directory e, which would increase unused space by 584.
# Delete directory a, which would increase unused space by 94853.
# Delete directory d, which would increase unused space by 24933642.
# Delete directory /, which would increase unused space by 48381165.
# Directories e and a are both too small; deleting them would not free up enough space. However, directories d and / are both big enough! Between these, 
# choose the smallest: d, increasing unused space by 24933642.
# 
# Find the smallest directory that, if deleted, would free up enough space on the filesystem to run the update. What is the total size of that directory?



# Solution

input = ["$ cd /",
"$ ls",
...
"$ ls",
"202264 cpqhb.jsf"]


cur_dir = ""
dirs = {}
filesizes_in_dir = 0

for line in input:
    parts = line.split(" ")
    if(parts[0] == "$"):
        filesizes_in_dir = 0
        if(parts[1] == "cd"):
            if(parts[2] == "/"):
                continue
            elif(parts[2] == ".."):
                cur_dir = "/".join(cur_dir.split("/")[:-1])
            else:
                cur_dir = cur_dir + "/" + parts[2]

    # not a command
    else:
        if(parts[0]=="dir"):
            filesizes_in_dir = 0
        else:
            filesizes_in_dir = int(parts[0])
        
        # update value in dict
        dirs.setdefault(cur_dir, 0)
        dirs[cur_dir] = dirs[cur_dir] + filesizes_in_dir

for d1, fs1 in dirs.items():
    for d2, fs2 in dirs.items():
        if(d1 != d2 and d1 in d2):
            dirs[d1] += fs2
    
print(f"Size of root folder is {dirs['']} bytes.\n")
print(f"We require 30000000 free bytes out of 70000000 bytes.")
print(f"That means, the folder to delete should be at least {dirs['']} - (70000000 - 30000000) bytes.")
print(f"Which is {dirs[''] - (70000000-30000000)} bytes.\n")

space_to_free = dirs[''] - (70000000-30000000)

print(f"Directories of this size or more, are:\n")

directory = ''
smol = dirs['']
for d, fs in dirs.items():
    if(fs >= space_to_free):
        print(d, fs)
        if(fs < smol):
            directory = d
            smol = fs

print(f"\nTaking the directory with the smallest value from those directories, we get '{directory}' with size {smol} bytes.")
