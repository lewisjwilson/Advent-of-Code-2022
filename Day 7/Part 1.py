input = ["$ cd /",
"$ ls",
...,
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

total = 0
print("Directories to delete:")
for d, fs in dirs.items():
    if(fs <= 100000):
        print(d)
        total += fs
        
print(f"Cumulative filesize of directories to delete: {total} bytes.")
