import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")

counts = dict()
for line in fhand:
    words = line.decode().split()
    #print(words)
    for word in words:
        counts[word]=counts.get(word,0)+1

#print(counts)
lst=list()
for k,v in counts.items():
    tup = (v,k)
    lst.append(tup)
tmp=list()
tmp=sorted(lst,reverse=True)
print(tmp)
#print(lst.sort(reverse=True))
