import sys
import random
map = []
width = 15
length = 15
playmode = False

for _ in range(width*length): 
    map.append(bool(random.getrandbits(1)))

pmap = []
for cell in map:
    if(cell): 
        pmap.append("⬜")
    else: 
        pmap.append("⬛")
i=0
l=0
yCells={}
xCells={}
t=0
for cell in map:
    if(i>=width): i=0
    if(t>=length): 
        l+=1
        t=0
    toAdd = 1 if (cell) else 0
    yCells[i] = yCells.get(i,0)+ toAdd
    xCells[l] = xCells.get(l,0)+ toAdd
    i+=1
    t+=1

print(xCells)
print(yCells)