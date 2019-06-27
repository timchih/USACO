"""
ID: xknxkn1
LANG: PYTHON3
TASK: beads
"""

f=open("beads.in",'r')

blen=int(f.readline())
print(blen)
beads=f.readline()
print(beads)

cutedbeads=[]
maxbeads=0

def cutbeads(cutpoint):
    global beads
    global cutedbeads
    for c in beads:
        #TBD
        cutedbeads.append(c)
    return cutedbeads

def getbeads():
    return 8

#breakpoint 0 means in front of first beads which is 1
for breakpoint in range(blen):
    cutbeads(breakpoint)
    num=getbeads()
    if num>maxbeads:
        maxbeads=num

outstr=str(maxbeads)

with open("beads.out",'w') as fw:
    outstr+="\n"
    print(outstr)
    fw.write(outstr)
