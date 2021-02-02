fname = input("Enter file name: ")
if len(fname) < 1: fname = "mbox.txt"

fh = open(fname)
count = 0
lst=list()
for lines in fh:
    if  lines.startswith('From '): 
        count=count+1
        lst=lines.split()
        print(lst[1])
    else:
        continue



print("There were", count, "lines in the file with From as the first word")
