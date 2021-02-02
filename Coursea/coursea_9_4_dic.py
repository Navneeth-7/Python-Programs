name = input("Enter file:")
if len(name) < 1: name = "mbox.txt"
handle = open(name)
di=dict()
lst_new=list()
for line in handle:
    line=line.strip()
 #   if line.startswith('From '):
    lst = line.split()
    lst_new.append(lst[1])

for w in lst_new:
    di[w]=di.get(w,0)+1

print(di)
largest=-1
name=None
for k,v in di.items():
    if v > largest:
        largest= v
        name = k
print(f"Largest repating value is {name} , count {largest}")