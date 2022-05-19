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
cCells={}
i=0
l=0
lCells={}
t=0
for cell in map:
    if(i>=width): i=0
    if(t>=length): 
        l+=1
        t=0
    toAdd = 1 if (cell) else 0
    cCells[i] = cCells.get(i,0)+ toAdd
    lCells[l] = lCells.get(l,0)+ toAdd
    i+=1
    t+=1

widthCount=[]
for f,k in cCells.items():
    widthCount.append(k)
lengthCount=[]
for f,k in lCells.items():
    lengthCount.append(k)

o = 0
maxZ=len(str(max(widthCount)))
for i in widthCount: 
    widthCount[o] = str(i).zfill(maxZ)
    o+=1

a=[]
if(len(str(max(widthCount))) > 1):
    for i in range(len(widthCount[0])):
        for l in widthCount:
            a.append(l[i])
        print('  ', ' '.join(a))
        a=[]
else: 
    print('  ',' '.join(widthCount))



c=0
r=[]
i=0
for cell in pmap:
    c+=1
    r.append(cell) if (not playmode) else r.append("⬜")
    if(c>=width):
        c=0
        print(str(lengthCount[i]).zfill(len(str(max(lengthCount)))),''.join(r))
        i+=1
        r = []
