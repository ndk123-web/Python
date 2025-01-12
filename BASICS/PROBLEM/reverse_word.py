import re

inp = 'Heloo bhai my name is navnath'

s_split = re.split(r"\s+",inp)
print(s_split)

l = len(s_split)

rev_split = s_split[::-1]

for i in rev_split:
    if(i == r'\s+'):
        print('',end=" ")
    else:
        print(i,end=" ")