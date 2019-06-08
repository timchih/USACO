"""
ID: mythica2
LANG: PYTHON3
TASK: gift1
"""
f=open("gift1.in",'r')
data=f.read()
print(data)
rows=data.split("\n")
print(rows)
names=[]
money={}
np=int(rows[0])
print("np=",np)
for i in range(np):
    name=rows[1+i]
    print("name",name)
    names.append(name)
    money[name]=0
print(money)
def calbalance(pp):
    global rows
    recievers=[]
    sender=rows[pp]
    sendinfostr=rows[pp+1]
    sendinfors=sendinfostr.split(" ")
    smoney=int(sendinfors[0]) 
    snum=int(sendinfors[1])
    if snum !=0:
        smoney_left=smoney%snum
        smoney_each=smoney//snum
    else:
        return pp+2
    for i in range(snum):
        receiver=rows[pp+1+i+1]
        print("receiver i get moeny of ",i,receiver,smoney_each)
        money[receiver]+=smoney_each
    money[sender]-=(smoney-smoney_left)
    print("sender balance",sender,money[sender])
    return pp+1+1+snum
pp=1+np
for i in range(np):
    pp=calbalance(pp)
    print(pp)
print(money)
with open("gift1.out",'w') as fw:
    for i in range(np):
        name=names[i]
        mymoney=money[name]
        outstr=name+" "+str(mymoney)+"\n"
        print(outstr)
        fw.write(outstr)