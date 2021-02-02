name = input("Enter file:")
if len(name) < 1: name = "mbox.txt"
handle = open(name)
di = dict()
tmp_lst=list()
tmp1_lst=list()
for line in handle:
    line = line.strip()
    if line.startswith('From '):
        lst = line.split()
        #print(lst)
        lst_new=lst[5]
        #print(lst_new)
        tmp_lst = lst_new.split(':')
        #print(tmp_lst[0])
        tmp1_lst.append(tmp_lst[0])
        #print(tmp1_lst)

#print(tmp1_lst)
for w in tmp1_lst:
    di[w] = di.get(w, 0) + 1
print(di)
print(sorted(di.items()))
tmp=list()
for k,v in di.items():
    newtup=(k,v)
    tmp.append(newtup)
tmp=sorted(tmp)
#for k,v in tmp:
#    print(k,v)