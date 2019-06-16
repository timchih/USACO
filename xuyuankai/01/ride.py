"""
ID: mythica2
LANG: PYTHON3
TASK: ride
"""
rin = open ('ride.in', 'r')
rout = open ('ride.out', 'w')
data = rin.read()
lines = data.split("\n")
num1first = 1
num2first = 1
for i in range(len(lines[0])):
    c=lines[0][i]
    num1 = ord(c)-64
    num1first *= num1
for i in range(len(lines[1])):
    d=lines[1][i]
    num2 = ord(d)-64
    num2first *= num2
print(num1first,num2first)
num1final = num1first%47
num2final = num2first%47
print(num1final,num2final)
if num1final == num2final:
    res = 'GO'
else:
    res = 'STAY'
print(res)
rout.write(res)
rout.write('\n')
rout.close()
rin.close()