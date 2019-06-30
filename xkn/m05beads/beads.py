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

bcolors=[]

def cutbeads(cutpoint):
    global beads
    cutedbeads=[]
    for i in range(blen):
        pos=(i+cutpoint)%blen
        c=beads[pos]
        cutedbeads.append(c)
    print("cutedbeads:",cutedbeads)
    print("\n")
    return cutedbeads

def countbeadscolor(cb):
    cblen=len(cb)
    headc=0
    tailc=0
    hcolor=cb[0]
    count=headc+tailc
    return count

#bp 0 means in front of first beads
#cb stands for cutted beads
for bp in range(blen):
    cb=cutbeads(bp)
    num=countbeadscolor(cb)
    bcolors.append(num)

maxbeads=max(bcolors)
outstr=str(maxbeads)

with open("beads.out",'w') as fw:
    outstr+="\n"
    print(outstr)
    fw.write(outstr)
