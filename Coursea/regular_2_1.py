import re
l1=list()
handle = open('reg.txt')
for line in handle:
    line= line.strip()
    stuff= re.findall('[0-9]+',line)
    if len(stuff) == 0: continue
    else:
        for i in range(len(stuff)):
            num = int(stuff[i])
            l1.append(num)
#print(f"Length : {len(l1)}")
print(f"Sum : {sum(l1)}")    
        