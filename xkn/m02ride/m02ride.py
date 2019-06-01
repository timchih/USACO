"""
ID: xknxkn1
LANG: PYTHON3
PROG: ride
TASK: ride
"""
fin = open ('ride.in', 'r')
fout = open ('ride.out', 'w')
line1=fin.readline()
print("l1",line1)
line2=fin.readline()
print("l2",line2)

def numchar(ichar):
    return ord(ichar)-ord('A')+1

print(numchar('Z'))

p1=1
for chrn in line1:
    print('_',chrn)
    p1*=numchar(chrn)

p2=1
for chrn in line2:
    print('-',chrn)
    p2*=numchar(chrn)

p1m=p1%47
p2m=p2%47

print(p1m,p2m)

answer='STAY'

if p1m == p2m:
    answer='GO'

print(answer)
fout.write ( answer + '\n')
fout.close()
