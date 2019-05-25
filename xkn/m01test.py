"""
ID: xknxkn1
LANG: PYTHON3
TASK: test
"""
fin = open ('test.in', 'r')
fout = open ('test.out', 'w')
line=fin.readline()
print(line)
x,y = map(int, line.split())
sum = x+y
fout.write (str(sum) + '\n')
fout.close()
