fname = input("Enter file name: ")
fh = open(fname)
lst = list()
newlst=list()
for line in fh:
    line=line.rstrip()
    lst=line.split()
    for i in lst:
        if i not in newlst:
            newlst.append(i)
newlst.sort()
print(newlst)

