# Question

# --- Part Two ---
# Your device's communication system is correctly detecting packets, but still isn't working. It looks like it also needs to look for messages.
# 
# A start-of-message marker is just like a start-of-packet marker, except it consists of 14 distinct characters rather than 4.
# 
# Here are the first positions of start-of-message markers for all of the above examples:
# 
# mjqjpqmgbljsphdztnvjfqwrcgsmlb: first marker after character 19
# bvwbjplbgvbhsrlpgdmjqwftvncz: first marker after character 23
# nppdvjthqldpwncqszvftbrmjlhg: first marker after character 23
# nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg: first marker after character 29
# zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw: first marker after character 26
# How many characters need to be processed before the first start-of-message marker is detected?



# Solution

datastream = "..."

marker = set()
index = 0
position = 14

l = len(datastream)
i = 0

while(i <= l-position):
    marker = set()
    for j in range(i, i+position):
        c = datastream[j]
        marker.add(c)
    if(len(marker)>position-1):
        index = i
        break
    i += 1
    
print(marker, "index: ", i+position)
        
